import * as vscode from "vscode"
import * as path from "path"
import * as fs from "fs"

interface Skill {
  name: string
  description: string
  category: string
  tags: string[]
  models: string[]
  version: string
  path: string
  languages: string[]
  has_ru: boolean
  created: string
  updated: string
}

interface CatalogData {
  metadata: {
    schema_version: string
    generated_at: string
    total_skills: number
    total_ru: number
    domains: string[]
    bilingual: boolean
  }
  skills: Skill[]
}

class CatalogProvider implements vscode.TreeDataProvider<SkillTreeItem> {
  private _onDidChangeTreeData = new vscode.EventEmitter<SkillTreeItem | undefined>()
  readonly onDidChangeTreeData = this._onDidChangeTreeData.event
  private catalog: CatalogData | null = null

  constructor() {
    this.loadCatalog()
  }

  async loadCatalog(): Promise<void> {
    const url = vscode.workspace.getConfiguration("claudeSkills").get<string>("catalogUrl", "")
    if (!url) return
    try {
      const response = await fetch(url)
      this.catalog = await response.json()
      this.normalizeCatalog()
    } catch (e) {
      vscode.window.showErrorMessage(`Failed to load catalog: ${e}`)
    }
    this.refresh()
  }

  private normalizeCatalog(): void {
    if (!this.catalog) return
    for (const skill of this.catalog.skills) {
      if (typeof skill.tags === "string") {
        skill.tags = (skill.tags as string).split(",").map((t: string) => t.trim()).filter(Boolean)
      }
      if (typeof skill.models === "string") {
        skill.models = (skill.models as string).split(",").map((t: string) => t.trim()).filter(Boolean)
      }
    }
  }

  refresh(): void {
    this._onDidChangeTreeData.fire(undefined)
  }

  getTreeItem(element: SkillTreeItem): vscode.TreeItem {
    return element
  }

  getChildren(element?: SkillTreeItem): Thenable<SkillTreeItem[]> {
    if (!this.catalog) return Promise.resolve([])

    if (!element) {
      return Promise.resolve(this.getCategories())
    }

    if (element.contextValue === "category") {
      return Promise.resolve(this.getSkillsForCategory(element.label as string))
    }

    return Promise.resolve([])
  }

  private getCategories(): SkillTreeItem[] {
    if (!this.catalog) return []
    const counts = new Map<string, number>()
    for (const s of this.catalog.skills) {
      counts.set(s.category, (counts.get(s.category) || 0) + 1)
    }
    return this.catalog.metadata.domains.map((d) => {
      const item = new SkillTreeItem(`${d} (${counts.get(d) || 0})`, vscode.TreeItemCollapsibleState.Collapsed)
      item.contextValue = "category"
      item.iconPath = new vscode.ThemeIcon("folder")
      return item
    })
  }

  private getSkillsForCategory(category: string): SkillTreeItem[] {
    if (!this.catalog) return []
    const cat = category.replace(/ \(\d+\)$/, "")
    return this.catalog.skills
      .filter((s) => s.category === cat)
      .slice(0, 50)
      .map((s) => {
        const item = new SkillTreeItem(s.name, vscode.TreeItemCollapsibleState.None)
        item.contextValue = "skill"
        item.description = s.description.slice(0, 60) + (s.description.length > 60 ? "..." : "")
        item.tooltip = new vscode.MarkdownString(`**${s.name}**\n\n${s.description}\n\nTags: ${s.tags.join(", ")}`)
        item.iconPath = new vscode.ThemeIcon("book")
        item.command = {
          command: "claudeSkills.openSkill",
          title: "Open Skill",
          arguments: [s],
        }
        return item
      })
  }

  search(query: string): SkillTreeItem[] {
    if (!this.catalog || !query) return []
    const q = query.toLowerCase()
    return this.catalog.skills
      .filter((s) => s.name.toLowerCase().includes(q) || s.description.toLowerCase().includes(q) || s.tags.some((t) => t.toLowerCase().includes(q)))
      .slice(0, 50)
      .map((s) => {
        const item = new SkillTreeItem(s.name, vscode.TreeItemCollapsibleState.None)
        item.contextValue = "skill"
        item.description = s.description.slice(0, 60)
        item.tooltip = new vscode.MarkdownString(`**${s.name}** (_${s.category}_)\n\n${s.description}`)
        item.iconPath = new vscode.ThemeIcon("book")
        return item
      })
  }
}

class SkillTreeItem extends vscode.TreeItem {
  constructor(label: string, collapsibleState: vscode.TreeItemCollapsibleState) {
    super(label, collapsibleState)
  }
}

class InstalledSkillsProvider implements vscode.TreeDataProvider<SkillTreeItem> {
  private _onDidChangeTreeData = new vscode.EventEmitter<SkillTreeItem | undefined>()
  readonly onDidChangeTreeData = this._onDidChangeTreeData.event

  refresh(): void {
    this._onDidChangeTreeData.fire(undefined)
  }

  getTreeItem(element: SkillTreeItem): vscode.TreeItem {
    return element
  }

  getChildren(element?: SkillTreeItem): Thenable<SkillTreeItem[]> {
    if (element) return Promise.resolve([])

    const skillsDir = vscode.workspace.getConfiguration("claudeSkills").get<string>("skillsDir", ".claude/skills")
    if (!vscode.workspace.workspaceFolders) return Promise.resolve([])

    const root = vscode.workspace.workspaceFolders[0].uri.fsPath
    const fullPath = path.join(root, skillsDir)

    if (!fs.existsSync(fullPath)) {
      return Promise.resolve([new SkillTreeItem("No skills installed", vscode.TreeItemCollapsibleState.None)])
    }

    const items: SkillTreeItem[] = []
    try {
      for (const domain of fs.readdirSync(fullPath)) {
        const domainPath = path.join(fullPath, domain)
        if (!fs.statSync(domainPath).isDirectory()) continue
        const skills = fs.readdirSync(domainPath).filter((f) => fs.statSync(path.join(domainPath, f)).isDirectory())
        for (const skill of skills) {
          const item = new SkillTreeItem(`${domain}/${skill}`, vscode.TreeItemCollapsibleState.None)
          item.contextValue = "installed"
          item.iconPath = new vscode.ThemeIcon("check")
          item.command = {
            command: "vscode.open",
            title: "Open",
            arguments: [vscode.Uri.file(path.join(domainPath, skill, "SKILL.md"))],
          }
          items.push(item)
        }
      }
    } catch {
      // ignore
    }

    if (items.length === 0) {
      items.push(new SkillTreeItem("No skills installed", vscode.TreeItemCollapsibleState.None))
    }

    return Promise.resolve(items)
  }
}

async function installSkill(skill: Skill): Promise<void> {
  if (!vscode.workspace.workspaceFolders) {
    vscode.window.showErrorMessage("Open a workspace first")
    return
  }

  const skillsDir = vscode.workspace.getConfiguration("claudeSkills").get<string>("skillsDir", ".claude/skills")
  const root = vscode.workspace.workspaceFolders[0].uri.fsPath
  const targetDir = path.join(root, skillsDir, skill.category, skill.name)

  if (fs.existsSync(targetDir)) {
    vscode.window.showInformationMessage(`Skill "${skill.name}" is already installed`)
    return
  }

  const baseUrl = "https://raw.githubusercontent.com/ssrjkk/claude-skills/main/.claude/skills"
  const files = [`${baseUrl}/${skill.category}/${skill.name}/SKILL.md`]
  if (skill.has_ru) {
    files.push(`${baseUrl}/${skill.category}/${skill.name}/SKILL.ru.md`)
  }

  fs.mkdirSync(targetDir, { recursive: true })

  try {
    for (const url of files) {
      const response = await fetch(url)
      const content = await response.text()
      const filename = url.endsWith("SKILL.ru.md") ? "SKILL.ru.md" : "SKILL.md"
      fs.writeFileSync(path.join(targetDir, filename), content, "utf-8")
    }
    vscode.window.showInformationMessage(`Installed skill: ${skill.name}`)
  } catch (e) {
    fs.rmSync(targetDir, { recursive: true, force: true })
    vscode.window.showErrorMessage(`Failed to install skill: ${e}`)
  }
}

async function openSkillPreview(skill: Skill): Promise<void> {
  const panel = vscode.window.createWebviewPanel("skillPreview", `Skill: ${skill.name}`, vscode.ViewColumn.One, {})
  const tags = skill.tags.map((t) => `<span class="tag">${t}</span>`).join(" ")
  const ruBadge = skill.has_ru ? '<span class="badge">RU</span>' : ""

  panel.webview.html = `<!DOCTYPE html>
<html lang="en">
<head>
  <style>
    body { font-family: -apple-system, system-ui, sans-serif; padding: 2rem; max-width: 800px; margin: 0 auto; color: var(--vscode-editor-foreground); background: var(--vscode-editor-background); }
    h1 { font-size: 1.8rem; margin-bottom: 0.5rem; }
    .meta { color: var(--vscode-descriptionForeground); font-size: 0.9rem; margin-bottom: 0.5rem; }
    .badge { display: inline-block; padding: 2px 8px; border-radius: 4px; font-size: 0.75rem; font-weight: 600; background: #7C3AED; color: white; margin-left: 8px; }
    .tags { margin: 1rem 0; }
    .tag { display: inline-block; padding: 2px 8px; border-radius: 12px; font-size: 0.75rem; background: var(--vscode-badge-background); color: var(--vscode-badge-foreground); margin-right: 4px; margin-bottom: 4px; }
    .description { font-size: 1.1rem; line-height: 1.6; margin: 1rem 0; color: var(--vscode-editor-foreground); }
    .actions { margin-top: 2rem; }
    .btn { display: inline-block; padding: 8px 16px; background: #7C3AED; color: white; border: none; border-radius: 6px; font-size: 0.9rem; cursor: pointer; }
    .info { margin: 1rem 0; font-size: 0.85rem; color: var(--vscode-descriptionForeground); }
  </style>
</head>
<body>
  <h1>${skill.name} ${ruBadge}</h1>
  <div class="meta">${skill.category} · v${skill.version} · ${skill.models.join(", ")}</div>
  <div class="tags">${tags}</div>
  <div class="description">${skill.description}</div>
  <div class="info">Created: ${skill.created} · Updated: ${skill.updated}</div>
  <div class="actions">
    <button class="btn" onclick="install()">Install Skill</button>
  </div>
  <script>
    const vscode = acquireVsCodeApi();
    function install() { vscode.postMessage({ command: 'install' }); }
  </script>
</body>
</html>`

  panel.webview.onDidReceiveMessage((msg) => {
    if (msg.command === "install") {
      installSkill(skill)
    }
  })
}

export function activate(context: vscode.ExtensionContext) {
  const catalogProvider = new CatalogProvider()
  const installedProvider = new InstalledSkillsProvider()

  context.subscriptions.push(
    vscode.window.registerTreeDataProvider("claudeSkillsCatalog", catalogProvider),
    vscode.window.registerTreeDataProvider("claudeSkillsInstalled", installedProvider)
  )

  context.subscriptions.push(
    vscode.commands.registerCommand("claudeSkills.install", () => {
      vscode.window.showInformationMessage("Select a skill from the catalog to install")
    })
  )

  context.subscriptions.push(
    vscode.commands.registerCommand("claudeSkills.refresh", () => {
      catalogProvider.loadCatalog()
      installedProvider.refresh()
    })
  )

  context.subscriptions.push(
    vscode.commands.registerCommand("claudeSkills.search", async () => {
      const query = await vscode.window.showInputBox({ prompt: "Search skills by name, description, or tag", placeHolder: "e.g. react, docker, testing" })
      if (!query) return

      const results = catalogProvider.search(query)
      const pick = await vscode.window.showQuickPick(
        results.map((r) => ({ label: r.label, description: r.description, skill: r })),
        { placeHolder: `Found ${results.length} skills` }
      )
      if (pick) {
        const skill = catalogProvider["catalog"]?.skills.find((s) => s.name === pick.label)
        if (skill) openSkillPreview(skill)
      }
    })
  )

  context.subscriptions.push(
    vscode.commands.registerCommand("claudeSkills.openSkill", (skill: Skill) => {
      openSkillPreview(skill)
    })
  )

  context.subscriptions.push(
    vscode.commands.registerCommand("claudeSkills.openSkillFromTree", async (item: SkillTreeItem) => {
      const skill = catalogProvider["catalog"]?.skills.find((s) => s.name === item.label)
      if (skill) openSkillPreview(skill)
    })
  )

  catalogProvider.loadCatalog()
}

export function deactivate() {}
