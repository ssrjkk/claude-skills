#!/usr/bin/env python3
"""Generate 5000 SKILL.md files using compact data-driven templates (v3)."""
import os, sys, re

BASE = ".claude/skills"
os.makedirs(BASE, exist_ok=True)

TMPL = {}
TMPL["framework"] = """---
name: {name}
description: {description}
category: {category}
tags: [{tags}]
models: [gpt-4, claude-3]
version: "1.0"
---

# {display_name}

> {description}

## Quick Start
```{lang}
{quickstart}
```

## When to Use
- Building applications with {item_name}
- {use1}
- {use2}
- {use3}

## Step-by-Step
1. Install: `{install}`
2. {step1}
3. {step2}
4. {step3}
5. {step4}

## Dependencies
- {item_name} {version}
- {dep1}
- {dep2}

## Examples
```{lang}
{example}
```

## Resources
- Official {item_name} documentation
- Community tutorials
- GitHub repositories

## Validation
- Run: `{verify}`
- Test with sample data
- Verify output correctness
"""

TMPL["tool"] = """---
name: {name}
description: {description}
category: {category}
tags: [{tags}]
models: [gpt-4, claude-3]
version: "1.0"
---

# {display_name}

> {description}

## Quick Start
```bash
{quickstart}
```

## When to Use
- Using {item_name} in your workflow
- {use1}
- {use2}

## Step-by-Step
1. Install {item_name}: `{install}`
2. {step1}
3. {step2}
4. {step3}

## Dependencies
- {item_name} {version}
- {dep1}

## Examples
```bash
{example}
```

## Resources
- Official documentation
- Community guides and tutorials

## Validation
- Verify: `{verify}`
- Check expected output
"""

TMPL["concept"] = """---
name: {name}
description: {description}
category: {category}
tags: [{tags}]
models: [gpt-4, claude-3]
version: "1.0"
---

# {display_name}

> {description}

## Quick Start
{quickstart}

## When to Use
- {use1}
- {use2}
- {use3}

## Step-by-Step
1. {step1}
2. {step2}
3. {step3}
4. {step4}
5. {step5}

## Dependencies
{no_deps}: No external dependencies

## Examples
{example}

## Resources
- Best practices and guidelines
- Industry standards

## Validation
- {verify}
"""

TMPL["platform"] = """---
name: {name}
description: {description}
category: {category}
tags: [{tags}]
models: [gpt-4, claude-3]
version: "1.0"
---

# {display_name}

> {description}

## Quick Start
```bash
{quickstart}
```

## When to Use
- Deploying on {item_name}
- {use1}
- {use2}

## Step-by-Step
1. Sign up / configure: `{install}`
2. {step1}
3. {step2}
4. {step3}

## Dependencies
- {item_name} account
- {dep1}

## Examples
```bash
{example}
```

## Resources
- {item_name} documentation
- API reference

## Validation
- Verify: `{verify}`
- Check dashboard / logs
"""

def norm(n):
    return n.lower().replace(" ", "-").replace("_", "-")

def tagify(*args):
    return ", ".join(norm(x) for x in args)

def cap_name(s):
    return " ".join(x.capitalize() for x in s.split("-"))

def gen_tag(name, topic, category, extra=""):
    parts = [name, topic, category]
    if extra: parts.append(extra)
    return tagify(*parts)

# Compact generator: items x topics
# item: (id, display_name) or just id (display = cat(id))
# topic: (suffix, display_suffix, use1, use2, use3)

def expand_items(items):
    """Expand item format: str -> (str, cat(str)), tuple -> as-is"""
    for it in items:
        if isinstance(it, str):
            yield it, cap_name(it)
        else:
            yield it[0], it[1]

def make_skills(category, sub, items, topics, template, lang, extra_tag=""):
    """Generate skill dicts from compact items x topics."""
    result = []
    for item_id, item_disp in expand_items(items):
        for tp in topics:
            suf, tdisp, *uses = tp
            uses = (uses + ["", "", ""])[:3]
            name = f"{norm(item_id)}-{norm(suf)}"
            display = f"{item_disp} {tdisp}"
            desc = f"{tdisp} with {item_disp}. {uses[0]}."
            result.append({
                "name": name, "display_name": display, "description": desc,
                "category": category, "template": template,
                "lang": lang, "item_name": item_disp,
                "tags": gen_tag(item_id, suf, category, extra_tag),
                "quickstart": f"# {display}\n# See {item_disp} docs",
                "install": f"pip install {norm(item_id)}" if template in ("framework",) and lang == "python" else f"npm install {norm(item_id)}" if template == "framework" else f"# Install {item_disp}",
                "use1": uses[0] or f"using {item_disp}",
                "use2": uses[1] or tdisp,
                "use3": uses[2] or f"{category} development",
                "step1": f"Set up {item_disp}",
                "step2": f"Configure {tdisp}",
                "step3": f"Implement features",
                "step4": f"Test and verify",
                "step5": f"Deploy and monitor",
                "version": ">= latest stable",
                "dep1": f"Runtime environment",
                "dep2": f"Dependencies as needed",
                "no_deps": "No external dependencies required",
                "example": f"# {display}\n# See {item_disp} documentation",
                "verify": f"{norm(item_id)} --version",
            })
    return result

# =======================================================
# AI SKILLS (llm-frameworks, ml-tools, dl-frameworks, nlp, cv)
# =======================================================

AI_GROUPS = [
    ("ai", "llm-fw", [
        "langchain", "llama-index", "haystack", "semantic-kernel", "dspy",
        "guidance", "outlines", "marvin", "promptflow", "vllm"
    ], [
        ("rag", "RAG", "building RAG systems", "document QA", "semantic search"),
        ("agents", "Agents", "building agents", "tool use", "autonomous reasoning"),
        ("memory", "Memory", "conversation memory", "state persistence", "context management"),
        ("prompting", "Prompt Engineering", "prompt templates", "few-shot", "output control"),
        ("evaluation", "Evaluation", "LLM evaluation", "quality metrics", "testing"),
        ("tool-use", "Tool Use", "function calling", "API integration", "external tools"),
        ("streaming", "Streaming", "token streaming", "real-time output", "async comms"),
        ("chaining", "Chaining", "multi-step workflows", "pipeline composition", "sequences"),
        ("embeddings", "Embeddings", "text embeddings", "vector search", "representations"),
        ("fine-tuning", "Fine-Tuning", "model customization", "domain adaptation", "optimization"),
    ], "framework", "python", "llm"),

    ("ai", "ml-libs", [
        "scikit-learn", "xgboost", "lightgbm", "catboost", "optuna",
        "hyperopt", "ray-tune", "tpot", "auto-sklearn", "flaml",
        "mlflow", "wandb", "neptune", "clearml", "dvc",
    ], [
        ("classification", "Classification", "building classifiers", "label prediction", "category assignment"),
        ("regression", "Regression", "predicting values", "trend analysis", "forecasting"),
        ("clustering", "Clustering", "grouping data", "segmentation", "pattern discovery"),
        ("hyperparameter-tuning", "Hyperparameter Tuning", "optimizing params", "model tuning", "performance"),
        ("feature-engineering", "Feature Engineering", "creating features", "transformation", "reduction"),
        ("pipeline", "Pipeline", "ML pipelines", "workflow automation", "end-to-end"),
        ("model-selection", "Model Selection", "choosing models", "comparison", "selection"),
        ("experiment-tracking", "Experiment Tracking", "tracking experiments", "logging", "analysis"),
        ("deployment", "Deployment", "model serving", "API endpoints", "production"),
        ("monitoring", "Monitoring", "model monitoring", "drift detection", "performance"),
    ], "framework", "python", "ml"),

    ("ai", "dl-libs", [
        "pytorch", "tensorflow", "keras", "jax", "mxnet",
        "paddlepaddle", "caffe2", "chainer", "tvm", "onnx",
        "transformers", "diffusers", "accelerate", "bitsandbytes", "trl", "peft",
    ], [
        ("training", "Training", "training models", "model fitting", "learning"),
        ("inference", "Inference", "running models", "prediction", "forward pass"),
        ("optimization", "Optimization", "model optimization", "tuning", "efficiency"),
        ("distributed", "Distributed", "distributed training", "multi-GPU", "parallel"),
        ("quantization", "Quantization", "model quantization", "precision reduction", "compression"),
        ("pruning", "Pruning", "model pruning", "sparsity", "compression"),
        ("transfer-learning", "Transfer Learning", "transfer learning", "pretrained", "fine-tuning"),
        ("data-loading", "Data Loading", "data pipelines", "dataset loading", "preprocessing"),
        ("checkpointing", "Checkpointing", "model saving", "checkpoints", "resume"),
        ("visualization", "Visualization", "model viz", "training graphs", "loss curves"),
    ], "framework", "python", "deep-learning"),

    ("ai", "nlp-tools", [
        "spacy", "nltk", "stanza", "flair", "textblob",
        "gensim", "fasttext", "tokenizers", "sentence-transformers", "trankit",
    ], [
        ("tokenization", "Tokenization", "text tokenization", "word splitting", "subword"),
        ("ner", "NER", "named entity recognition", "entity extraction", "information extraction"),
        ("pos-tagging", "POS Tagging", "POS tagging", "grammar labeling", "linguistic analysis"),
        ("sentiment", "Sentiment Analysis", "sentiment detection", "opinion mining", "emotion analysis"),
        ("text-classification", "Text Classification", "document categorization", "text labeling", "filtering"),
        ("dependency-parsing", "Dependency Parsing", "syntax analysis", "dependency trees", "parsing"),
        ("lemmatization", "Lemmatization", "word lemmatization", "root forms", "morphology"),
        ("summarization", "Summarization", "text summarization", "abstractive", "extractive"),
        ("translation", "Translation", "machine translation", "language translation", "text translation"),
        ("similarity", "Similarity", "text similarity", "semantic similarity", "matching"),
    ], "framework", "python", "nlp"),

    ("ai", "cv-tools", [
        "opencv", "pillow", "scikit-image", "albumentations", "imgaug",
        "kornia", "detectron2", "mmdetection", "yolo", "pytorch-lightning",
    ], [
        ("image-classification", "Image Classification", "classifying images", "recognition", "labeling"),
        ("object-detection", "Object Detection", "detecting objects", "bounding boxes", "localization"),
        ("segmentation", "Segmentation", "image segmentation", "pixel classification", "region detection"),
        ("image-augmentation", "Image Augmentation", "data augmentation", "transformation", "expansion"),
        ("feature-extraction", "Feature Extraction", "extracting features", "keypoints", "descriptors"),
        ("face-detection", "Face Detection", "facial recognition", "face detection", "verification"),
        ("optical-flow", "Optical Flow", "motion detection", "optical flow", "video analysis"),
        ("image-filtering", "Image Filtering", "image filters", "convolution", "noise reduction"),
        ("edge-detection", "Edge Detection", "edge detection", "boundary detection", "contours"),
        ("color-processing", "Color Processing", "color manipulation", "color spaces", "correction"),
    ], "framework", "python", "computer-vision"),
]

# =======================================================
# BACKEND SKILLS (languages, frameworks, tools, patterns)
# =======================================================

BACKEND_GROUPS = [
    ("backend", "langs", [
        "python", "javascript", "typescript", "java", "csharp",
        "go", "rust", "php", "ruby", "scala",
        "kotlin", "elixir", "swift", "crystal", "nim",
        "zig", "haskell", "clojure", "erlang", "dart",
    ], [
        ("rest-api", "REST API", "building REST APIs", "HTTP endpoints", "web services"),
        ("cli-tool", "CLI Tool", "building CLI tools", "command-line apps", "utilities"),
        ("web-framework", "Web Framework", "web dev", "HTTP servers", "web apps"),
        ("orm", "ORM", "database access", "object-relational mapping", "persistence"),
        ("testing", "Testing", "writing tests", "unit testing", "automation"),
        ("async", "Async", "async operations", "concurrent code", "event loops"),
        ("logging", "Logging", "app logging", "structured logging", "management"),
        ("config", "Configuration", "config management", "env config", "settings"),
        ("error-handling", "Error Handling", "error management", "exception handling", "fault tolerance"),
        ("dependency-injection", "DI", "DI containers", "inversion of control", "modular code"),
    ], "framework", "python", "backend"),

    ("backend", "python-fw", [
        ("django", "Django"), ("flask", "Flask"), ("fastapi", "FastAPI"),
        ("bottle", "Bottle"), ("tornado", "Tornado"), ("pyramid", "Pyramid"),
        ("sanic", "Sanic"), ("starlette", "Starlette"), ("aiohttp", "aiohttp"),
        ("falcon", "Falcon"), ("masonite", "Masonite"), ("responder", "Responder"),
    ], [
        ("routing", "Routing", "HTTP routing", "URL handling", "request routing"),
        ("middleware", "Middleware", "middleware pipelines", "request processing", "cross-cutting"),
        ("templating", "Templating", "server templates", "view rendering", "template engines"),
        ("auth", "Authentication", "user auth", "login", "access control"),
        ("database", "Database", "DB access", "persistence", "query building"),
        ("testing", "Testing", "integration tests", "unit tests", "API testing"),
        ("deployment", "Deployment", "production deploy", "server config", "hosting"),
        ("websocket", "WebSocket", "real-time", "WebSocket", "live updates"),
    ], "framework", "python", "backend"),

    ("backend", "java-fw", [
        ("spring-boot", "Spring Boot"), ("micronaut", "Micronaut"), ("quarkus", "Quarkus"),
        ("dropwizard", "Dropwizard"), ("play", "Play"), ("vertx", "Vert.x"),
        ("grails", "Grails"), ("javalin", "Javalin"), ("spark", "Spark"),
    ], [
        ("routing", "Routing", "HTTP routing", "endpoints", "mapping"),
        ("middleware", "Middleware", "request processing", "filters", "interceptors"),
        ("database", "Database", "DB access", "JPA", "repositories"),
        ("auth", "Auth", "security", "authentication", "authorization"),
        ("testing", "Testing", "unit tests", "integration", "mocking"),
        ("deployment", "Deployment", "build", "deploy", "packaging"),
        ("config", "Config", "configuration", "properties", "profiles"),
        ("monitoring", "Monitoring", "metrics", "health checks", "observability"),
    ], "framework", "java", "backend"),

    ("backend", "go-fw", [
        ("gin", "Gin"), ("echo", "Echo"), ("fiber", "Fiber"), ("chi", "Chi"),
        ("revel", "Revel"), ("beego", "Beego"), ("buffalo", "Buffalo"), ("kit", "Go Kit"),
    ], [
        ("routing", "Routing", "HTTP routing", "endpoints", "handlers"),
        ("middleware", "Middleware", "request pipeline", "logging", "auth"),
        ("database", "Database", "DB access", "SQL", "migrations"),
        ("testing", "Testing", "unit tests", "table-driven tests", "benchmarks"),
        ("deployment", "Deployment", "build", "cross-compile", "deploy"),
        ("config", "Config", "config management", "env vars", "files"),
        ("templating", "Templating", "HTML templates", "views", "rendering"),
        ("grpc", "gRPC", "gRPC services", "protobuf", "RPC"),
    ], "framework", "go", "backend"),

    ("backend", "rust-fw", [
        ("actix-web", "Actix Web"), ("axum", "Axum"), ("rocket", "Rocket"),
        ("tide", "Tide"), ("warp", "Warp"), ("poem", "Poem"), ("salvo", "Salvo"),
    ], [
        ("routing", "Routing", "HTTP routing", "endpoints", "handlers"),
        ("middleware", "Middleware", "request pipeline", "processing", "filters"),
        ("database", "Database", "DB access", "SQLx", "Diesel"),
        ("testing", "Testing", "unit tests", "integration", "cargo test"),
        ("async", "Async", "async handlers", "tokio", "futures"),
        ("templating", "Templating", "templates", "views", "rendering"),
        ("deployment", "Deployment", "build", "release", "deploy"),
        ("websocket", "WebSocket", "real-time", "WebSocket", "live"),
    ], "framework", "rust", "backend"),

    ("backend", "ruby-fw", [
        ("rails", "Rails"), ("sinatra", "Sinatra"), ("hanami", "Hanami"),
        ("roda", "Roda"), ("cuba", "Cuba"), ("grape", "Grape"), ("padrino", "Padrino"),
    ], [
        ("routing", "Routing", "HTTP routing", "endpoints", "routes"),
        ("middleware", "Middleware", "rack middleware", "pipeline", "filters"),
        ("database", "Database", "ActiveRecord", "migrations", "queries"),
        ("testing", "Testing", "RSpec", "Minitest", "integration"),
        ("templating", "Templating", "ERB", "Haml", "Slim"),
        ("deployment", "Deployment", "deploy", "Capistrano", "hosting"),
        ("auth", "Auth", "authentication", "authorization", "Devise"),
        ("api", "API", "API building", "JSON APIs", "REST"),
    ], "framework", "ruby", "backend"),

    ("backend", "php-fw", [
        ("laravel", "Laravel"), ("symfony", "Symfony"), ("codeigniter", "CodeIgniter"),
        ("cakephp", "CakePHP"), ("yii", "Yii"), ("laminas", "Laminas"),
        ("slim", "Slim"), ("phalcon", "Phalcon"),
    ], [
        ("routing", "Routing", "HTTP routing", "endpoints", "controllers"),
        ("middleware", "Middleware", "pipeline", "filters", "processing"),
        ("database", "Database", "Eloquent", "doctrine", "queries"),
        ("testing", "Testing", "PHPUnit", "integration", "feature tests"),
        ("templating", "Templating", "Blade", "Twig", "views"),
        ("deployment", "Deployment", "deploy", "hosting", "optimization"),
        ("auth", "Auth", "authentication", "authorization", "security"),
        ("api", "API", "APIs", "REST", "JSON"),
    ], "framework", "php", "backend"),

    ("backend", "js-fw", [
        ("express", "Express"), ("koa", "Koa"), ("fastify", "Fastify"),
        ("nestjs", "NestJS"), ("hono", "Hono"), ("adonisjs", "AdonisJS"),
        ("sails", "Sails.js"), ("loopback", "LoopBack"), ("feathers", "FeathersJS"),
    ], [
        ("routing", "Routing", "HTTP routing", "endpoints", "handlers"),
        ("middleware", "Middleware", "request pipeline", "logging", "error handling"),
        ("database", "Database", "ORM", "Prisma", "Mongoose"),
        ("testing", "Testing", "Jest", "Vitest", "integration"),
        ("templating", "Templating", "Pug", "EJS", "views"),
        ("deployment", "Deployment", "deploy", "serverless", "hosting"),
        ("auth", "Auth", "JWT", "OAuth", "sessions"),
        ("websocket", "WebSocket", "Socket.io", "real-time", "WS"),
    ], "framework", "javascript", "backend"),

    ("backend", "patterns", [
        ("microservices", "Microservices"), ("cqrs", "CQRS"), ("event-sourcing", "Event Sourcing"),
        ("saga", "Saga"), ("bff", "Backend for Frontend"), ("circuit-breaker", "Circuit Breaker"),
        ("strangler-fig", "Strangler Fig"), ("api-gateway", "API Gateway"),
        ("throttling", "Throttling"), ("retry", "Retry"), ("bulkhead", "Bulkhead"),
        ("sidecar", "Sidecar"), ("ambassador", "Ambassador"), ("repository", "Repository"),
        ("unit-of-work", "Unit of Work"), ("factory", "Factory"), ("strategy", "Strategy"),
        ("observer", "Observer"), ("decorator", "Decorator"), ("adapter", "Adapter"),
    ], [
        ("intro", "Introduction", "understanding the pattern", "core concepts", "when to use"),
        ("implementation", "Implementation", "practical implementation", "code examples", "best practices"),
        ("testing", "Testing", "testing the pattern", "integration", "verification"),
        ("scaling", "Scaling", "scaling considerations", "performance", "production"),
        ("migration", "Migration", "adopting the pattern", "migration path", "refactoring"),
    ], "concept", "", "architecture"),
]

# =======================================================
# FRONTEND SKILLS (frameworks, CSS, build-tools, meta-fw, state)
# =======================================================

FRONTEND_GROUPS = [
    ("frontend", "fw", [
        "react", "vue", "angular", "svelte", "solid",
        "preact", "lit", "alpine", "stimulus", "ember",
        "backbone", "mithril", "aurelia", "marko", "riot", "inferno",
    ], [
        ("components", "Components", "building components", "UI elements", "reusable"),
        ("state-management", "State Management", "state handling", "data flow", "reactive"),
        ("routing", "Routing", "client routing", "navigation", "URL"),
        ("forms", "Forms", "form handling", "validation", "submission"),
        ("styling", "Styling", "component styling", "CSS modules", "scoped styles"),
        ("testing", "Testing", "component testing", "unit tests", "integration"),
        ("performance", "Performance", "optimization", "rendering", "bundles"),
        ("ssr", "SSR", "server rendering", "hydration", "isomorphic"),
        ("animations", "Animations", "UI animations", "transitions", "motion"),
        ("accessibility", "Accessibility", "a11y", "ARIA", "keyboard"),
    ], "framework", "typescript", "frontend"),

    ("frontend", "css", [
        ("tailwind", "Tailwind CSS"), ("bootstrap", "Bootstrap"), ("bulma", "Bulma"),
        ("foundation", "Foundation"), ("material-ui", "MUI"), ("chakra-ui", "Chakra UI"),
        ("radix-ui", "Radix UI"), ("ant-design", "Ant Design"), ("daisyui", "daisyUI"),
        ("pico", "Pico CSS"), ("purecss", "Pure.css"), ("semantic-ui", "Semantic UI"),
        ("spectre", "Spectre.css"), ("water", "Water.css"), ("milligram", "Milligram"),
    ], [
        ("grid", "Grid", "layout grids", "responsive", "CSS Grid"),
        ("forms", "Forms", "form styling", "inputs", "layouts"),
        ("typography", "Typography", "text styling", "fonts", "readability"),
        ("responsive", "Responsive", "mobile-first", "breakpoints", "responsive"),
        ("theming", "Theming", "custom themes", "tokens", "colors"),
        ("components", "Components", "UI components", "widgets", "elements"),
        ("dark-mode", "Dark Mode", "dark theme", "color modes", "switching"),
        ("utilities", "Utilities", "utility classes", "helpers", "patterns"),
    ], "framework", "css", "css"),

    ("frontend", "build", [
        ("webpack", "Webpack"), ("vite", "Vite"), ("esbuild", "esbuild"),
        ("rollup", "Rollup"), ("parcel", "Parcel"), ("turbopack", "Turbopack"),
        ("swc", "SWC"), ("babel", "Babel"), ("postcss", "PostCSS"),
        ("sass", "Sass"), ("less", "Less"), ("stylus", "Stylus"),
        ("tsc", "TypeScript"), ("oxlint", "Oxlint"), ("prettier", "Prettier"), ("eslint", "ESLint"),
    ], [
        ("setup", "Setup", "initial setup", "config", "first build"),
        ("config", "Config", "configuration", "options", "customization"),
        ("plugins", "Plugins", "plugins", "extensions", "addons"),
        ("optimization", "Optimization", "build optimization", "minification", "performance"),
        ("bundling", "Bundling", "code bundling", "chunking", "tree shaking"),
        ("code-splitting", "Code Splitting", "lazy loading", "dynamic imports", "chunks"),
        ("source-maps", "Source Maps", "debugging", "source maps", "error tracing"),
        ("hmr", "HMR", "hot reload", "live updates", "dev experience"),
    ], "framework", "javascript", "build-tool"),

    ("frontend", "meta", [
        ("nextjs", "Next.js"), ("nuxt", "Nuxt"), ("remix", "Remix"),
        ("gatsby", "Gatsby"), ("astro", "Astro"), ("sveltekit", "SvelteKit"),
        ("solidstart", "SolidStart"), ("qwik", "Qwik"),
        ("eleventy", "Eleventy"), ("hugo", "Hugo"), ("jekyll", "Jekyll"),
        ("docusaurus", "Docusaurus"), ("vitepress", "VitePress"), ("storybook", "Storybook"),
    ], [
        ("ssr", "SSR", "server rendering", "dynamic", "SEO"),
        ("ssg", "SSG", "static generation", "pre-rendering", "build-time"),
        ("isr", "ISR", "incremental", "hybrid", "on-demand"),
        ("routing", "Routing", "file-based routing", "navigation", "config"),
        ("data-fetching", "Data Fetching", "data loading", "API", "server data"),
        ("api-routes", "API Routes", "API endpoints", "serverless", "backend"),
        ("middleware", "Middleware", "request middleware", "edge", "interceptors"),
        ("deployment", "Deployment", "production", "hosting", "CI/CD"),
    ], "framework", "typescript", "meta-framework"),

    ("frontend", "state", [
        ("redux", "Redux"), ("zustand", "Zustand"), ("pinia", "Pinia"),
        ("valtio", "Valtio"), ("jotai", "Jotai"), ("recoil", "Recoil"),
        ("mobx", "MobX"), ("effector", "Effector"), ("xstate", "XState"),
        ("ngrx", "NgRx"), ("vuex", "Vuex"), ("akita", "Akita"),
    ], [
        ("store", "Store", "state store", "data store", "central state"),
        ("actions", "Actions", "actions", "mutations", "events"),
        ("selectors", "Selectors", "derived data", "memoization", "queries"),
        ("middleware", "Middleware", "side effects", "async", "interceptors"),
        ("devtools", "DevTools", "debugging", "inspection", "time travel"),
        ("persistence", "Persistence", "state persistence", "storage", "rehydration"),
        ("testing", "Testing", "state testing", "store tests", "integration"),
        ("optimization", "Optimization", "performance", "rendering", "memoization"),
    ], "framework", "typescript", "state-management"),
]

# =======================================================
# DEVOPS SKILLS (CI/CD, container, K8s, IaC, monitoring, cloud)
# =======================================================

DEVOPS_GROUPS = [
    ("devops", "ci", [
        ("github-actions", "GitHub Actions"), ("gitlab-ci", "GitLab CI"), ("jenkins", "Jenkins"),
        ("circleci", "CircleCI"), ("travis-ci", "Travis CI"), ("azure-pipelines", "Azure Pipelines"),
        ("teamcity", "TeamCity"), ("bamboo", "Bamboo"), ("drone", "Drone CI"),
        ("concourse", "Concourse"), ("woodpecker", "Woodpecker"), ("dagger", "Dagger"),
        ("earthly", "Earthly"), ("buildkite", "Buildkite"),
    ], [
        ("setup", "Setup", "pipeline setup", "initial config", "installation"),
        ("pipeline", "Pipeline", "pipeline creation", "build stages", "workflow"),
        ("testing", "Testing", "automated tests", "test stages", "quality gates"),
        ("deployment", "Deployment", "auto-deploy", "release", "delivery"),
        ("caching", "Caching", "dependency caching", "build cache", "speed"),
        ("secrets", "Secrets", "secret management", "env vars", "credentials"),
        ("monitoring", "Monitoring", "monitoring", "build tracking", "alerts"),
        ("security", "Security", "security scanning", "vulns", "compliance"),
    ], "tool", "", "ci-cd"),

    ("devops", "container", [
        ("docker", "Docker"), ("podman", "Podman"), ("containerd", "containerd"),
        ("nerdctl", "nerdctl"), ("buildah", "Buildah"), ("skopeo", "Skopeo"),
        ("kaniko", "Kaniko"), ("docker-compose", "Docker Compose"),
        ("lxc", "LXC"), ("singularity", "Singularity"),
    ], [
        ("setup", "Setup", "installation", "config", "first use"),
        ("images", "Images", "building images", "Dockerfiles", "management"),
        ("networking", "Networking", "container networks", "config", "DNS"),
        ("volumes", "Volumes", "data volumes", "persistent storage", "mounts"),
        ("compose", "Compose", "multi-container", "services", "orchestration"),
        ("security", "Security", "container security", "scanning", "runtime security"),
        ("optimization", "Optimization", "image optimization", "size", "multi-stage"),
        ("registry", "Registry", "image registry", "push/pull", "private"),
    ], "tool", "", "container"),

    ("devops", "k8s", [
        ("kubernetes", "Kubernetes"), ("k3s", "K3s"), ("k0s", "K0s"),
        ("microk8s", "MicroK8s"), ("kind", "Kind"), ("minikube", "Minikube"),
        ("openshift", "OpenShift"), ("rancher", "Rancher"),
        ("eks", "Amazon EKS"), ("aks", "Azure AKS"), ("gke", "Google GKE"),
    ], [
        ("deployment", "Deployment", "apps deployment", "workloads", "rolling updates"),
        ("service", "Service", "services", "networking", "load balancing"),
        ("configmap", "ConfigMap", "config management", "env", "settings"),
        ("secrets", "Secrets", "secret management", "sensitive data", "encryption"),
        ("ingress", "Ingress", "ingress controller", "traffic routing", "TLS"),
        ("helm", "Helm", "package management", "charts", "releases"),
        ("monitoring", "Monitoring", "monitoring", "metrics", "alerting"),
        ("storage", "Storage", "persistent storage", "volumes", "storage classes"),
        ("rbac", "RBAC", "access control", "roles", "permissions"),
        ("autoscaling", "Autoscaling", "HPA", "scaling", "resources"),
    ], "tool", "", "kubernetes"),

    ("devops", "iac", [
        ("terraform", "Terraform"), ("pulumi", "Pulumi"), ("ansible", "Ansible"),
        ("chef", "Chef"), ("puppet", "Puppet"), ("saltstack", "SaltStack"),
        ("cloudformation", "CloudFormation"), ("cdk", "AWS CDK"),
        ("crossplane", "Crossplane"), ("opentofu", "OpenTofu"),
        ("packer", "Packer"), ("vagrant", "Vagrant"),
    ], [
        ("setup", "Setup", "installation", "init", "first use"),
        ("modules", "Modules", "modules", "reusable", "abstraction"),
        ("state", "State", "state management", "remote state", "locking"),
        ("provisioning", "Provisioning", "provisioning", "infra setup", "deploy"),
        ("networking", "Networking", "network infra", "VPC", "subnets"),
        ("security", "Security", "security groups", "IAM", "encryption"),
        ("testing", "Testing", "infra testing", "compliance", "validation"),
        ("cicd", "CI/CD", "pipeline integration", "automation", "GitOps"),
    ], "tool", "", "iac"),

    ("devops", "monitoring", [
        ("prometheus", "Prometheus"), ("grafana", "Grafana"), ("datadog", "Datadog"),
        ("newrelic", "New Relic"), ("dynatrace", "Dynatrace"),
        ("elastic", "Elastic Stack"), ("loki", "Loki"), ("tempo", "Tempo"),
        ("jaeger", "Jaeger"), ("zipkin", "Zipkin"),
        ("opentelemetry", "OpenTelemetry"), ("signoz", "SigNoz"),
        ("thanos", "Thanos"), ("victoria-metrics", "VictoriaMetrics"),
    ], [
        ("setup", "Setup", "installation", "config", "first use"),
        ("metrics", "Metrics", "collecting metrics", "data sources", "types"),
        ("alerts", "Alerts", "alerting rules", "notifications", "Alertmanager"),
        ("dashboards", "Dashboards", "dashboards", "visualization", "panels"),
        ("logging", "Logging", "log collection", "parsing", "analysis"),
        ("tracing", "Tracing", "distributed tracing", "spans", "analysis"),
        ("scraping", "Scraping", "target discovery", "scrape", "service discovery"),
        ("storage", "Storage", "data retention", "storage config", "archival"),
    ], "tool", "", "monitoring"),

    ("devops", "cloud", [
        ("aws", "AWS"), ("azure", "Azure"), ("gcp", "GCP"),
        ("digitalocean", "DigitalOcean"), ("linode", "Linode"), ("vultr", "Vultr"),
        ("heroku", "Heroku"), ("railway", "Railway"), ("render", "Render"),
        ("flyio", "Fly.io"), ("netlify", "Netlify"), ("vercel", "Vercel"),
        ("cloudflare", "Cloudflare"), ("fastly", "Fastly"), ("akamai", "Akamai"),
    ], [
        ("compute", "Compute", "VM/compute", "instances", "containers"),
        ("storage", "Storage", "object storage", "block storage", "file storage"),
        ("database", "Database", "managed databases", "RDS", "cloud DB"),
        ("networking", "Networking", "VPC", "networking", "CDN"),
        ("serverless", "Serverless", "functions", "Lambda", "FaaS"),
        ("monitoring", "Monitoring", "monitoring", "metrics", "logging"),
        ("security", "Security", "cloud security", "IAM", "compliance"),
        ("cost", "Cost", "cost optimization", "budgeting", "reserved"),
    ], "platform", "", "cloud"),
]

# =======================================================
# DATABASE SKILLS
# =======================================================

DATABASE_GROUPS = [
    ("database", "sql", [
        ("postgresql", "PostgreSQL"), ("mysql", "MySQL"), ("mariadb", "MariaDB"),
        ("sqlite", "SQLite"), ("sqlserver", "SQL Server"), ("oracle", "Oracle"),
        ("cockroachdb", "CockroachDB"), ("yugabyte", "YugabyteDB"), ("cratedb", "CrateDB"),
    ], [
        ("setup", "Setup", "installation", "config", "connection"),
        ("querying", "Querying", "SQL queries", "CRUD", "joins"),
        ("schema", "Schema Design", "schema", "modeling", "structure"),
        ("indexing", "Indexing", "indexes", "performance", "query speed"),
        ("replication", "Replication", "replication", "HA", "read replicas"),
        ("backup", "Backup", "backup strategies", "PITR", "recovery"),
        ("migration", "Migration", "schema migrations", "versioning", "change mgmt"),
        ("security", "Security", "access control", "encryption", "audit"),
        ("optimization", "Optimization", "query tuning", "performance", "config"),
        ("monitoring", "Monitoring", "monitoring", "metrics", "alerting"),
    ], "framework", "sql", "sql"),

    ("database", "nosql", [
        ("mongodb", "MongoDB"), ("couchdb", "CouchDB"), ("firestore", "Firestore"),
        ("dynamodb", "DynamoDB"), ("cassandra", "Cassandra"), ("scylla", "ScyllaDB"),
        ("hbase", "HBase"), ("neo4j", "Neo4j"),
        ("arangodb", "ArangoDB"), ("surreal", "SurrealDB"),
    ], [
        ("setup", "Setup", "installation", "config", "connection"),
        ("querying", "Querying", "queries", "CRUD", "operations"),
        ("schema", "Schema Design", "schema design", "modeling", "structure"),
        ("indexing", "Indexing", "indexes", "performance", "speed"),
        ("replication", "Replication", "replication", "HA", "scaling"),
        ("backup", "Backup", "backup", "recovery", "disaster"),
        ("security", "Security", "security", "access control", "encryption"),
        ("aggregation", "Aggregation", "aggregation pipelines", "analytics", "reporting"),
        ("optimization", "Optimization", "performance", "tuning", "optimization"),
        ("monitoring", "Monitoring", "monitoring", "metrics", "alerting"),
    ], "framework", "javascript", "nosql"),

    ("database", "cache", [
        ("redis", "Redis"), ("memcached", "Memcached"), ("hazelcast", "Hazelcast"),
        ("ignite", "Apache Ignite"), ("couchbase", "Couchbase"), ("ehcache", "Ehcache"),
        ("varnish", "Varnish"), ("nginx-cache", "Nginx Cache"),
    ], [
        ("setup", "Setup", "installation", "config", "first use"),
        ("caching", "Caching", "caching strategies", "TTL", "invalidation"),
        ("clustering", "Clustering", "cluster setup", "HA", "sharding"),
        ("persistence", "Persistence", "persistence", "RDB/AOF", "durability"),
        ("security", "Security", "security", "auth", "encryption"),
        ("monitoring", "Monitoring", "monitoring", "metrics", "performance"),
        ("pub-sub", "Pub/Sub", "publish/subscribe", "messaging", "channels"),
        ("optimization", "Optimization", "performance tuning", "memory", "throughput"),
    ], "tool", "", "caching"),

    ("database", "timeseries", [
        ("timescaledb", "TimescaleDB"), ("influxdb", "InfluxDB"), ("clickhouse", "ClickHouse"),
        ("questdb", "QuestDB"), ("druid", "Apache Druid"), ("pinot", "Apache Pinot"),
        ("prometheus-tsdb", "Prometheus TSDB"), ("victoria-metrics", "VictoriaMetrics"),
    ], [
        ("setup", "Setup", "installation", "config", "first ingest"),
        ("ingestion", "Ingestion", "data ingestion", "insert", "streaming"),
        ("querying", "Querying", "time-series queries", "aggregations", "downsampling"),
        ("retention", "Retention", "data retention", "policies", "tiered storage"),
        ("compression", "Compression", "compression", "encoding", "storage efficiency"),
        ("clustering", "Clustering", "clustering", "HA", "scaling"),
        ("monitoring", "Monitoring", "monitoring", "metrics", "performance"),
        ("visualization", "Visualization", "charting", "grafana", "dashboards"),
    ], "tool", "", "time-series"),

    ("database", "search", [
        ("elasticsearch", "Elasticsearch"), ("opensearch", "OpenSearch"), ("solr", "Solr"),
        ("meilisearch", "Meilisearch"), ("typesense", "Typesense"), ("algolia", "Algolia"),
        ("sphinx", "Sphinx"), ("weaviate", "Weaviate"),
    ], [
        ("setup", "Setup", "installation", "config", "first index"),
        ("indexing", "Indexing", "document indexing", "mappings", "analyzers"),
        ("searching", "Searching", "full-text search", "queries", "filtering"),
        ("aggregations", "Aggregations", "bucket aggs", "metrics", "analytics"),
        ("mapping", "Mapping", "field mapping", "types", "analysis"),
        ("scoring", "Scoring", "relevance scoring", "boosting", "ranking"),
        ("clustering", "Clustering", "cluster setup", "nodes", "sharding"),
        ("monitoring", "Monitoring", "cluster monitoring", "metrics", "performance"),
    ], "tool", "", "search-engine"),

    ("database", "graph", [
        ("neo4j", "Neo4j"), ("janusgraph", "JanusGraph"), ("dgraph", "Dgraph"),
        ("nebula", "Nebula Graph"), ("amazon-neptune", "Amazon Neptune"),
        ("arangodb-graph", "ArangoDB Graph"), ("orientdb", "OrientDB"),
    ], [
        ("setup", "Setup", "installation", "config", "first query"),
        ("querying", "Querying", "Cypher/Gremlin", "graph queries", "traversal"),
        ("modeling", "Modeling", "graph modeling", "nodes", "relationships"),
        ("indexing", "Indexing", "indexes", "performance", "lookups"),
        ("clustering", "Clustering", "clustering", "HA", "scaling"),
        ("visualization", "Visualization", "graph viz", "exploration", "analysis"),
        ("performance", "Performance", "optimization", "query perf", "tuning"),
        ("security", "Security", "security", "access control", "encryption"),
    ], "tool", "", "graph-database"),
]

# =======================================================
# DATA / QA / SECURITY SKILLS
# =======================================================

DATA_GROUPS = [
    ("data", "eng", [
        ("apache-spark", "Apache Spark"), ("apache-flink", "Apache Flink"), ("apache-beam", "Apache Beam"),
        ("hadoop", "Hadoop"), ("presto", "Presto"), ("trino", "Trino"),
        ("dbt", "dbt"), ("airflow", "Airflow"), ("dagster", "Dagster"),
        ("prefect", "Prefect"), ("kafka", "Kafka"), ("pulsar", "Pulsar"),
        ("nifi", "NiFi"), ("kinesis", "Kinesis"),
    ], [
        ("setup", "Setup", "installation", "config", "first job"),
        ("etl", "ETL", "extract-transform-load", "pipelines", "processing"),
        ("streaming", "Streaming", "real-time", "stream processing", "events"),
        ("batch", "Batch", "batch processing", "scheduled", "large-scale"),
        ("sql", "SQL", "SQL queries", "analytics", "exploration"),
        ("optimization", "Optimization", "performance", "tuning", "scaling"),
        ("monitoring", "Monitoring", "monitoring", "metrics", "alerts"),
        ("integration", "Integration", "connectors", "sources", "sinks"),
    ], "tool", "", "data-engineering"),

    ("data", "analysis", [
        ("pandas", "Pandas"), ("polars", "Polars"), ("numpy", "NumPy"),
        ("scipy", "SciPy"), ("jupyter", "Jupyter"), ("matplotlib", "Matplotlib"),
        ("seaborn", "Seaborn"), ("plotly", "Plotly"), ("bokeh", "Bokeh"),
        ("altair", "Altair"),
    ], [
        ("dataframe", "DataFrame", "data manipulation", "tabular", "wrangling"),
        ("visualization", "Visualization", "charting", "plotting", "graphical analysis"),
        ("cleaning", "Cleaning", "data cleaning", "preprocessing", "quality"),
        ("analysis", "Analysis", "data analysis", "statistics", "exploration"),
        ("transformation", "Transformation", "transform", "feature engineering", "pipeline"),
        ("integration", "Integration", "data sources", "import/export", "connectors"),
        ("performance", "Performance", "optimization", "large data", "efficiency"),
        ("deployment", "Deployment", "app deployment", "sharing", "production"),
    ], "framework", "python", "data-science"),

    ("data", "apps", [
        ("streamlit", "Streamlit"), ("gradio", "Gradio"), ("dash", "Dash"),
        ("panel", "Panel"), ("shiny", "Shiny"), ("taipy", "Taipy"),
        ("nicegui", "NiceGUI"), ("voila", "Voila"),
    ], [
        ("setup", "Setup", "installation", "config", "first app"),
        ("layout", "Layout", "app layout", "components", "UI"),
        ("widgets", "Widgets", "input widgets", "controls", "interaction"),
        ("charts", "Charts", "charts", "visualization", "plotting"),
        ("data", "Data", "data binding", "state", "updates"),
        ("deployment", "Deployment", "deploy", "hosting", "sharing"),
        ("theming", "Theming", "themes", "styling", "customization"),
        ("performance", "Performance", "performance", "caching", "optimization"),
    ], "framework", "python", "data-apps"),
]

QA_GROUPS = [
    ("qa", "fw", [
        ("pytest", "pytest"), ("junit", "JUnit"), ("testng", "TestNG"),
        ("mocha", "Mocha"), ("jest", "Jest"), ("vitest", "Vitest"),
        ("rspec", "RSpec"), ("minitest", "Minitest"), ("phpunit", "PHPUnit"),
        ("gotest", "Go Test"), ("cargo-test", "Cargo Test"),
        ("exunit", "ExUnit"), ("swift-test", "Swift Testing"),
    ], [
        ("setup", "Setup", "installation", "config", "first test"),
        ("unit-tests", "Unit Tests", "unit testing", "component", "isolated"),
        ("fixtures", "Fixtures", "test fixtures", "setup/teardown", "data"),
        ("mocking", "Mocking", "mocks", "stubs", "fakes"),
        ("parameterization", "Parameterization", "parametrized tests", "data-driven", "matrix"),
        ("coverage", "Coverage", "code coverage", "reports", "metrics"),
        ("integration", "Integration", "integration tests", "service tests", "API"),
        ("ci", "CI", "CI integration", "automation", "reporting"),
    ], "framework", "bash", "testing"),

    ("qa", "e2e", [
        ("cypress", "Cypress"), ("playwright", "Playwright"), ("selenium", "Selenium"),
        ("puppeteer", "Puppeteer"), ("detox", "Detox"), ("appium", "Appium"),
        ("webdriverio", "WebdriverIO"), ("nightwatch", "Nightwatch"),
        ("testcafe", "TestCafe"), ("katalon", "Katalon"),
    ], [
        ("setup", "Setup", "installation", "config", "first test"),
        ("selectors", "Selectors", "element selectors", "locators", "DOM"),
        ("actions", "Actions", "user actions", "clicks", "input"),
        ("assertions", "Assertions", "assertions", "verifications", "expects"),
        ("reporting", "Reporting", "reports", "screenshots", "videos"),
        ("parallel", "Parallel", "parallel execution", "sharding", "concurrent"),
        ("ci", "CI", "CI integration", "headless", "pipeline"),
        ("mobile", "Mobile", "mobile testing", "emulation", "devices"),
    ], "framework", "javascript", "e2e"),

    ("qa", "perf", [
        ("k6", "k6"), ("jmeter", "JMeter"), ("gatling", "Gatling"),
        ("locust", "Locust"), ("artillery", "Artillery"), ("vegeta", "Vegeta"),
        ("wrk", "wrk"), ("ab", "Apache Bench"), ("siege", "Siege"),
        ("hey", "hey"), ("tsung", "Tsung"),
    ], [
        ("setup", "Setup", "installation", "config", "first run"),
        ("scenarios", "Scenarios", "test scenarios", "user flows", "modeling"),
        ("metrics", "Metrics", "performance metrics", "latency", "throughput"),
        ("thresholds", "Thresholds", "pass/fail", "SLOs", "thresholds"),
        ("reports", "Reports", "report generation", "analysis", "dashboards"),
        ("distributed", "Distributed", "distributed load", "multi-node", "scaling"),
        ("ci", "CI", "CI integration", "automation", "pipeline"),
        ("spike", "Spike", "spike tests", "stress", "soak"),
    ], "tool", "", "performance-testing"),
]

SECURITY_GROUPS = [
    ("security", "standards", [
        ("owasp", "OWASP"), ("nist", "NIST"), ("soc2", "SOC 2"),
        ("iso27001", "ISO 27001"), ("hipaa", "HIPAA"), ("gdpr", "GDPR"),
        ("pcidss", "PCI DSS"), ("pki", "PKI"), ("x509", "X.509"),
        ("oauth2", "OAuth 2.0"), ("saml", "SAML"), ("openid", "OpenID Connect"),
        ("ldap", "LDAP"), ("kerberos", "Kerberos"), ("tls", "TLS/SSL"),
    ], [
        ("basics", "Basics", "fundamentals", "core", "intro"),
        ("implementation", "Implementation", "implementation", "deployment", "integration"),
        ("audit", "Audit", "security audit", "compliance", "assessment"),
        ("best-practices", "Best Practices", "best practices", "guidelines", "standards"),
        ("testing", "Testing", "security testing", "scanning", "pentest"),
        ("tools", "Tools", "security tools", "utilities", "automation"),
        ("monitoring", "Monitoring", "security monitoring", "detection", "SIEM"),
        ("incident-response", "Incident Response", "incident response", "forensics", "remediation"),
    ], "concept", "", "security"),

    ("security", "tools", [
        ("nmap", "Nmap"), ("wireshark", "Wireshark"), ("burpsuite", "Burp Suite"),
        ("metasploit", "Metasploit"), ("nessus", "Nessus"), ("openvas", "OpenVAS"),
        ("trivy", "Trivy"), ("snyk", "Snyk"), ("sonarqube", "SonarQube"),
        ("zap", "ZAP"), ("hashcat", "Hashcat"), ("john", "John the Ripper"),
        ("hydra", "Hydra"), ("aircrack", "Aircrack-ng"), ("sqlmap", "SQLmap"),
    ], [
        ("setup", "Setup", "installation", "config", "first use"),
        ("scanning", "Scanning", "security scanning", "recon", "enumeration"),
        ("analysis", "Analysis", "analysis", "interpretation", "reporting"),
        ("exploitation", "Exploitation", "exploitation", "testing", "PoC"),
        ("reporting", "Reporting", "reports", "findings", "recommendations"),
        ("automation", "Automation", "automation", "CI/CD", "scripting"),
        ("remediation", "Remediation", "fixing vulns", "patching", "hardening"),
        ("compliance", "Compliance", "compliance", "policy", "auditing"),
    ], "tool", "", "security-tool"),
]

# =======================================================
# MOBILE / DESIGN / GAMEDEV / BLOCKCHAIN SKILLS
# =======================================================

MOBILE_GROUPS = [
    ("mobile", "fw", [
        ("react-native", "React Native"), ("flutter", "Flutter"), ("kotlin-multiplatform", "Kotlin Multiplatform"),
        ("xamarin", "Xamarin"), ("ionic", "Ionic"), ("capacitor", "Capacitor"),
        ("cordova", "Cordova"), ("nativescript", "NativeScript"),
        ("swift-ios", "Swift iOS"), ("kotlin-android", "Kotlin Android"),
    ], [
        ("setup", "Setup", "setup", "project init", "first build"),
        ("ui", "UI", "UI components", "layouts", "screens"),
        ("navigation", "Navigation", "navigation", "routing", "deep links"),
        ("state", "State", "state management", "data flow", "app state"),
        ("networking", "Networking", "API calls", "HTTP", "fetching"),
        ("storage", "Storage", "local storage", "persistence", "database"),
        ("push", "Push", "push notifications", "FCM", "APNs"),
        ("deployment", "Deployment", "app store", "release", "signing"),
        ("testing", "Testing", "testing", "unit tests", "UI tests"),
        ("performance", "Performance", "optimization", "battery", "memory"),
    ], "framework", "typescript", "mobile"),
]

DESIGN_GROUPS = [
    ("design", "tools", [
        ("figma", "Figma"), ("sketch", "Sketch"), ("adobe-xd", "Adobe XD"),
        ("framer", "Framer"), ("penpot", "Penpot"), ("invision", "InVision"),
        ("zeplin", "Zeplin"), ("zeroheight", "Zeroheight"),
        ("spec", "Spec"), ("backlight", "Backlight"),
    ], [
        ("setup", "Setup", "workspace", "project", "first design"),
        ("components", "Components", "components", "UI kits", "reusable"),
        ("prototyping", "Prototyping", "prototypes", "wireframes", "flows"),
        ("design-system", "Design Systems", "tokens", "guides", "libraries"),
        ("collaboration", "Collaboration", "collaboration", "review", "handoff"),
        ("plugins", "Plugins", "plugins", "extensions", "automation"),
        ("export", "Export", "assets", "code gen", "delivery"),
        ("versioning", "Versioning", "version control", "history", "branches"),
    ], "platform", "", "design"),

    ("design", "ux", [
        ("user-research", "User Research"), ("usability-testing", "Usability Testing"),
        ("a-b-testing", "A/B Testing"), ("heatmaps", "Heatmaps"),
        ("wireframing", "Wireframing"), ("persona", "Personas"),
        ("journey-mapping", "Journey Mapping"), ("information-architecture", "Information Architecture"),
    ], [
        ("basics", "Basics", "fundamentals", "methods", "intro"),
        ("planning", "Planning", "study planning", "recruiting", "scheduling"),
        ("execution", "Execution", "running sessions", "data collection", "moderation"),
        ("analysis", "Analysis", "data analysis", "insights", "findings"),
        ("reporting", "Reporting", "reports", "presentations", "recommendations"),
        ("tools", "Tools", "tools", "software", "templates"),
    ], "concept", "", "ux-research"),
]

GAMEDEV_GROUPS = [
    ("gamedev", "engines", [
        ("unity", "Unity"), ("unreal", "Unreal Engine"), ("godot", "Godot"),
        ("bevy", "Bevy"), ("phaser", "Phaser"), ("cocos", "Cocos Creator"),
        ("defold", "Defold"), ("rpgmaker", "RPG Maker"),
        ("game-maker", "GameMaker"), ("construct", "Construct"),
    ], [
        ("setup", "Setup", "engine setup", "project", "first scene"),
        ("scripting", "Scripting", "game logic", "behaviors", "code"),
        ("physics", "Physics", "physics", "collision", "rigid bodies"),
        ("animation", "Animation", "animation", "sprites", "rigging"),
        ("audio", "Audio", "audio", "SFX", "music"),
        ("ui", "UI", "game UI", "HUD", "menus"),
        ("rendering", "Rendering", "graphics", "shaders", "lighting"),
        ("optimization", "Optimization", "performance", "profiling", "optimization"),
        ("multiplayer", "Multiplayer", "networking", "multiplayer", "netcode"),
        ("publishing", "Publishing", "publishing", "store", "distribution"),
    ], "framework", "csharp", "game-engine"),

    ("gamedev", "design", [
        ("level-design", "Level Design"), ("game-balance", "Game Balance"),
        ("narrative", "Narrative Design"), ("procedural-generation", "Procedural Generation"),
        ("game-economy", "Game Economy"), ("combat-design", "Combat Design"),
        ("puzzle-design", "Puzzle Design"), ("open-world", "Open World Design"),
    ], [
        ("basics", "Basics", "fundamentals", "principles", "intro"),
        ("planning", "Planning", "planning", "documentation", "design doc"),
        ("implementation", "Implementation", "implementation", "iteration", "testing"),
        ("balancing", "Balancing", "balancing", "tuning", "difficulty"),
        ("player-feedback", "Feedback", "player feedback", "playtesting", "iteration"),
        ("tools", "Tools", "tools", "editors", "workflows"),
    ], "concept", "", "game-design"),
]

BLOCKCHAIN_GROUPS = [
    ("blockchain", "chains", [
        ("ethereum", "Ethereum"), ("solana", "Solana"), ("polygon", "Polygon"),
        ("avalanche", "Avalanche"), ("cosmos", "Cosmos"), ("polkadot", "Polkadot"),
        ("near", "NEAR"), ("cardano", "Cardano"), ("tezos", "Tezos"),
        ("algorand", "Algorand"), ("stellar", "Stellar"), ("hedera", "Hedera"),
        ("fantom", "Fantom"), ("arbitrum", "Arbitrum"), ("optimism", "Optimism"),
        ("zksync", "zkSync"), ("starknet", "StarkNet"), ("base", "Base"),
    ], [
        ("setup", "Setup", "node setup", "wallet", "dev env"),
        ("smart-contracts", "Smart Contracts", "contracts", "Solidity", "deployment"),
        ("dapps", "DApps", "decentralized apps", "web3", "frontend"),
        ("defi", "DeFi", "DeFi", "lending", "trading"),
        ("nft", "NFT", "tokens", "marketplaces", "collections"),
        ("tokens", "Tokens", "token standards", "ERC-20", "ERC-721"),
        ("staking", "Staking", "staking", "rewards", "validators"),
        ("bridge", "Bridge", "cross-chain", "bridges", "interop"),
    ], "framework", "solidity", "blockchain"),
]

# =======================================================
# IOT / DESKTOP / NETWORKING / SCIENTIFIC / PAYMENTS
# =======================================================

IOT_GROUPS = [
    ("iot", "boards", [
        ("arduino", "Arduino"), ("esp32", "ESP32"), ("esp8266", "ESP8266"),
        ("raspberry-pi", "Raspberry Pi"), ("stm32", "STM32"), ("nrf52", "nRF52"),
        ("teensy", "Teensy"), ("mbed", "Mbed OS"),
        ("micropython", "MicroPython"), ("circuitpython", "CircuitPython"),
    ], [
        ("setup", "Setup", "board setup", "IDE", "first blink"),
        ("gpio", "GPIO", "digital I/O", "pin control", "interfacing"),
        ("pwm", "PWM", "PWM signals", "LED", "motor"),
        ("adc", "ADC", "analog input", "sensors", "measurement"),
        ("communication", "Comm", "I2C", "SPI", "UART"),
        ("wifi", "WiFi", "wireless", "network", "HTTP"),
        ("ble", "BLE", "Bluetooth", "beacons", "peripheral"),
        ("sensors", "Sensors", "sensor integration", "temperature", "motion"),
        ("actuators", "Actuators", "motors", "relays", "servos"),
        ("power", "Power", "power management", "low power", "battery"),
    ], "framework", "cpp", "iot"),

    ("iot", "platforms", [
        ("platformio", "PlatformIO"), ("esphome", "ESPHome"), ("tasmota", "Tasmota"),
        ("home-assistant", "Home Assistant"), ("openhab", "openHAB"),
        ("node-red", "Node-RED"), ("thingsboard", "ThingsBoard"),
        ("aws-iot", "AWS IoT"), ("azure-iot", "Azure IoT"), ("google-iot", "Google IoT"),
    ], [
        ("setup", "Setup", "setup", "config", "first device"),
        ("devices", "Devices", "device management", "provisioning", "registry"),
        ("telemetry", "Telemetry", "data collection", "sensors", "streaming"),
        ("commands", "Commands", "device commands", "control", "actuation"),
        ("dashboards", "Dashboards", "dashboards", "visualization", "monitoring"),
        ("automation", "Automation", "automation", "rules", "triggers"),
        ("security", "Security", "device security", "auth", "encryption"),
        ("integration", "Integration", "integrations", "APIs", "connectors"),
    ], "platform", "", "iot-platform"),
]

DESKTOP_GROUPS = [
    ("desktop", "fw", [
        ("electron", "Electron"), ("tauri", "Tauri"), ("flutter-desktop", "Flutter Desktop"),
        ("qt", "Qt"), ("gtk", "GTK"), ("wxwidgets", "wxWidgets"),
        ("javafx", "JavaFX"), ("swiftui-mac", "SwiftUI Mac"),
        ("winui", "WinUI"), ("avalonia", "Avalonia"),
        ("pyqt", "PyQt"), ("tkinter", "Tkinter"), ("wpf", "WPF"),
    ], [
        ("setup", "Setup", "SDK setup", "project", "first window"),
        ("ui", "UI", "UI components", "widgets", "layout"),
        ("window", "Window", "windows", "dialogs", "menus"),
        ("events", "Events", "event handling", "signals", "callbacks"),
        ("threading", "Threading", "multithreading", "async", "background"),
        ("packaging", "Packaging", "app packaging", "installers", "distribution"),
        ("native", "Native", "native APIs", "system", "file system"),
        ("styling", "Styling", "styling", "themes", "customization"),
    ], "framework", "javascript", "desktop"),
]

NETWORKING_GROUPS = [
    ("networking", "protocols", [
        ("tcp-ip", "TCP/IP"), ("dns", "DNS"), ("dhcp", "DHCP"),
        ("http", "HTTP"), ("tls-ssl", "TLS/SSL"), ("bgp", "BGP"),
        ("ospf", "OSPF"), ("vpn", "VPN"), ("vlan", "VLAN"),
        ("nat", "NAT"), ("mpls", "MPLS"), ("sd-wan", "SD-WAN"),
    ], [
        ("basics", "Basics", "fundamentals", "core", "intro"),
        ("configuration", "Config", "setup", "config", "deployment"),
        ("troubleshooting", "Troubleshooting", "diagnostics", "debug", "solving"),
        ("security", "Security", "hardening", "protection", "best practices"),
        ("monitoring", "Monitoring", "monitoring", "metrics", "alerts"),
        ("optimization", "Optimization", "tuning", "optimization", "throughput"),
        ("automation", "Automation", "network automation", "scripting", "IaC"),
        ("design", "Design", "network design", "architecture", "planning"),
    ], "concept", "", "networking"),

    ("networking", "tools", [
        ("wireshark", "Wireshark"), ("tcpdump", "tcpdump"), ("ping", "ping/traceroute"),
        ("netstat", "netstat/ss"), ("nslookup", "nslookup/dig"), ("nmap", "Nmap"),
        ("iperf", "iperf"), ("netcat", "netcat"), ("ip", "ip/ifconfig"),
        ("iptables", "iptables/nftables"), ("curl", "curl"), ("socat", "socat"),
    ], [
        ("basics", "Basics", "basic usage", "syntax", "intro"),
        ("configuration", "Config", "advanced config", "options", "flags"),
        ("troubleshooting", "Troubleshooting", "debugging", "analysis", "diagnosis"),
        ("scripting", "Scripting", "automation", "scripts", "integration"),
        ("performance", "Performance", "benchmarking", "measurement", "analysis"),
        ("security", "Security", "security testing", "auditing", "scanning"),
    ], "tool", "", "networking-tool"),
]

SCIENTIFIC_GROUPS = [
    ("scientific", "tools", [
        ("numpy", "NumPy"), ("scipy", "SciPy"), ("sympy", "SymPy"),
        ("matlab", "MATLAB"), ("r-lang", "R"), ("julia", "Julia"),
        ("octave", "GNU Octave"), ("sagemath", "SageMath"),
        ("mathematica", "Mathematica"), ("gnuplot", "gnuplot"),
    ], [
        ("setup", "Setup", "installation", "env", "getting started"),
        ("numerical", "Numerical", "numerical methods", "linear algebra", "optimization"),
        ("visualization", "Visualization", "scientific plots", "charts", "graphing"),
        ("statistics", "Statistics", "statistical analysis", "testing", "distributions"),
        ("signal-processing", "Signal Processing", "FFT", "filtering", "waveforms"),
        ("simulation", "Simulation", "Monte Carlo", "modeling", "simulation"),
        ("optimization", "Optimization", "optimization", "minimization", "solving"),
        ("parallel", "Parallel", "parallel computing", "GPU", "vectorization"),
    ], "framework", "python", "scientific-computing"),
]

PAYMENTS_GROUPS = [
    ("payments", "gateways", [
        ("stripe", "Stripe"), ("paypal", "PayPal"), ("square", "Square"),
        ("adyen", "Adyen"), ("braintree", "Braintree"),
        ("mollie", "Mollie"), ("paddle", "Paddle"),
    ], [
        ("setup", "Setup", "account setup", "integration", "first payment"),
        ("checkout", "Checkout", "checkout flow", "UI", "cart"),
        ("subscriptions", "Subscriptions", "recurring", "plans", "management"),
        ("webhooks", "Webhooks", "webhooks", "events", "notifications"),
        ("refunds", "Refunds", "refunds", "disputes", "chargebacks"),
        ("fraud", "Fraud", "fraud detection", "risk", "3DS"),
        ("reporting", "Reporting", "reports", "reconciliation", "analytics"),
        ("compliance", "Compliance", "PCI DSS", "regulatory", "KYC"),
    ], "platform", "", "payments"),

    ("payments", "billing", [
        ("recurly", "Recurly"), ("chargebee", "Chargebee"), ("zuora", "Zuora"),
        ("stripe-billing", "Stripe Billing"), ("paddle-billing", "Paddle Billing"),
    ], [
        ("setup", "Setup", "account setup", "integration", "config"),
        ("plans", "Plans", "plan creation", "pricing", "tiers"),
        ("invoicing", "Invoicing", "invoices", "billing cycles", "automation"),
        ("dunning", "Dunning", "retry logic", "failed payments", "recovery"),
        ("analytics", "Analytics", "revenue analytics", "MRR", "churn"),
        ("compliance", "Compliance", "tax compliance", "regulatory", "reporting"),
    ], "platform", "", "billing"),
]

# =======================================================
# PRODUCT / EMBEDDED / AR-VR / COMMUNICATIONS
# =======================================================

PRODUCT_GROUPS = [
    ("product", "methodologies", [
        ("agile", "Agile"), ("scrum", "Scrum"), ("kanban", "Kanban"),
        ("lean", "Lean"), ("safe", "SAFe"), ("less", "LeSS"),
        ("prince2", "PRINCE2"), ("pmp", "PMP"), ("itil", "ITIL"),
    ], [
        ("basics", "Basics", "fundamentals", "principles", "intro"),
        ("implementation", "Implementation", "adoption", "practice", "execution"),
        ("best-practices", "Best Practices", "practices", "guidelines", "tips"),
        ("metrics", "Metrics", "measurement", "tracking", "success"),
        ("tools", "Tools", "tooling", "software", "templates"),
        ("facilitation", "Facilitation", "sessions", "workshops", "meetings"),
        ("coaching", "Coaching", "team coaching", "mentoring", "training"),
        ("maturity", "Maturity", "assessment", "improvement", "evolution"),
    ], "concept", "", "methodology"),

    ("product", "frameworks", [
        ("user-stories", "User Stories"), ("okr", "OKRs"), ("kpi", "KPIs"),
        ("north-star", "North Star"), ("aarrr", "AARRR"), ("heuristics", "Heuristics"),
        ("design-thinking", "Design Thinking"), ("jobs-to-be-done", "Jobs to be Done"),
        ("roadmap", "Roadmapping"), ("backlog", "Backlog Management"),
        ("prioritization", "Prioritization"), ("spec", "Specification Writing"),
    ], [
        ("basics", "Basics", "fundamentals", "principles", "intro"),
        ("implementation", "Implementation", "execution", "practice", "usage"),
        ("best-practices", "Best Practices", "tips", "guidelines", "proven"),
        ("metrics", "Metrics", "measurement", "success", "tracking"),
        ("tools", "Tools", "tools", "software", "templates"),
        ("facilitation", "Facilitation", "running", "workshops", "collaboration"),
    ], "concept", "", "product-framework"),
]

EMBEDDED_GROUPS = [
    ("embedded", "arch", [
        ("arm-cortex", "ARM Cortex-M"), ("riscv", "RISC-V"), ("avr", "AVR"),
        ("pic", "PIC"), ("xtensa", "Xtensa"),
    ], [
        ("setup", "Setup", "toolchain", "project", "first build"),
        ("toolchain", "Toolchain", "compiler", "linker", "debugger"),
        ("bootstrap", "Bootstrap", "startup code", "vectors", "init"),
        ("interrupts", "Interrupts", "interrupts", "NVIC", "priorities"),
        ("memory", "Memory", "memory layout", "RAM/ROM", "linker"),
        ("dma", "DMA", "DMA", "transfers", "peripherals"),
        ("timers", "Timers", "timers", "PWM", "capture"),
        ("debugging", "Debugging", "debug", "JTAG/SWD", "logging"),
    ], "concept", "", "embedded-arch"),

    ("embedded", "rtos", [
        ("freertos", "FreeRTOS"), ("zephyr", "Zephyr"), ("rt-thread", "RT-Thread"),
        ("contiki", "Contiki-NG"), ("threadx", "ThreadX"), ("vxworks", "VxWorks"),
    ], [
        ("setup", "Setup", "setup", "config", "first task"),
        ("tasks", "Tasks", "task management", "scheduling", "priorities"),
        ("synchronization", "Sync", "mutexes", "semaphores", "queues"),
        ("memory", "Memory", "memory management", "allocation", "pools"),
        ("timers", "Timers", "software timers", "timeouts", "periodic"),
        ("interrupts", "Interrupts", "ISR handling", "deferred processing", "priorities"),
        ("debugging", "Debugging", "debug", "tracing", "analysis"),
        ("optimization", "Optimization", "optimization", "RTOS tuning", "performance"),
    ], "framework", "c", "rtos"),
]

ARVR_GROUPS = [
    ("ar-vr", "platforms", [
        ("arkit", "ARKit"), ("arcore", "ARCore"), ("webxr", "WebXR"),
        ("openxr", "OpenXR"), ("steamvr", "SteamVR"), ("oculus", "Oculus SDK"),
        ("hololens", "HoloLens"), ("magic-leap", "Magic Leap"),
        ("unity-xr", "Unity XR"), ("unreal-xr", "Unreal XR"),
    ], [
        ("setup", "Setup", "SDK setup", "project", "first scene"),
        ("tracking", "Tracking", "spatial tracking", "position", "orientation"),
        ("rendering", "Rendering", "stereoscopic", "rendering", "optimization"),
        ("interaction", "Interaction", "hand tracking", "gestures", "input"),
        ("spatial", "Spatial", "room mapping", "meshing", "anchors"),
        ("audio", "Audio", "spatial audio", "3D sound", "positional"),
        ("optimization", "Optimization", "performance", "frame rate", "optimization"),
        ("deployment", "Deployment", "deployment", "stores", "distribution"),
    ], "framework", "csharp", "ar-vr"),
]

COMMS_GROUPS = [
    ("communications", "protocols", [
        ("voip", "VoIP"), ("sip", "SIP"), ("webrtc", "WebRTC"),
        ("xmpp", "XMPP"), ("mqtt", "MQTT"), ("amqp", "AMQP"),
        ("stomp", "STOMP"), ("coap", "CoAP"),
    ], [
        ("basics", "Basics", "fundamentals", "protocol", "intro"),
        ("setup", "Setup", "setup", "server", "client"),
        ("implementation", "Implementation", "implementation", "code", "integration"),
        ("security", "Security", "security", "encryption", "auth"),
        ("testing", "Testing", "testing", "tools", "verification"),
        ("scaling", "Scaling", "scaling", "performance", "optimization"),
    ], "protocol", "", "communication-protocol"),

    ("communications", "platforms", [
        ("twilio", "Twilio"), ("sendgrid", "SendGrid"), ("mailgun", "Mailgun"),
        ("ses", "Amazon SES"), ("pusher", "Pusher"), ("pubnub", "PubNub"),
        ("vonage", "Vonage"), ("plivo", "Plivo"), ("telegram-bot", "Telegram Bot"),
        ("slack-api", "Slack API"), ("discord-bot", "Discord Bot"),
    ], [
        ("setup", "Setup", "account setup", "API", "first message"),
        ("messaging", "Messaging", "sending messages", "templates", "delivery"),
        ("voice", "Voice", "voice calls", "IVR", "conferencing"),
        ("video", "Video", "video calls", "streaming", "recording"),
        ("chat", "Chat", "chat", "bots", "automation"),
        ("webhooks", "Webhooks", "webhooks", "events", "callbacks"),
        ("analytics", "Analytics", "analytics", "tracking", "reporting"),
        ("integration", "Integration", "integration", "SDKs", "libraries"),
    ], "platform", "", "communication-platform"),
]

# =======================================================
# MORE DOMAINS (healthcare, ecommerce, education, finance, media)
# =======================================================

HEALTHCARE_GROUPS = [
    ("healthcare", "standards", [
        ("hipaa", "HIPAA"), ("fhir", "FHIR"), ("hl7", "HL7 v2"),
        ("dicom", "DICOM"), ("icd10", "ICD-10"), ("snomed", "SNOMED CT"),
        ("loinc", "LOINC"), ("ccda", "C-CDA"),
    ], [
        ("basics", "Basics", "fundamentals", "standards", "intro"),
        ("implementation", "Implementation", "integration", "systems", "code"),
        ("compliance", "Compliance", "compliance", "audits", "regulations"),
        ("interoperability", "Interop", "interoperability", "exchange", "integration"),
        ("testing", "Testing", "testing", "validation", "conformance"),
        ("tools", "Tools", "tools", "libraries", "software"),
    ], "concept", "", "healthcare"),

    ("healthcare", "systems", [
        ("ehr", "EHR Systems"), ("emr", "EMR Systems"), ("pms", "Practice Management"),
        ("labs", "LIS"), ("pharmacy", "Pharmacy Systems"), ("imaging", "PACS"),
        ("population-health", "Population Health"), ("telehealth", "Telehealth"),
    ], [
        ("setup", "Setup", "implementation", "config", "first use"),
        ("workflow", "Workflow", "clinical workflow", "process", "automation"),
        ("integration", "Integration", "system integration", "APIs", "interfaces"),
        ("data", "Data", "data management", "exchange", "analytics"),
        ("compliance", "Compliance", "compliance", "security", "auditing"),
        ("reporting", "Reporting", "reports", "dashboards", "analytics"),
    ], "concept", "", "healthcare-system"),
]

ECOMMERCE_GROUPS = [
    ("ecommerce", "platforms", [
        ("shopify", "Shopify"), ("magento", "Magento"), ("woocommerce", "WooCommerce"),
        ("bigcommerce", "BigCommerce"), ("salesforce-commerce", "Salesforce Commerce"),
        ("commercetools", "commercetools"), ("medusa", "Medusa"),
        ("vendure", "Vendure"), ("saleor", "Saleor"),
    ], [
        ("setup", "Setup", "setup", "config", "first product"),
        ("products", "Products", "product management", "catalog", "variants"),
        ("cart", "Cart", "cart", "checkout", "UX"),
        ("payments", "Payments", "payment integration", "gateways", "processing"),
        ("shipping", "Shipping", "shipping", "rates", "fulfillment"),
        ("orders", "Orders", "order management", "processing", "fulfillment"),
        ("marketing", "Marketing", "marketing", "promotions", "SEO"),
        ("analytics", "Analytics", "analytics", "reports", "tracking"),
    ], "platform", "", "ecommerce"),

    ("ecommerce", "headless", [
        ("commercetools", "commercetools"), ("shopify-storefront", "Shopify Storefront"),
        ("medusa", "Medusa"), ("vendure", "Vendure"), ("saleor", "Saleor"),
        ("swell", "Swell"), ("elastic-path", "Elastic Path"),
    ], [
        ("setup", "Setup", "setup", "API setup", "first query"),
        ("products", "Products", "product API", "catalog", "search"),
        ("cart", "Cart", "cart API", "checkout", "orders"),
        ("customers", "Customers", "customer API", "accounts", "auth"),
        ("content", "Content", "content management", "CMS", "pages"),
        ("integration", "Integration", "frontend integration", "Next.js", "React"),
    ], "platform", "", "headless-commerce"),
]

EDUCATION_GROUPS = [
    ("education", "platforms", [
        ("moodle", "Moodle"), ("canvas", "Canvas LMS"), ("blackboard", "Blackboard"),
        ("sakai", "Sakai"), ("edx", "Open edX"), ("brightspace", "Brightspace"),
        ("teachable", "Teachable"), ("thinkific", "Thinkific"),
    ], [
        ("setup", "Setup", "setup", "config", "first course"),
        ("courses", "Courses", "course creation", "content", "structure"),
        ("assessments", "Assessments", "quizzes", "assignments", "grading"),
        ("users", "Users", "user management", "roles", "enrollment"),
        ("analytics", "Analytics", "analytics", "reports", "tracking"),
        ("integration", "Integration", "LTI", "API", "plugins"),
    ], "platform", "", "education-platform"),

    ("education", "standards", [
        ("lti", "LTI"), ("xapi", "xAPI"), ("scorm", "SCORM"),
        ("caliper", "Caliper"), ("oneRoster", "OneRoster"),
    ], [
        ("basics", "Basics", "fundamentals", "standard", "intro"),
        ("implementation", "Implementation", "implementation", "integration", "code"),
        ("testing", "Testing", "testing", "conformance", "validation"),
        ("deployment", "Deployment", "deployment", "LMS integration", "production"),
    ], "concept", "", "education-standard"),
]

FINANCE_GROUPS = [
    ("finance", "trading", [
        ("algo-trading", "Algorithmic Trading"), ("backtesting", "Backtesting"),
        ("market-data", "Market Data"), ("order-management", "OMS"),
        ("risk-management", "Risk Management"), ("portfolio", "Portfolio Management"),
        ("execution", "Execution Systems"), ("compliance-trading", "Trading Compliance"),
    ], [
        ("basics", "Basics", "fundamentals", "concepts", "intro"),
        ("implementation", "Implementation", "implementation", "systems", "code"),
        ("data", "Data", "data sources", "feeds", "storage"),
        ("strategy", "Strategy", "strategy dev", "backtesting", "optimization"),
        ("risk", "Risk", "risk analysis", "limits", "monitoring"),
        ("reporting", "Reporting", "reports", "P&L", "analytics"),
    ], "concept", "", "trading"),

    ("finance", "fintech", [
        ("open-banking", "Open Banking"), ("psd2", "PSD2"), ("plaid", "Plaid"),
        ("yodlee", "Yodlee"), ("teller", "Teller"), ("dwolla", "Dwolla"),
        ("marqeta", "Marqeta"), ("synctera", "Synctera"),
    ], [
        ("setup", "Setup", "account setup", "API", "integration"),
        ("accounts", "Accounts", "account linking", "verification", "data"),
        ("payments", "Payments", "payments", "transfers", "ACH"),
        ("compliance", "Compliance", "compliance", "KYC", "AML"),
        ("data", "Data", "financial data", "aggregation", "analysis"),
        ("security", "Security", "security", "encryption", "auth"),
    ], "platform", "", "fintech"),
]

MEDIA_GROUPS = [
    ("media", "streaming", [
        ("hls", "HLS"), ("dash", "MPEG-DASH"), ("rtmp", "RTMP"),
        ("srt", "SRT"), ("webRTC-streaming", "WebRTC Streaming"),
        ("ffmpeg", "FFmpeg"), ("gstreamer", "GStreamer"),
        ("encoding", "Encoding"), ("transcoding", "Transcoding"),
    ], [
        ("setup", "Setup", "setup", "config", "first stream"),
        ("encoding", "Encoding", "encoding", "codecs", "settings"),
        ("packaging", "Packaging", "packaging", "segments", "manifests"),
        ("delivery", "Delivery", "delivery", "CDN", "players"),
        ("protection", "Protection", "DRM", "encryption", "security"),
        ("analytics", "Analytics", "analytics", "QoS", "monitoring"),
    ], "tool", "", "media-streaming"),

    ("media", "production", [
        ("davinci", "DaVinci Resolve"), ("premiere", "Premiere Pro"), ("final-cut", "Final Cut Pro"),
        ("after-effects", "After Effects"), ("nuke", "Nuke"), ("blender-vfx", "Blender VFX"),
        ("color-grading", "Color Grading"), ("compositing", "Compositing"),
    ], [
        ("setup", "Setup", "setup", "project", "first edit"),
        ("editing", "Editing", "editing", "timeline", "cuts"),
        ("effects", "Effects", "VFX", "transitions", "effects"),
        ("color", "Color", "color grading", "correction", "looks"),
        ("audio", "Audio", "audio editing", "mixing", "sound design"),
        ("export", "Export", "export", "rendering", "delivery"),
    ], "tool", "", "media-production"),
]

# =======================================================
# REMAINING: engineering / os-admin / energy / sustainability / hr
# =======================================================

ENG_GROUPS = [
    ("engineering", "practices", [
        ("code-review", "Code Review"), ("pair-programming", "Pair Programming"),
        ("tdd", "TDD"), ("bdd", "BDD"), ("ddd", "Domain-Driven Design"),
        ("clean-code", "Clean Code"), ("refactoring", "Refactoring"),
        ("documentation", "Documentation"), ("api-design", "API Design"),
        ("tech-debt", "Tech Debt Management"),
    ], [
        ("basics", "Basics", "fundamentals", "principles", "intro"),
        ("implementation", "Implementation", "practice", "application", "execution"),
        ("best-practices", "Best Practices", "tips", "guidelines", "standards"),
        ("tools", "Tools", "tooling", "automation", "support"),
        ("team", "Team", "team adoption", "culture", "collaboration"),
        ("measurement", "Measurement", "metrics", "tracking", "improvement"),
    ], "concept", "", "engineering"),

    ("engineering", "modeling", [
        ("uml", "UML"), ("c4-model", "C4 Model"), ("archimate", "ArchiMate"),
        ("bpmn", "BPMN"), ("er-diagrams", "ER Diagrams"),
        ("system-design", "System Design"), ("architecture", "Software Architecture"),
        ("event-storming", "Event Storming"), ("mermaid", "Mermaid.js"),
        ("plantuml", "PlantUML"), ("drawio", "Draw.io"),
    ], [
        ("basics", "Basics", "fundamentals", "notation", "intro"),
        ("diagrams", "Diagrams", "diagramming", "creation", "tools"),
        ("modeling", "Modeling", "system modeling", "design", "documentation"),
        ("best-practices", "Best Practices", "practices", "guidelines", "standards"),
        ("tools", "Tools", "tooling", "software", "editors"),
        ("collaboration", "Collaboration", "team collaboration", "sharing", "review"),
    ], "concept", "", "modeling"),
]

OSADMIN_GROUPS = [
    ("os-admin", "linux", [
        ("ubuntu", "Ubuntu"), ("debian", "Debian"), ("centos", "CentOS"),
        ("rhel", "RHEL"), ("fedora", "Fedora"), ("arch", "Arch Linux"),
        ("suse", "SUSE"), ("alpine", "Alpine Linux"),
        ("systemd", "systemd"), ("bash", "Bash Scripting"),
        ("linux-kernel", "Linux Kernel"), ("linux-security", "Linux Security"),
    ], [
        ("setup", "Setup", "installation", "config", "first use"),
        ("packages", "Packages", "package management", "apt", "yum"),
        ("users", "Users", "user management", "groups", "permissions"),
        ("filesystem", "Filesystem", "filesystem", "storage", "mounts"),
        ("networking", "Networking", "network config", "interfaces", "firewall"),
        ("processes", "Processes", "process management", "services", "monitoring"),
        ("security", "Security", "hardening", "SELinux", "apparmor"),
        ("automation", "Automation", "scripting", "cron", "systemd timers"),
        ("backup", "Backup", "backup", "recovery", "snapshots"),
        ("logging", "Logging", "logging", "journald", "syslog"),
    ], "concept", "", "linux"),

    ("os-admin", "windows", [
        ("windows-server", "Windows Server"), ("active-directory", "Active Directory"),
        ("powershell", "PowerShell"), ("group-policy", "Group Policy"),
        ("iis", "IIS"), ("hyper-v", "Hyper-V"),
        ("windows-update", "Windows Update"), ("bitlocker", "BitLocker"),
        ("registry", "Windows Registry"), ("performance-monitor", "Performance Monitor"),
    ], [
        ("setup", "Setup", "installation", "config", "first use"),
        ("users", "Users", "user mgmt", "AD", "permissions"),
        ("networking", "Networking", "network", "DNS", "DHCP"),
        ("security", "Security", "security", "policies", "defender"),
        ("automation", "Automation", "PowerShell", "scripts", "scheduled tasks"),
        ("monitoring", "Monitoring", "monitoring", "perfmon", "events"),
        ("backup", "Backup", "backup", "recovery", "snapshots"),
        ("iis", "IIS", "web server", "sites", "app pools"),
    ], "concept", "", "windows"),
]

ENERGY_GROUPS = [
    ("energy", "smart-grid", [
        ("scada", "SCADA"), ("plc", "PLC Programming"), ("modbus", "Modbus"),
        ("dnp3", "DNP3"), ("iec61850", "IEC 61850"),
        ("smart-meter", "Smart Metering"), ("demand-response", "Demand Response"),
        ("grid-optimization", "Grid Optimization"),
    ], [
        ("basics", "Basics", "fundamentals", "concepts", "intro"),
        ("protocols", "Protocols", "communication", "protocols", "integration"),
        ("implementation", "Implementation", "deployment", "systems", "config"),
        ("monitoring", "Monitoring", "monitoring", "data collection", "analysis"),
        ("security", "Security", "security", "OT security", "hardening"),
        ("analytics", "Analytics", "analytics", "optimization", "forecasting"),
    ], "concept", "", "smart-grid"),

    ("energy", "renewable", [
        ("solar-pv", "Solar PV"), ("wind-energy", "Wind Energy"),
        ("battery-storage", "Battery Storage"), ("ev-charging", "EV Charging"),
        ("microgrid", "Microgrid"), ("energy-management", "Energy Management"),
    ], [
        ("basics", "Basics", "fundamentals", "technology", "intro"),
        ("design", "Design", "system design", "sizing", "configuration"),
        ("monitoring", "Monitoring", "monitoring", "data", "performance"),
        ("optimization", "Optimization", "optimization", "efficiency", "analytics"),
        ("integration", "Integration", "grid integration", "interconnection", "compliance"),
    ], "concept", "", "renewable-energy"),
]

HR_GROUPS = [
    ("hr", "systems", [
        ("workday", "Workday"), ("sap-successfactors", "SAP SuccessFactors"),
        ("bamboohr", "BambooHR"), ("greenhouse", "Greenhouse"),
        ("lever", "Lever"), ("hubstaff", "Hubstaff"),
        ("deel", "Deel"), ("remote", "Remote.com"),
    ], [
        ("setup", "Setup", "setup", "config", "first use"),
        ("employees", "Employees", "employee mgmt", "data", "org"),
        ("payroll", "Payroll", "payroll", "benefits", "compliance"),
        ("recruiting", "Recruiting", "ATS", "candidates", "hiring"),
        ("performance", "Performance", "performance mgmt", "reviews", "goals"),
        ("analytics", "Analytics", "analytics", "reports", "insights"),
        ("integration", "Integration", "integration", "APIs", "SSO"),
        ("compliance", "Compliance", "compliance", "regulations", "reporting"),
    ], "platform", "", "hr-tech"),

    ("hr", "recruiting", [
        ("linkedin-recruiter", "LinkedIn Recruiter"), ("indeed", "Indeed"),
        ("glassdoor", "Glassdoor"), ("ziprecruiter", "ZipRecruiter"),
        ("angelist", "AngelList/Wellfound"), ("hackerrank", "HackerRank"),
        ("codility", "Codility"), ("interviewing", "Technical Interviewing"),
    ], [
        ("sourcing", "Sourcing", "candidate sourcing", "search", "outreach"),
        ("screening", "Screening", "resume screening", "assessment", "filtering"),
        ("interviewing", "Interviewing", "interviews", "questions", "evaluation"),
        ("offers", "Offers", "offer mgmt", "negotiation", "closing"),
        ("analytics", "Analytics", "analytics", "metrics", "improvement"),
        ("tools", "Tools", "tools", "ATS", "platforms"),
    ], "concept", "", "recruiting"),
]

SUPPLY_CHAIN_GROUPS = [
    ("supply-chain", "systems", [
        ("sap", "SAP SCM"), ("oracle-scm", "Oracle SCM"), ("blue-yonder", "Blue Yonder"),
        ("kinaxis", "Kinaxis"), ("jda", "JDA/Blue Yonder"),
        ("manhattan", "Manhattan Associates"), ("highjump", "HighJump"),
        ("infor", "Infor SCM"),
    ], [
        ("setup", "Setup", "setup", "config", "first use"),
        ("inventory", "Inventory", "inventory mgmt", "tracking", "optimization"),
        ("warehousing", "Warehousing", "WMS", "operations", "fulfillment"),
        ("transportation", "Transportation", "TMS", "shipping", "logistics"),
        ("planning", "Planning", "demand planning", "forecasting", "replenishment"),
        ("procurement", "Procurement", "procurement", "purchasing", "suppliers"),
        ("analytics", "Analytics", "analytics", "reports", "optimization"),
        ("integration", "Integration", "integration", "EDI", "APIs"),
    ], "platform", "", "supply-chain"),

    ("supply-chain", "logistics", [
        ("shipstation", "ShipStation"), ("easypost", "EasyPost"), ("shippo", "Shippo"),
        ("flexport", "Flexport"), ("project44", "project44"),
        ("fourkites", "FourKites"), ("tive", "Tive"),
    ], [
        ("setup", "Setup", "setup", "API", "first shipment"),
        ("shipping", "Shipping", "shipping", "carriers", "rates"),
        ("tracking", "Tracking", "tracking", "visibility", "alerts"),
        ("warehouse", "Warehouse", "warehouse ops", "picking", "packing"),
        ("integration", "Integration", "integration", "ecommerce", "ERP"),
        ("analytics", "Analytics", "analytics", "metrics", "optimization"),
    ], "platform", "", "logistics"),
]

GEO_GROUPS = [
    ("geospatial", "tools", [
        ("qgis", "QGIS"), ("arcgis", "ArcGIS"), ("postgis", "PostGIS"),
        ("geoserver", "GeoServer"), ("mapserver", "MapServer"),
        ("leaflet", "Leaflet"), ("mapbox", "Mapbox"), ("openlayers", "OpenLayers"),
        ("google-maps", "Google Maps API"), ("mapbox-gl", "Mapbox GL"),
        ("kepler", "Kepler.gl"), ("deck-gl", "Deck.gl"),
    ], [
        ("setup", "Setup", "setup", "config", "first map"),
        ("data", "Data", "geospatial data", "formats", "sources"),
        ("mapping", "Mapping", "mapping", "visualization", "styling"),
        ("analysis", "Analysis", "spatial analysis", "queries", "buffers"),
        ("routing", "Routing", "routing", "directions", "networks"),
        ("tiles", "Tiles", "tile serving", "rendering", "caching"),
        ("geocoding", "Geocoding", "geocoding", "reverse geocoding", "addresses"),
        ("integration", "Integration", "integration", "APIs", "web apps"),
    ], "framework", "javascript", "gis"),
]

SUSTAINABILITY_GROUPS = [
    ("sustainability", "standards", [
        ("esg", "ESG"), ("csrd", "CSRD"), ("gri", "GRI"),
        ("sasb", "SASB"), ("tcfd", "TCFD"), ("sbti", "SBTi"),
        ("ghg-protocol", "GHG Protocol"), ("carbon-accounting", "Carbon Accounting"),
    ], [
        ("basics", "Basics", "fundamentals", "framework", "intro"),
        ("reporting", "Reporting", "reporting", "disclosure", "compliance"),
        ("measurement", "Measurement", "measurement", "carbon footprint", "metrics"),
        ("data", "Data", "data collection", "management", "analytics"),
        ("tools", "Tools", "tools", "software", "platforms"),
        ("strategy", "Strategy", "strategy", "targets", "roadmap"),
    ], "concept", "", "sustainability"),
]

# =======================================================
# GENERATOR RUNNER
# =======================================================

ALL_GROUPS = (
    AI_GROUPS + BACKEND_GROUPS + FRONTEND_GROUPS + DEVOPS_GROUPS +
    DATABASE_GROUPS + DATA_GROUPS + QA_GROUPS + SECURITY_GROUPS +
    MOBILE_GROUPS + DESIGN_GROUPS + GAMEDEV_GROUPS + BLOCKCHAIN_GROUPS +
    IOT_GROUPS + DESKTOP_GROUPS + NETWORKING_GROUPS + SCIENTIFIC_GROUPS +
    PAYMENTS_GROUPS + PRODUCT_GROUPS + EMBEDDED_GROUPS + ARVR_GROUPS +
    COMMS_GROUPS + HEALTHCARE_GROUPS + ECOMMERCE_GROUPS + EDUCATION_GROUPS +
    FINANCE_GROUPS + MEDIA_GROUPS + ENG_GROUPS + OSADMIN_GROUPS +
    ENERGY_GROUPS + HR_GROUPS + SUPPLY_CHAIN_GROUPS + GEO_GROUPS +
    SUSTAINABILITY_GROUPS
)

def main():
    total = 0
    skipped = 0
    created = 0
    for group_cat, sub, items, topics, template, lang, extra_tag in ALL_GROUPS:
        skills = make_skills(group_cat, sub, items, topics, template, lang, extra_tag)
        for s in skills:
            total += 1
            name = s["name"]
            # Skip if already exists
            dir_path = os.path.join(BASE, group_cat, name)
            fpath = os.path.join(dir_path, "SKILL.md")
            if os.path.exists(fpath):
                skipped += 1
                continue
            os.makedirs(dir_path, exist_ok=True)
            tmpl_key = s["template"]
            content = TMPL.get(tmpl_key, TMPL["framework"]).format(**s)
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(content)
            created += 1
            if created % 200 == 0:
                print(f"  Created {created}...")

    print(f"\n=== Generation Complete ===")
    print(f"Total defined: {total}")
    print(f"Created: {created}")
    print(f"Skipped (already exist): {skipped}")
    # Count existing
    import glob
    existing = len(glob.glob(os.path.join(BASE, "**", "SKILL.md"), recursive=True))
    print(f"Total SKILL.md files on disk: {existing}")

if __name__ == "__main__":
    main()
