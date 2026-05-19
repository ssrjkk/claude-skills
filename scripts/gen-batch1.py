import os

def sk(name, desc, cat, tags, models, content):
    path = f'.claude/skills/{cat}/{name}'
    os.makedirs(path, exist_ok=True)
    t = '[' + ', '.join(tags) + ']'
    m = '[' + ', '.join(models) + ']'
    with open(f'{path}/SKILL.md', 'w', encoding='utf-8') as f:
        f.write(f"---\nname: {name}\ndescription: {desc}\ncategory: {cat}\ntags: {t}\nmodels: {m}\nversion: 1.0.0\ncreated: 2026-05-14\n---\n{content}\n")
    print(f'  {cat}/{name}')

# === BACKEND ===
sk("nestjs", "Creates Node.js server-side applications with NestJS, modules, dependency injection, and decorators. Use for enterprise-grade Node.js APIs.", "backend", ["nestjs", "nodejs", "typescript", "api", "decorators"], ["sonnet", "opus"], """# NestJS

> Progressive Node.js framework with TypeScript, decorators, and DI.

## Quick Start
```bash
npm i -g @nestjs/cli && nest new my-api
cd my-api && npm run start:dev
```

## Core Concepts
### Modules
```typescript
@Module({ imports: [UsersModule], controllers: [AppController], providers: [AppService] })
export class AppModule {}
```

### Controllers
```typescript
@Controller('users')
export class UsersController {
  @Get() findAll() { return this.usersService.findAll() }
  @Post() @Body() create(dto: CreateUserDto) { return this.usersService.create(dto) }
}
```

### Providers (Services)
```typescript
@Injectable()
export class UsersService {
  private users: User[] = []
  findAll() { return this.users }
  create(dto: CreateUserDto) { const user = { id: Date.now(), ...dto }; this.users.push(user); return user }
}
```

## When to Use
- Enterprise TypeScript APIs
- Microservices with NATS/RabbitMQ
- GraphQL + REST hybrid APIs
- Projects needing strong structure

## Step-by-Step
1. Init: `nest new project`
2. Generate: `nest g module users`, `nest g controller users`, `nest g service users`
3. Define entities and DTOs
4. Run: `npm run start:dev`

## Validation
1. Server starts on port 3000
2. CRUD endpoints respond correctly
3. Dependency injection resolves providers""")

sk("fastify", "Builds fast and low-overhead Node.js web APIs with Fastify, schema validation, and plugins. Use for high-performance Node.js backends.", "backend", ["fastify", "nodejs", "api", "performance", "validation"], ["sonnet", "opus"], """# Fastify

> Fast and low-overhead Node.js web framework with schema validation.

## Quick Start
```javascript
import Fastify from 'fastify'
const app = Fastify({ logger: true })
app.get('/health', async () => ({ status: 'ok' }))
await app.listen({ port: 3000 })
```

## Schema Validation
```javascript
app.post('/users', {
  schema: {
    body: { type: 'object', properties: { name: { type: 'string' }, email: { type: 'string' } }, required: ['name', 'email'] }
  }
}, async (req, reply) => ({ id: 1, ...req.body }))
```

## Plugins
```javascript
import cors from '@fastify/cors'
import jwt from '@fastify/jwt'
await app.register(cors, { origin: '*' })
await app.register(jwt, { secret: process.env.JWT_SECRET })
app.decorate('authenticate', async (req, reply) => { await req.jwtVerify() })
```

## When to Use
- High-throughput APIs
- JSON schema validated endpoints
- Plugin-based architecture
- Drop-in Express replacement

## Validation
1. Server starts with logging
2. Schema validation rejects invalid input
3. Plugins register without errors""")

sk("actix-web", "Develops high-performance HTTP APIs in Rust with Actix Web, actors, and middleware. Use for maximum throughput web services.", "backend", ["rust", "actix-web", "async", "performance", "api"], ["sonnet", "opus"], """# Actix Web

> Rust's powerful, pragmatic web framework with actor model.

## Quick Start
```rust
use actix_web::{get, web, App, HttpServer, Responder};
#[get("/health")]
async fn health() -> impl Responder { web::Json(json!({"status": "ok"})) }
#[actix_web::main]
async fn main() -> std::io::Result<()> {
    HttpServer::new(|| App::new().service(health))
        .bind(("127.0.0.1", 8080))?.run().await
}
```

## Extractors & State
```rust
use actix_web::web;
use std::sync::Mutex;
struct AppState { counter: Mutex<i32> }
async fn count(data: web::Data<AppState>) -> String {
    let mut c = data.counter.lock().unwrap(); *c += 1; format!("Count: {}", *c)
}
```

## Middleware
```rust
use actix_web::middleware::{Logger, Compress};
HttpServer::new(|| App::new().wrap(Logger::default()).wrap(Compress::default()))
```

## When to Use
- Maximum performance web services
- Rust-native APIs
- Concurrent workloads
- Low-latency requirements

## Validation
1. Server compiles and runs
2. Endpoints return correct status codes
3. Middleware chain executes properly""")

sk("phoenix", "Builds scalable web applications with Phoenix, Elixir, LiveView, and Ecto. Use for real-time, fault-tolerant apps.", "backend", ["phoenix", "elixir", "liveview", "ecto", "realtime"], ["sonnet", "opus"], """# Phoenix

> Elixir web framework with real-time capabilities and fault tolerance.

## Quick Start
```bash
mix phx.new my_app && cd my_app
mix ecto.create && mix phx.server
```

## Contexts
```elixir
defmodule MyApp.Accounts do
  alias MyApp.Accounts.User
  def list_users, do: Repo.all(User)
  def get_user!(id), do: Repo.get!(User, id)
  def create_user(attrs) do
    %User{} |> User.changeset(attrs) |> Repo.insert()
  end
end
```

## LiveView
```elixir
defmodule MyAppWeb.CounterLive do
  use MyAppWeb, :live_view
  def mount(_params, _session, socket) do
    {:ok, assign(socket, :count, 0)}
  end
  def handle_event("inc", _, socket) do
    {:noreply, update(socket, :count, &(&1 + 1))}
  end
end
```

## When to Use
- Real-time applications (chat, notifications)
- Fault-tolerant systems
- Concurrent web apps
- LiveView interactive UIs

## Validation
1. Server starts on port 4000
2. Ecto migrations run successfully
3. LiveView updates in real-time""")

sk("strapi", "Creates headless CMS backends with Strapi, content types, roles, and REST/GraphQL APIs. Use for rapid content management.", "backend", ["strapi", "cms", "headless", "api", "content"], ["sonnet", "opus"], """# Strapi

> Open-source headless CMS with auto-generated APIs.

## Quick Start
```bash
npx create-strapi-app my-project --quickstart
# Admin UI at http://localhost:1337/admin
```

## Content Types
```json
{
  "kind": "collectionType",
  "attributes": {
    "title": { "type": "string", "required": true },
    "body": { "type": "richtext" },
    "author": { "type": "relation", "relation": "manyToOne", "target": "api::author.author" }
  }
}
```

## Custom Controllers
```javascript
// src/api/article/controllers/article.js
module.exports = createCoreController('api::article.article', ({ strapi }) => ({
  async popular(ctx) {
    const articles = await strapi.db.query('api::article.article').findMany({
      where: { views: { $gte: 1000 } },
      orderBy: { views: 'desc' }
    })
    return this.transformResponse(articles)
  }
}))
```

## When to Use
- Content-driven websites
- Mobile app backends
- Blog/News platforms
- Multi-channel content delivery

## Validation
1. Admin panel loads at /admin
2. Content types created and API responds
3. Role-based permissions work correctly""")

sk("pocketbase", "Deploys backend-as-a-service with PocketBase, including embedded SQLite, auth, file storage, and real-time subscriptions. Use for rapid prototyping.", "backend", ["pocketbase", "bas", "sqlite", "auth", "realtime"], ["sonnet", "opus"], """# PocketBase

> Lightweight backend with embedded database, auth, file storage, and admin UI.

## Quick Start
```bash
# Download from pocketbase.io
./pocketbase serve
# Admin UI at http://localhost:8090/_/
```

## Collections & API
```javascript
const pb = new PocketBase('http://localhost:8090')
await pb.admins.authWithPassword('admin@example.com', 'password')
const collection = await pb.collections.create({
  name: 'posts',
  schema: [{ name: 'title', type: 'text', required: true }, { name: 'body', type: 'editor' }, { name: 'published', type: 'bool' }]
})
const record = await pb.collection('posts').create({ title: 'Hello World', body: 'First post', published: true })
```

## Auth Rules
Configure API rules in Admin UI per collection (create, read, update, delete, list).
Use `@request.auth.id != ""` for authenticated users, empty for public.

## When to Use
- Prototypes and MVPs
- Side projects and hackathons
- Small to medium apps
- Embedded database needs

## Validation
1. Admin UI accessible at port 8090
2. Collections created and API responds
3. Auth (email, OAuth2) works correctly""")

sk("hono", "Creates lightweight, fast web APIs with Hono, supporting Cloudflare Workers, Deno, Bun, and Node.js. Use for edge-compatible APIs.", "backend", ["hono", "edge", "cloudflare", "workers", "typescript"], ["sonnet", "opus"], """# Hono

> Ultralight web framework for edge runtimes (Cloudflare Workers, Deno, Bun).

## Quick Start
```typescript
import { Hono } from 'hono'
const app = new Hono()
app.get('/', (c) => c.text('Hello Hono!'))
app.get('/api/users/:id', (c) => c.json({ id: c.req.param('id'), name: 'Alice' }))
export default app
```

## Middleware
```typescript
import { cors } from 'hono/cors'
import { jwt } from 'hono/jwt'
app.use('/api/*', cors())
app.use('/api/admin/*', jwt({ secret: 'my-secret-key' }))
app.onError((err, c) => c.json({ error: err.message }, 500))
```

## When to Use
- Cloudflare Workers APIs
- Edge computing applications
- Multi-runtime deployments
- Minimal bundle size requirements

## Validation
1. Server responds on all target runtimes
2. Middleware chain executes correctly
3. Edge deployment succeeds""")

# === FRONTEND ===
sk("htmx", "Builds dynamic web UIs with htmx, HTML-over-the-Wire, and hypermedia-driven interactions. Use for server-rendered apps with modern UX.", "frontend", ["htmx", "html", "hypermedia", "ajax", "server-rendered"], ["sonnet", "opus"], """# htmx

> Access modern browser features directly from HTML, without JavaScript.

## Quick Start
```html
<script src="https://unpkg.com/htmx.org"></script>
<button hx-get="/api/clicked" hx-swap="outerHTML">Click Me</button>
<div hx-get="/api/updates" hx-trigger="every 10s" hx-target="#status">Loading...</div>
```

## Core Attributes
- `hx-get`, `hx-post`, `hx-put`, `hx-delete` — HTTP methods
- `hx-target` — Where to swap response content
- `hx-swap` — How to swap (innerHTML, outerHTML, beforebegin, afterend, delete, none)
- `hx-trigger` — Event that triggers request (click, change, keyup, every 5s, revealed, etc.)
- `hx-indicator` — Loading indicator element

## When to Use
- Server-rendered applications
- Progressive enhancement
- Django/Rails/Express apps
- Replacing jQuery interactions

## Validation
1. AJAX requests replace content correctly
2. All triggers fire as expected
3. Form submissions work without page reload""")

sk("qwik", "Creates instant-loading web applications with Qwik, resumability, and fine-grained lazy loading. Use for maximum performance SPAs.", "frontend", ["qwik", "resumable", "performance", "framework", "typescript"], ["sonnet", "opus"], """# Qwik

> Resumable framework for instant-loading web applications.

## Quick Start
```bash
npm create qwik@latest
cd my-app && npm start
```

## Components
```tsx
export default component$(() => {
  const count = useSignal(0)
  return <button onClick$={() => count.value++}>{count.value}</button>
})
```

## Route Loaders
```tsx
export const useData = routeLoader$(async () => {
  const data = await fetch('https://api.example.com/data')
  return data.json()
})
```

## When to Use
- SEO-critical applications
- Slow network environments
- Large enterprise SPAs
- E-commerce and content sites

## Validation
1. App loads instantly on first visit
2. Code splits and lazy loads correctly
3. Resumability preserves state after pause""")

sk("lit", "Builds fast, standard-compliant web components with Lit, reactive properties, and Shadow DOM. Use for framework-agnostic UI.", "frontend", ["lit", "web-components", "shadow-dom", "reactive", "standards"], ["sonnet", "opus"], """# Lit

> Simple library for building fast, lightweight web components.

## Quick Start
```javascript
import { LitElement, html, css } from 'lit'
class MyElement extends LitElement {
  static properties = { name: { type: String } }
  static styles = css`h1 { color: blue; }`
  render() { return html`<h1>Hello, ${this.name}!</h1>` }
}
customElements.define('my-element', MyElement)
```

## Reactive Properties & Lifecycle
```javascript
static properties = { count: { type: Number } }
constructor() { super(); this.count = 0 }
connectedCallback() { super.connectedCallback(); console.log('mounted') }
updated(changedProperties) { if (changedProperties.has('count')) console.log('count changed') }
```

## When to Use
- Framework-agnostic components
- Design system elements
- Micro-frontend architectures
- Shadow DOM encapsulation

## Validation
1. Custom elements register and render
2. Properties update reactively
3. Shadow DOM isolates styles""")

sk("docusaurus", "Creates documentation websites with Docusaurus, MDX, versioning, and search. Use for open-source docs and knowledge bases.", "frontend", ["docusaurus", "docs", "mdx", "documentation", "static-site"], ["sonnet", "opus"], """# Docusaurus

> Build optimized documentation websites with React and MDX.

## Quick Start
```bash
npx create-docusaurus@latest my-docs classic
cd my-docs && npm start
```

## Sidebar Configuration
```javascript
module.exports = { tutorialSidebar: ['intro', { type: 'category', label: 'Getting Started', items: ['installation', 'quickstart'] }] }
```

## MDX Features
```mdx
import Tabs from '@theme/Tabs'; import TabItem from '@theme/TabItem'
<Tabs><TabItem value="npm" label="npm">npm install</TabItem><TabItem value="yarn" label="yarn">yarn add</TabItem></Tabs>
```

## When to Use
- Open-source project documentation
- API reference sites
- Internal knowledge bases
- Product documentation portals

## Validation
1. Dev server starts on port 3000
2. Search indexes content correctly
3. Versioning works with multiple docs versions""")

sk("alpinejs", "Adds JavaScript behavior to HTML with Alpine.js, a minimal reactive framework. Use for sprinkling interactivity into server-rendered apps.", "frontend", ["alpinejs", "javascript", "reactive", "html", "lightweight"], ["sonnet", "opus"], """# Alpine.js

> Minimal JavaScript framework for composing behavior directly in HTML.

## Quick Start
```html
<script src="https://unpkg.com/alpinejs" defer></script>
<div x-data="{ count: 0 }">
  <button @click="count++">Clicked <span x-text="count"></span> times</button>
</div>
```

## Directives
- `x-data` — Component data scope
- `x-bind` / `:` — Bind attributes
- `x-on` / `@` — Event listeners
- `x-show` — Toggle visibility (`display: none`)
- `x-model` — Two-way binding
- `x-for` — Loops over arrays
- `x-text` — Set innerText
- `x-html` — Set innerHTML

## When to Use
- Server-rendered HTML with interactivity
- Laravel/Rails/Django apps
- Replacing jQuery
- Simple interactive components

## Validation
1. Reactive state updates DOM
2. Event handlers fire correctly
3. x-show and x-if toggle visibility""")

sk("sass-scss", "Writes maintainable CSS with Sass/SCSS, including variables, mixins, nesting, and partials. Use for scalable stylesheets.", "frontend", ["sass", "scss", "css", "preprocessor", "styling"], ["sonnet", "opus"], """# Sass/SCSS

> Professional CSS preprocessor with variables, mixins, and nesting.

## Quick Start
```scss
$primary: #007bff;
.card { font-family: 'Inter', sans-serif; padding: 1rem;
  &-header { font-size: 1.25rem; }
  &-body { padding: 0.5rem 0; }
}
```

## Mixins & Functions
```scss
@mixin respond-to($bp) {
  @if $bp == md { @media (min-width: 768px) { @content; } }
}
@function rem($px) { @return $px / 16px * 1rem; }
.element { font-size: rem(16px); @include respond-to(md) { width: 50%; } }
```

## When to Use
- Large CSS codebases
- Design system foundations
- Reusable style patterns
- Team-scale CSS projects

## Validation
1. SCSS compiles to valid CSS
2. Mixins output correct styles
3. Variables cascade properly""")

# === MOBILE ===
sk("react-native-bare", "Develops React Native applications without Expo, using native modules, libraries, and custom builds. Use for advanced RN projects.", "mobile", ["react-native", "mobile", "native-modules", "typescript", "ios"], ["sonnet", "opus"], """# React Native (Bare)

> React Native without Expo — full control over native code.

## Quick Start
```bash
npx react-native init MyApp --template react-native-template-typescript
cd MyApp && npx react-native run-ios
```

## Native Modules (iOS)
```objectivec
// MyModule.m
#import <React/RCTBridgeModule.h>
@interface RCT_EXTERN_MODULE(MyModule, NSObject)
RCT_EXTERN_METHOD(doSomething:(NSString *)input resolver:(RCTPromiseResolveBlock)resolve rejecter:(RCTPromiseRejectBlock)reject)
@end
```

## Third-Party Libraries
```bash
npm install react-native-vision-camera react-native-reanimated react-native-gesture-handler
cd ios && pod install
```

## When to Use
- Custom native module requirements
- Maximum performance control
- Existing native codebases
- Complex native integrations

## Validation
1. App builds for iOS and Android
2. Native modules link correctly
3. Metro bundler starts without errors""")

sk("ionic", "Builds cross-platform mobile apps with Ionic, Angular/React/Vue, and Capacitor. Use for hybrid apps with native-like UI.", "mobile", ["ionic", "mobile", "hybrid", "angular", "capacitor"], ["sonnet", "opus"], """# Ionic

> Cross-platform mobile SDK with native-style UI components.

## Quick Start
```bash
npm install -g @ionic/cli
ionic start my-app blank --type=angular
cd my-app && ionic serve
```

## Pages
```typescript
import { Component } from '@angular/core'
@Component({
  selector: 'app-home',
  template: `<ion-header><ion-toolbar><ion-title>Home</ion-title></ion-toolbar></ion-header>
    <ion-content><ion-list><ion-item *ngFor="let item of items">{{ item.name }}</ion-item></ion-list></ion-content>`
})
export class HomePage { items = [{name: 'Item 1'}, {name: 'Item 2'}] }
```

## Navigation
```typescript
import { NavController } from '@ionic/angular'
this.navCtrl.navigateForward('/details', { state: { id: 1 } })
```

## When to Use
- Rapid cross-platform development
- Web-to-mobile conversion
- Enterprise mobile apps
- Prototypes with native feel

## Validation
1. App runs in browser with ionic serve
2. Platform builds succeed for iOS/Android
3. UI components render with correct styling""")

# === DEVOPS ===
sk("terraform-azure", "Provisions Azure infrastructure using Terraform modules for compute, networking, and managed services. Use for Azure IaC.", "devops", ["terraform", "azure", "infrastructure", "iac", "cloud"], ["sonnet", "opus"], """# Terraform Azure

> Infrastructure as code for Microsoft Azure.

## Quick Start
```hcl
provider "azurerm" { features {} }
resource "azurerm_resource_group" "main" { name = "my-resources"; location = "West Europe" }
resource "azurerm_linux_web_app" "app" {
  name = "my-webapp"; resource_group_name = azurerm_resource_group.main.name
  location = azurerm_resource_group.main.location; service_plan_id = azurerm_service_plan.main.id
  site_config { application_stack { node_version = "20-lts" } }
}
```

## When to Use
- Azure resource provisioning
- Multi-cloud infrastructure
- Enterprise compliance
- Repeatable environments

## Validation
1. terraform plan shows expected resources
2. Azure resources create successfully
3. terraform destroy cleans up properly""")

sk("pulumi", "Provisions cloud infrastructure with Pulumi using TypeScript, Python, Go, or C#. Use for modern IaC with real programming languages.", "devops", ["pulumi", "iac", "typescript", "cloud", "infrastructure"], ["sonnet", "opus"], """# Pulumi

> Infrastructure as code using general-purpose programming languages.

## Quick Start
```typescript
import * as aws from '@pulumi/aws'
const bucket = new aws.s3.Bucket('my-bucket', { website: { indexDocument: 'index.html' } })
export const bucketName = bucket.id
export const bucketUrl = bucket.websiteEndpoint
```

## Resources & Export
```typescript
const cluster = new aws.ecs.Cluster('cluster')
const service = new aws.ecs.Service('service', { cluster: cluster.arn, taskDefinition: taskDef.arn, desiredCount: 2 })
export const serviceArn = service.arn
```

## When to Use
- TypeScript/Python/Go-native IaC
- Complex infrastructure logic
- Cloud-native applications
- Team-familiar languages

## Validation
1. pulumi up completes without errors
2. Resources created correctly
3. pulumi destroy cleans up all resources""")

sk("cloudflare", "Configures Cloudflare for CDN, DNS, Workers, D1, R2, and Durable Objects. Use for edge computing and site acceleration.", "devops", ["cloudflare", "cdn", "workers", "dns", "edge"], ["sonnet", "opus"], """# Cloudflare

> Edge network platform for CDN, DNS, Workers, and storage.

## Quick Start (Worker)
```typescript
export default { async fetch(request): Promise<Response> {
  const url = new URL(request.url)
  if (url.pathname === '/api/hello') {
    return new Response(JSON.stringify({ message: 'Hello from edge!' }), { headers: { 'Content-Type': 'application/json' } })
  }
  return fetch(request)
}}
```

## D1 Database
```typescript
export default { async fetch(request, env) {
  const { results } = await env.DB.prepare('SELECT * FROM users WHERE id = ?').bind(1).all()
  return Response.json(results)
}}
```

## R2 Storage
```typescript
await env.MY_BUCKET.put('file.txt', 'Hello World')
const object = await env.MY_BUCKET.get('file.txt')
```

## When to Use
- Global CDN and caching
- Edge compute applications
- DNS management
- DDoS protection

## Validation
1. DNS resolves through Cloudflare
2. Workers deploy and respond
3. Cache headers respected correctly""")

sk("vercel", "Deploys frontend applications with Vercel, including serverless functions, preview deployments, and edge functions.", "devops", ["vercel", "deployment", "serverless", "frontend", "edge"], ["sonnet", "opus"], """# Vercel

> Frontend deployment platform with serverless functions and edge compute.

## Quick Start
```bash
npm install -g vercel
vercel deploy
```

## Serverless Functions
```typescript
// api/users.ts
import type { VercelRequest, VercelResponse } from '@vercel/node'
export default function handler(req: VercelRequest, res: VercelResponse) {
  res.json({ users: [{ id: 1, name: 'Alice' }] })
}
```

## Edge Middleware
```typescript
// middleware.ts
export default function middleware(request: Request) {
  const country = request.headers.get('x-vercel-ip-country')
  return new Response(`Hello from ${country}`, { headers: { 'x-edge': 'true' } })
}
export const config = { matcher: '/api/edge' }
```

## When to Use
- Frontend deployments
- Next.js applications
- Preview deployments per branch
- Edge computing needs

## Validation
1. Deploy succeeds with zero errors
2. Preview URL works correctly
3. Serverless functions respond""")

sk("netlify", "Deploys static sites and serverless functions with Netlify, including forms, identity, and split testing.", "devops", ["netlify", "deployment", "static-site", "jamstack", "serverless"], ["sonnet", "opus"], """# Netlify

> All-in-one platform for static sites and serverless functions.

## Quick Start
```bash
npm install -g netlify-cli
netlify deploy --prod
```

## Functions
```javascript
// netlify/functions/hello.js
exports.handler = async (event, context) => ({
  statusCode: 200,
  body: JSON.stringify({ message: 'Hello from Netlify!' })
})
```

## Redirects (_redirects)
```
/api/*    https://api.example.com/:splat   200
/blog/*   /blog/:splat
/*        /index.html                       200
```

## When to Use
- Static site hosting
- JAMstack architectures
- Form handling without backend
- Branch-based previews

## Validation
1. Deploy succeeds via CLI or Git
2. Functions respond correctly
3. Redirects work as configured""")

sk("grafana", "Creates dashboards and visualizations with Grafana, including Prometheus data sources, alerting, and annotations.", "devops", ["grafana", "monitoring", "dashboards", "visualization", "alerting"], ["sonnet", "opus"], """# Grafana

> Open-source monitoring and observability platform.

## Quick Start
```bash
docker run -d -p 3000:3000 --name grafana grafana/grafana
# UI at http://localhost:3000 (admin/admin)
```

## Dashboard JSON
```json
{
  "title": "System Overview",
  "panels": [{
    "title": "CPU Usage",
    "type": "timeseries",
    "datasource": "Prometheus",
    "targets": [{ "expr": "100 - (avg by(instance) (rate(node_cpu_seconds_total{mode=\"idle\"}[5m])) * 100)" }]
  }]
}
```

## Alert Rules
```yaml
groups:
  - name: instance_down
    rules:
      - alert: InstanceDown
        expr: up == 0
        for: 5m
        labels: { severity: critical }
        annotations: { summary: "Instance {{ $labels.instance }} down" }
```

## When to Use
- Infrastructure dashboards
- Application performance monitoring
- Multi-source observability
- Team alerting

## Validation
1. Data source connects successfully
2. Panels display real-time data
3. Alerts fire correctly""")

sk("opentelemetry", "Implements observability with OpenTelemetry for distributed tracing, metrics, and logs collection.", "devops", ["opentelemetry", "observability", "tracing", "metrics", "monitoring"], ["sonnet", "opus"], """# OpenTelemetry

> Unified observability framework for traces, metrics, and logs.

## Quick Start (Node.js)
```javascript
const { NodeSDK } = require('@opentelemetry/sdk-node')
const { ConsoleSpanExporter } = require('@opentelemetry/sdk-trace-base')
const sdk = new NodeSDK({ traceExporter: new ConsoleSpanExporter() })
sdk.start()
```

## Distributed Tracing
```javascript
const { trace } = require('@opentelemetry/api')
const tracer = trace.getTracer('my-service')
const span = tracer.startSpan('process-order')
span.setAttribute('order.id', orderId)
span.end()
```

## Metrics
```javascript
const meter = metrics.getMeter('my-service')
const requestCounter = meter.createCounter('requests.total', { description: 'Total requests' })
requestCounter.add(1, { route: '/api/users' })
```

## When to Use
- Microservices observability
- Distributed tracing
- Multi-vendor telemetry
- Standardized instrumentation

## Validation
1. Traces appear in collector
2. Metrics export correctly
3. Context propagation works across services""")

sk("helm", "Packages and deploys Kubernetes applications with Helm, including charts, templates, and releases.", "devops", ["helm", "kubernetes", "charts", "packaging", "deployment"], ["sonnet", "opus"], """# Helm

> Kubernetes package manager with charts, templates, and release management.

## Quick Start
```bash
helm create my-app
helm install my-release ./my-app
helm list
```

## Chart Structure
```
my-app/
  Chart.yaml          # Metadata
  values.yaml         # Default configuration
  templates/          # K8s manifests with Go templates
    deployment.yaml
    service.yaml
    _helpers.tpl
```

## Go Templates
```yaml
apiVersion: apps/v1
kind: Deployment
spec:
  replicas: {{ .Values.replicaCount }}
  template:
    spec:
      containers:
        - name: {{ .Chart.Name }}
          image: "{{ .Values.image.repository }}:{{ .Values.image.tag }}"
```

## When to Use
- Standardized Kubernetes deployments
- Multi-environment configurations
- Application package distribution
- CI/CD for Kubernetes

## Validation
1. helm lint passes without errors
2. helm template renders correct manifests
3. helm install creates resources successfully""")

sk("kubernetes", "Deploys and manages containerized applications on Kubernetes with pods, deployments, services, and ingress.", "devops", ["kubernetes", "k8s", "containers", "orchestration", "deployment"], ["sonnet", "opus"], """# Kubernetes

> Container orchestration platform for deploying and scaling applications.

## Quick Start
```yaml
apiVersion: apps/v1; kind: Deployment; metadata: { name: nginx-deployment }
spec:
  replicas: 3; selector: { matchLabels: { app: nginx } }
  template:
    metadata: { labels: { app: nginx } }
    spec: { containers: [{ name: nginx, image: nginx:latest, ports: [{ containerPort: 80 }] }] }
```
```bash
kubectl apply -f deployment.yaml
```

## Services & Ingress
```yaml
apiVersion: v1; kind: Service; metadata: { name: nginx-service }
spec:
  type: LoadBalancer; selector: { app: nginx }
  ports: [{ port: 80, targetPort: 80 }]
```

## kubectl Essentials
```bash
kubectl get pods                    # List pods
kubectl logs -f deployment/nginx    # Follow logs
kubectl exec -it pod-name -- bash   # Shell into pod
kubectl port-forward svc/nginx 8080:80  # Port forward
kubectl delete all -l app=nginx     # Delete by label
```

## When to Use
- Container orchestration at scale
- Microservices deployments
- CI/CD pipelines
- Hybrid/multi-cloud apps

## Validation
1. kubectl get pods shows all pods running
2. Services are accessible
3. Rolling updates work without downtime""")

# === DATA ===
sk("apache-spark", "Processes large-scale data with Apache Spark using DataFrames, RDDs, and Spark SQL. Use for big data ETL and analytics.", "data", ["spark", "big-data", "dataframe", "pyspark", "analytics"], ["sonnet", "opus"], """# Apache Spark

> Unified analytics engine for large-scale data processing.

## Quick Start
```python
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("MyApp").getOrCreate()
df = spark.read.csv("data/*.csv", header=True, inferSchema=True)
df.groupBy("category").agg({"amount": "sum"}).show()
```

## DataFrame API
```python
from pyspark.sql.functions import col, avg, when
result = df.filter(col("age") > 18) \\
    .withColumn("adult", when(col("age") >= 21, "yes").otherwise("no")) \\
    .groupBy("department").agg(avg("salary").alias("avg_salary"))
```

## Spark SQL
```python
df.createOrReplaceTempView("users")
result = spark.sql("SELECT department, AVG(salary) as avg_salary FROM users GROUP BY department")
```

## When to Use
- Terabyte-scale data processing
- ETL pipelines
- Interactive analytics
- ML feature engineering

## Validation
1. SparkContext initializes
2. DataFrame operations execute
3. Spark SQL queries return correct results""")

sk("apache-flink", "Builds real-time stream processing applications with Apache Flink, event time, and exactly-once semantics.", "data", ["flink", "stream-processing", "realtime", "events", "java"], ["sonnet", "opus"], """# Apache Flink

> Stream processing framework for real-time data pipelines.

## Quick Start
```java
StreamExecutionEnvironment env = StreamExecutionEnvironment.getExecutionEnvironment();
DataStream<String> stream = env.socketTextStream("localhost", 9999);
stream.flatMap((line, out) -> { for (String word : line.split(" ")) out.collect(word); })
    .keyBy(word -> word).sum(1).print();
env.execute("WordCount");
```

## Windows
```java
stream.keyBy(event -> event.getUserId())
    .window(TumblingEventTimeWindows.of(Time.hours(1)))
    .aggregate(new AverageAggregate())
```

## When to Use
- Real-time data pipelines
- Event-driven applications
- Streaming ETL
- Fraud detection

## Validation
1. Job submits to Flink cluster
2. Stream processes events correctly
3. Checkpoints restore state on failure""")

sk("pytorch", "Builds and trains deep learning models with PyTorch, including tensors, autograd, and neural network modules.", "data", ["pytorch", "deep-learning", "neural-networks", "tensor", "gpu"], ["sonnet", "opus"], """# PyTorch

> Machine learning framework with dynamic computation graphs.

## Quick Start
```python
import torch, torch.nn as nn
model = nn.Sequential(nn.Linear(784, 256), nn.ReLU(), nn.Linear(256, 10), nn.LogSoftmax(dim=1))
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
for images, labels in dataloader:
    output = model(images); loss = nn.CrossEntropyLoss()(output, labels)
    loss.backward(); optimizer.step(); optimizer.zero_grad()
```

## Custom Module
```python
class MyCNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(1, 32, 3); self.dropout = nn.Dropout2d(0.25)
        self.fc1 = nn.Linear(5408, 128)
    def forward(self, x):
        x = self.conv1(x); x = self.dropout(x); return self.fc1(x)
```

## When to Use
- Deep learning research
- Custom neural architectures
- NLP and computer vision
- GPU-accelerated training

## Validation
1. Model runs forward pass without error
2. Loss decreases during training
3. GPU utilization is correct""")

sk("jupyter", "Creates and manages Jupyter notebooks for data analysis, visualization, and reproducible research.", "data", ["jupyter", "notebooks", "python", "data-science", "visualization"], ["sonnet", "opus"], """# Jupyter

> Interactive computing environment for data science and research.

## Quick Start
```bash
pip install jupyterlab
jupyter lab
```

## Magic Commands
```python
%matplotlib inline           # Show plots inline
%timeit df.groupby('col').sum()  # Time execution
%load_ext autoreload         # Auto-reload modules
%autoreload 2
%%bash                      # Run bash commands
echo "Hello from shell"
```

## When to Use
- Exploratory data analysis
- Reproducible research
- Data storytelling
- Model prototyping

## Validation
1. JupyterLab UI loads correctly
2. Kernels execute code successfully
3. Plots render inline""")

sk("pandas", "Manipulates and analyzes data with pandas, including DataFrames, group operations, and time series.", "data", ["pandas", "python", "dataframe", "data-analysis", "csv"], ["sonnet", "opus"], """# Pandas

> Data manipulation and analysis library for Python.

## Quick Start
```python
import pandas as pd
df = pd.read_csv('data.csv')
df.info(); df.describe(); df['category'].value_counts()
```

## Selection & Grouping
```python
df[df['price'] > 100]                              # Filter
df.groupby('category').agg({'price': ['mean', 'std'], 'quantity': 'sum'})
df['date'] = pd.to_datetime(df['date'])
df.set_index('date', inplace=True).resample('M').mean()  # Time series
```

## When to Use
- CSV/Excel data analysis
- Data cleaning and transformation
- Time series analysis
- ETL pipeline development

## Validation
1. DataFrame operations execute correctly
2. GroupBy aggregations return expected values
3. Missing values handled properly""")

# === DATABASE ===
sk("mysql", "Designs and manages MySQL databases with schemas, indexes, queries, and replication. Use for relational data storage.", "database", ["mysql", "sql", "database", "relational", "queries"], ["sonnet", "opus"], """# MySQL

> Popular open-source relational database management system.

## Quick Start
```sql
CREATE DATABASE myapp; USE myapp;
CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100) NOT NULL, email VARCHAR(255) UNIQUE NOT NULL, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
```

## Indexes & Optimization
```sql
CREATE INDEX idx_email ON users(email);
CREATE FULLTEXT INDEX idx_search ON posts(title, body);
EXPLAIN SELECT * FROM users WHERE email = 'test@example.com';
```

## When to Use
- Web application backends
- Content management systems
- E-commerce platforms
- Relational data with joins

## Validation
1. Connection to MySQL succeeds
2. Queries return correct results
3. EXPLAIN shows index usage""")

sk("sqlite", "Embeds SQLite databases in applications with zero configuration and single-file storage. Use for local data persistence.", "database", ["sqlite", "sql", "embedded", "database", "lightweight"], ["sonnet", "opus"], """# SQLite

> Self-contained, serverless, zero-configuration SQL database engine.

## Quick Start
```bash
sqlite3 mydb.db
CREATE TABLE users (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, email TEXT UNIQUE NOT NULL);
INSERT INTO users (name, email) VALUES ('Alice', 'alice@example.com');
SELECT * FROM users;
```

## CLI Commands
```bash
.tables          # List tables
.schema users    # Show schema
.mode json       # JSON output
.headers on      # Show column headers
```

## Python Integration
```python
import sqlite3
conn = sqlite3.connect('mydb.db')
cursor = conn.execute('SELECT * FROM users WHERE id = ?', (1,))
```

## When to Use
- Mobile app storage
- Desktop application data
- Prototypes and testing
- Embedded/IoT devices

## Validation
1. Database file creates correctly
2. SQL queries execute without error
3. Transactions commit and rollback""")

sk("cassandra", "Models and queries data with Apache Cassandra for high-availability, partition-tolerant NoSQL workloads.", "database", ["cassandra", "nosql", "wide-column", "distributed", "database"], ["sonnet", "opus"], """# Apache Cassandra

> Highly-scalable, partition-tolerant NoSQL database.

## Quick Start
```sql
CREATE KEYSPACE myapp WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 1};
USE myapp;
CREATE TABLE users (user_id UUID PRIMARY KEY, name TEXT, email TEXT, created_at TIMESTAMP);
CREATE TABLE orders_by_user (user_id UUID, order_id UUID, total DECIMAL, created_at TIMESTAMP, PRIMARY KEY (user_id, created_at, order_id)) WITH CLUSTERING ORDER BY (created_at DESC);
```

## When to Use
- High-write-throughput applications
- Time-series data
- IoT sensor data
- Multi-region deployments

## Validation
1. Node joins the cluster
2. CQL queries return correct data
3. Replication works across nodes""")

sk("neo4j", "Models graph data with Neo4j and Cypher query language for connected data and relationship-rich domains.", "database", ["neo4j", "graph", "cypher", "nosql", "relationships"], ["sonnet", "opus"], """# Neo4j

> Graph database for connected data with Cypher query language.

## Quick Start
```cypher
CREATE (alice:Person {name: 'Alice', age: 30})
CREATE (bob:Person {name: 'Bob', age: 25})
CREATE (alice)-[:KNOWS {since: 2020}]->(bob)
MATCH (n:Person) RETURN n.name, n.age
```

## Graph Queries
```cypher
MATCH path = shortestPath((alice:Person {name: 'Alice'})-[:KNOWS*]-(charlie:Person {name: 'Charlie'}))
RETURN path
MATCH (user:Person {name: 'Alice'})-[:PURCHASED]->(product)<-[:PURCHASED]-(other)-[:PURCHASED]->(rec)
WHERE NOT (user)-[:PURCHASED]->(rec)
RETURN rec.name, COUNT(*) as score ORDER BY score DESC LIMIT 5
```

## When to Use
- Social networks
- Recommendation engines
- Fraud detection
- Knowledge graphs

## Validation
1. Neo4j service is running
2. Nodes and relationships created
3. Cypher queries return expected patterns""")

sk("influxdb", "Collects and queries time-series data with InfluxDB, Flux language, and continuous queries.", "database", ["influxdb", "time-series", "metrics", "monitoring", "database"], ["sonnet", "opus"], """# InfluxDB

> Purpose-built time-series database for metrics and events.

## Quick Start
```bash
docker run -d -p 8086:8086 influxdb:2.0
# UI at http://localhost:8086
```

## Line Protocol
```
weather,location=us-east,sensor=temp-a temperature=72.5,humidity=0.45 1705312800000000000
```

## Flux Query
```flux
from(bucket: "sensor-data")
  |> range(start: -1h)
  |> filter(fn: (r) => r._measurement == "weather" and r._field == "temperature")
  |> aggregateWindow(every: 5m, fn: mean)
```

## When to Use
- Infrastructure monitoring metrics
- IoT sensor data
- Application performance tracking
- Real-time analytics

## Validation
1. InfluxDB responds on port 8086
2. Data writes via line protocol succeed
3. Flux queries return time-bucketed results""")

sk("clickhouse", "Analyzes large datasets with ClickHouse, column-oriented DBMS for real-time analytical queries.", "database", ["clickhouse", "olap", "analytics", "columnar", "sql"], ["sonnet", "opus"], """# ClickHouse

> Column-oriented DBMS for real-time analytical queries.

## Quick Start
```sql
CREATE TABLE orders (order_id UInt64, user_id UInt32, amount Decimal(10,2), created_at DateTime)
ENGINE = MergeTree() ORDER BY created_at;
```

## Partitioning & Optimization
```sql
CREATE TABLE events (event_date Date, event_type String, user_id UInt32, value Float64)
ENGINE = MergeTree() PARTITION BY toYYYYMM(event_date) ORDER BY (event_type, event_date);
```

## Analytics
```sql
SELECT toStartOfMonth(created_at) AS month, user_id, COUNT(*) AS order_count, SUM(amount) AS total_spent
FROM orders GROUP BY month, user_id ORDER BY total_spent DESC LIMIT 10;
```

## When to Use
- Real-time analytics dashboards
- Clickstream analysis
- Log analytics
- OLAP workloads

## Validation
1. ClickHouse accepts connections
2. Tables created and data inserted
3. Aggregation queries complete quickly""")

sk("firebase", "Builds serverless applications with Firebase, including Firestore, Auth, Cloud Functions, and Realtime Database.", "database", ["firebase", "google", "serverless", "realtime", "auth"], ["sonnet", "opus"], """# Firebase

> Google's app development platform with backend services.

## Quick Start
```javascript
import { initializeApp } from 'firebase/app'
import { getFirestore, collection, addDoc, getDocs, query, where } from 'firebase/firestore'
const app = initializeApp({ /* config */ })
const db = getFirestore(app)
await addDoc(collection(db, 'users'), { name: 'Alice', email: 'alice@example.com' })
const q = query(collection(db, 'users'), where('name', '==', 'Alice'))
const snap = await getDocs(q)
```

## Auth & Functions
```javascript
import { getAuth, signInWithPopup, GoogleAuthProvider } from 'firebase/auth'
const auth = getAuth(app)
const result = await signInWithPopup(auth, new GoogleAuthProvider())
```

## When to Use
- Rapid prototyping
- Real-time collaborative apps
- Mobile app backends
- Serverless architectures

## Validation
1. Firebase app initializes
2. Firestore read/write operations succeed
3. Auth providers authenticate users""")

print(f'Batch 1 complete: 32 skills created')
