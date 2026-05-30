# Contributing to Claude Skills Library

## Welcome!

We're excited that you want to contribute to the Claude Skills Library! This is a collaborative project that benefits from community input.

## How to Contribute

### Adding a New Skill

1. **Choose a Category**: Pick an existing category or propose a new one
2. **Get a Skill ID**: Follow the naming convention (Category-Subcategory-Number)
3. **Use the Template**: Copy the standard skill template
4. **Write Content**: Follow the structure guidelines
5. **Add Examples**: Include real, working code examples
6. **Test**: Verify all examples work
7. **Submit**: Create a pull request

### Skill Template

```markdown
# [SKILL_ID]: Skill Name

**Category:** Category > Subcategory
**Difficulty:** Beginner/Intermediate/Advanced
**Time to Master:** X minutes/hours
**Prerequisites:** [Related Skills]

## Overview
[2-3 sentence description]

## Learning Objectives
- Objective 1
- Objective 2
- Objective 3

## Step-by-Step Instructions

### Step 1: [Action]
[Instructions]

### Step 2: [Action]
[Instructions]

## Code Examples

```language
[Code example]
```

## Common Pitfalls
- Pitfall 1
- Pitfall 2

## Advanced Tips
- Tip 1
- Tip 2

## Related Skills
- [Related Skill]

## Resources
- [Resource Link]
```

## Naming Conventions

### Category Prefixes (2-3 letters)

```
SD = Software Development
TQ = Testing & QA
DD = DevOps & Deployment
DS = Data Science & ML
WD = Web Development
SC = Security & Compliance
DC = Documentation
PT = Productivity Tools
BA = Business Analytics
IS = Infrastructure & Systems
```

### Subcategory Examples

```
SD-LANG = Programming Languages
SD-ARCH = Architecture
WD-FE = Frontend
WD-BE = Backend
DD-DOCKER = Docker
DD-K8S = Kubernetes
```

### Numbering

Sequential from 001 onwards within each subcategory.

## Content Guidelines

### Writing Style

- **Clear**: Use simple, direct language
- **Practical**: Focus on actionable steps
- **Complete**: Include all necessary details
- **Examples**: Provide working code samples
- **Professional**: Maintain consistent tone

### Code Quality

- **Working Code**: All examples must be tested
- **Comments**: Explain complex logic
- **Best Practices**: Follow industry standards
- **Multiple Languages**: Show variations where relevant
- **Error Handling**: Include error cases

### Structure

- **Clear Headings**: Organize content logically
- **Numbered Steps**: Easy to follow
- **Code Blocks**: Proper syntax highlighting
- **Links**: Cross-reference related skills
- **Resources**: Provide external references

## Quality Checklist

Before submitting:

- [ ] Unique, valid Skill ID
- [ ] Follows template structure
- [ ] Clear, professional writing
- [ ] All code examples tested
- [ ] Proper Markdown formatting
- [ ] Related skills linked
- [ ] No spelling/grammar errors
- [ ] All headings present
- [ ] Resources section included
- [ ] Time estimate is realistic
- [ ] Prerequisites clearly listed

## Pull Request Process

1. **Fork** the repository
2. **Create Branch**: `git checkout -b add-skill-xy-001`
3. **Make Changes**: Add your new skill
4. **Commit**: `git commit -m "Add XY-001: Skill Name"`
5. **Push**: `git push origin add-skill-xy-001`
6. **Create PR**: Fill in the template
7. **Respond**: Address review feedback
8. **Merge**: Once approved

## PR Template

```markdown
## Description

Briefly describe the skill(s) being added.

## Type of Change

- [ ] New skill
- [ ] Updated existing skill
- [ ] Fixed typo/error
- [ ] Added examples

## Checklist

- [ ] Content follows template
- [ ] Code examples are tested
- [ ] Markdown is properly formatted
- [ ] No duplicate skills
- [ ] Skills are linked appropriately
- [ ] References are included

## Related Issue

Closes #(issue number)
```

## Editing Existing Skills

If you find errors or want to improve existing skills:

1. **Identify Issues**: Note what needs fixing
2. **Make Changes**: Edit the relevant file
3. **Test Updates**: Verify examples still work
4. **Document Changes**: Explain your edits
5. **Submit PR**: Follow the pull request process

## Proposing New Categories

If you think we need new categories:

1. **Create Issue**: Propose the category
2. **Explain Scope**: Why is it needed?
3. **Suggest Skills**: What would it contain?
4. **Get Feedback**: Wait for community input
5. **Implement**: Once approved

## Code of Conduct

We are committed to providing a welcoming community:

- Be respectful and inclusive
- Give credit to others
- Provide constructive feedback
- Respect different perspectives
- Report issues professionally

## Questions?

- Check existing issues
- Review the FAQ
- Email: support@claude-skills.io
- Discussions: Use GitHub Discussions

## Recognition

Contributors will be:

- Listed in CONTRIBUTORS.md
- Thanked in release notes
- Featured in monthly highlights
- Given contributor badge

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

**Thank you for contributing to Claude Skills Library!**

Together, we're building the most comprehensive development skills resource.
