import os, json

NEW_SKILLS = [
    # backend
    {
        "name": "flask-python",
        "description": "Creates lightweight web applications and REST APIs with Flask, Jinja2 templates, and SQLAlchemy. Use for simple Python web apps and microservices.",
        "category": "backend",
        "tags": ["python", "flask", "web", "jinja", "sqlalchemy"],
        "models": ["sonnet", "opus"],
        "template": """# Flask Python

> Lightweight Python web framework with Jinja2 templates.

## Quick Start
```python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/api/health")
def health():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(debug=True)
```

## When to Use
- Simple web apps and APIs
- Prototyping and MVPs
- Small microservices
- Traditional server-rendered apps

## Step-by-Step
1. Install: `pip install flask`
2. Create `app.py` with routes
3. Use Jinja2 templates for HTML
4. Run: `python app.py`

## Dependencies
```bash
pip install flask flask-sqlalchemy jinja2
```

## Examples
```python
@app.route("/users/<int:id>")
def get_user(id):
    return jsonify({"id": id, "name": "Alice"})
```

## Resources
- [Flask Docs](https://flask.palletsprojects.com)

## Validation
1. Server starts on http://localhost:5000
2. `/api/health` returns 200
3. Templates render correctly"""
    },
    {
        "name": "websocket",
        "description": "Implements real-time bidirectional communication using WebSockets with Socket.IO, ws, or native WebSocket API. Use for chat, live updates, and collaborative apps.",
        "category": "backend",
        "tags": ["websocket", "realtime", "socketio", "nodejs", "python"],
        "models": ["sonnet", "opus"],
        "template": """# WebSocket

> Real-time bidirectional communication for modern apps.

## Quick Start (Node.js + ws)
```javascript
const WebSocket = require('ws');
const wss = new WebSocket.Server({ port: 8080 });

wss.on('connection', (ws) => {
  ws.on('message', (msg) => {
    console.log('received:', msg.toString());
    ws.send(`Echo: ${msg}`);
  });
});
```

## When to Use
- Chat applications
- Live notifications
- Collaborative editing
- Real-time dashboards

## Step-by-Step
1. Install WebSocket library
2. Create server with connection handler
3. Handle messages and broadcast
4. Connect from client with `new WebSocket(url)`

## Dependencies
```bash
npm install ws socket.io
# or
pip install websockets
```

## Examples
Client: `new WebSocket("ws://localhost:8080")`
Server broadcasts to all connected clients.

## Resources
- [MDN WebSocket API](https://developer.mozilla.org/en-US/docs/Web/API/WebSocket)

## Validation
1. Server starts on ws://localhost:8080
2. Client connects successfully
3. Messages echo back correctly"""
    },
    # frontend
    {
        "name": "gatsby",
        "description": "Builds blazing-fast static sites and progressive web apps with Gatsby, React, and GraphQL. Use for content-driven sites and documentation.",
        "category": "frontend",
        "tags": ["gatsby", "react", "graphql", "static-site", "pwa"],
        "models": ["sonnet", "opus"],
        "template": """# Gatsby

> React-based static site generator with GraphQL data layer.

## Quick Start
```bash
npm init gatsby
cd my-site
npm run develop
```

## When to Use
- Blogs and marketing sites
- Documentation portals
- E-commerce storefronts
- Portfolio websites

## Step-by-Step
1. Create site: `npm init gatsby`
2. Add plugins for data sources
3. Query data with GraphQL
4. Build: `npm run build`

## Dependencies
```bash
npm install gatsby react react-dom
```

## Examples
```jsx
import { graphql, useStaticQuery } from "gatsby"

export default function Home() {
  const data = useStaticQuery(graphql`
    query { site { siteMetadata { title } } }
  `)
  return <h1>{data.site.siteMetadata.title}</h1>
}
```

## Resources
- [Gatsby Docs](https://www.gatsbyjs.com/docs)

## Validation
1. Dev server runs on port 8000
2. Build completes without errors
3. Pages render from GraphQL data"""
    },
    {
        "name": "nuxt",
        "description": "Creates universal Vue applications with Nuxt 3, file-based routing, SSR, and auto-imports. Use for SEO-friendly Vue apps.",
        "category": "frontend",
        "tags": ["nuxt", "vue", "ssr", "ssg", "vue3"],
        "models": ["sonnet", "opus"],
        "template": """# Nuxt

> Vue.js framework with SSR, SSG, and file-based routing.

## Quick Start
```bash
npx nuxi init my-app
cd my-app
npm run dev
```

## When to Use
- SEO-critical Vue apps
- Full-stack Vue applications
- Static generated sites
- Enterprise dashboards

## Step-by-Step
1. Init project: `npx nuxi init`
2. Create pages in `pages/` directory
3. Use auto-imported components
4. Deploy with `npm run build`

## Dependencies
```bash
npm install nuxt
```

## Examples
```vue
<template>
  <div>
    <h1>{{ title }}</h1>
    <NuxtLink to="/about">About</NuxtLink>
  </div>
</template>
<script setup>
const { data: title } = await useFetch('/api/title')
</script>
```

## Resources
- [Nuxt Docs](https://nuxt.com/docs)

## Validation
1. Dev server runs on port 3000
2. SSR renders HTML correctly
3. Navigation works without full reload"""
    },
    {
        "name": "storybook",
        "description": "Develops UI components in isolation with Storybook, supporting multiple frameworks. Use for building component libraries and design systems.",
        "category": "frontend",
        "tags": ["storybook", "components", "design-system", "react", "vue"],
        "models": ["sonnet", "opus"],
        "template": """# Storybook

> UI component explorer for isolated development and testing.

## Quick Start
```bash
npx storybook@latest init
npm run storybook
```

## When to Use
- Building component libraries
- Design system documentation
- Visual regression testing
- Component-driven development

## Step-by-Step
1. Init: `npx storybook@latest init`
2. Write stories in `*.stories.tsx` files
3. Configure addons in `.storybook/main.ts`
4. Build: `npm run build-storybook`

## Dependencies
```bash
npm install @storybook/react @storybook/addon-essentials
```

## Examples
```tsx
import type { Meta, StoryObj } from '@storybook/react'
import { Button } from './Button'

const meta: Meta<typeof Button> = {
  component: Button,
  argTypes: { variant: { control: 'select' } },
}
export default meta

export const Primary: StoryObj<typeof Button> = {
  args: { variant: 'primary', children: 'Click me' },
}
```

## Resources
- [Storybook Docs](https://storybook.js.org/docs)

## Validation
1. Storybook opens on port 6006
2. All stories render without errors
3. Controls and actions work"""
    },
    # database
    {
        "name": "postgresql",
        "description": "Models relational data, writes optimized queries, and manages PostgreSQL databases with indexes, views, and CTEs. Use for robust data storage.",
        "category": "database",
        "tags": ["postgresql", "sql", "database", "relational", "queries"],
        "models": ["sonnet", "opus"],
        "template": """# PostgreSQL

> Advanced relational database with powerful querying and indexing.

## Quick Start
```sql
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  name VARCHAR(100) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  created_at TIMESTAMP DEFAULT NOW()
);

CREATE INDEX idx_users_email ON users(email);
```

## When to Use
- Structured relational data
- Complex queries and joins
- Transactional workloads
- Analytics with window functions

## Step-by-Step
1. Install PostgreSQL
2. Create database: `CREATE DATABASE mydb;`
3. Design schema with migrations
4. Optimize with EXPLAIN ANALYZE

## Dependencies
```bash
# psql client
psql -h localhost -U postgres -d mydb
```

## Examples
```sql
SELECT u.name, COUNT(o.id) as order_count
FROM users u
LEFT JOIN orders o ON o.user_id = u.id
GROUP BY u.id
HAVING COUNT(o.id) > 5
ORDER BY order_count DESC;
```

## Resources
- [PostgreSQL Docs](https://www.postgresql.org/docs)

## Validation
1. Connection succeeds
2. Queries return correct results
3. Indexes improve query performance"""
    },
    {
        "name": "elasticsearch",
        "description": "Indexes, searches, and analyzes data with Elasticsearch, using full-text search, aggregations, and Kibana visualization. Use for search and log analytics.",
        "category": "database",
        "tags": ["elasticsearch", "search", "kibana", "analytics", "nosql"],
        "models": ["sonnet", "opus"],
        "template": """# Elasticsearch

> Distributed search and analytics engine for all types of data.

## Quick Start
```json
PUT /products/_doc/1
{
  "name": "Wireless Mouse",
  "price": 29.99,
  "tags": ["electronics", "accessories"]
}
```

## When to Use
- Full-text search
- Log and event analytics
- Product catalogs
- Metrics and monitoring

## Step-by-Step
1. Start Elasticsearch + Kibana
2. Create index with mapping
3. Index documents
4. Search with query DSL

## Dependencies
```bash
# Docker
docker run -p 9200:9200 -e "discovery.type=single-node" elasticsearch:8.x
```

## Examples
```json
GET /products/_search
{
  "query": { "match": { "name": "wireless mouse" } },
  "aggs": { "avg_price": { "avg": { "field": "price" } } }
}
```

## Resources
- [Elasticsearch Guide](https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html)

## Validation
1. Cluster health is green
2. Documents indexed and searchable
3. Aggregations return correct results"""
    },
    {
        "name": "dynamodb",
        "description": "Designs NoSQL tables, writes efficient queries, and manages capacity with AWS DynamoDB. Use for serverless applications at scale.",
        "category": "database",
        "tags": ["dynamodb", "aws", "nosql", "serverless", "database"],
        "models": ["sonnet", "opus"],
        "template": """# DynamoDB

> AWS NoSQL database with single-digit millisecond performance.

## Quick Start
```javascript
import { DynamoDBClient } from "@aws-sdk/client-dynamodb";
import { DynamoDBDocumentClient, PutCommand } from "@aws-sdk/lib-dynamodb";

const client = DynamoDBDocumentClient.from(new DynamoDBClient({}));
await client.send(new PutCommand({
  TableName: "Users",
  Item: { id: "123", name: "Alice", email: "alice@example.com" }
}));
```

## When to Use
- Serverless applications
- High-scale read/write workloads
- Key-value access patterns
- Time-series data

## Step-by-Step
1. Define table with partition key
2. Choose secondary indexes
3. Provision capacity or use on-demand
4. Query with key or index

## Dependencies
```bash
npm install @aws-sdk/client-dynamodb @aws-sdk/lib-dynamodb
```

## Examples
```javascript
const result = await client.send(new QueryCommand({
  TableName: "Users",
  KeyConditionExpression: "id = :id",
  ExpressionAttributeValues: { ":id": "123" }
}));
```

## Resources
- [DynamoDB Docs](https://docs.aws.amazon.com/dynamodb)

## Validation
1. Table creation succeeds
2. Put/Get/Query operations work
3. Capacity matches workload"""
    },
    # data
    {
        "name": "dbt",
        "description": "Transforms data in warehouses using dbt with SQL models, tests, and documentation. Use for analytics engineering and data transformation.",
        "category": "data",
        "tags": ["dbt", "sql", "data-warehouse", "analytics", "etl"],
        "models": ["sonnet", "opus"],
        "template": """# dbt

> Data transformation tool that enables analytics engineers to transform data in their warehouses.

## Quick Start
```sql
-- models/staging/stg_orders.sql
WITH source AS (
  SELECT * FROM {{ source('shopify', 'orders') }}
)
SELECT
  id AS order_id,
  customer_id,
  total_price,
  created_at
FROM source
```

## When to Use
- Data warehouse transformations
- Analytics engineering
- Data quality testing
- Documentation generation

## Step-by-Step
1. Init: `dbt init my_project`
2. Write SQL models in `models/`
3. Define sources and tests
4. Run: `dbt run`

## Dependencies
```bash
pip install dbt-core dbt-postgres
dbt init my_project
```

## Examples
```sql
{{ config(materialized='table') }}
SELECT
  customer_id,
  COUNT(*) as order_count,
  SUM(total_price) as total_spent
FROM {{ ref('stg_orders') }}
GROUP BY customer_id
```

## Resources
- [dbt Docs](https://docs.getdbt.com)

## Validation
1. `dbt run` completes successfully
2. `dbt test` passes all tests
3. Documentation generates: `dbt docs generate`"""
    },
    {
        "name": "snowflake",
        "description": "Manages data warehousing with Snowflake, including virtual warehouses, clustering, and semi-structured data support. Use for cloud analytics at scale.",
        "category": "data",
        "tags": ["snowflake", "data-warehouse", "cloud", "analytics", "sql"],
        "models": ["sonnet", "opus"],
        "template": """# Snowflake

> Cloud data warehouse with separate storage and compute.

## Quick Start
```sql
CREATE WAREHOUSE my_wh WITH WAREHOUSE_SIZE = 'XSMALL';
CREATE DATABASE analytics;
CREATE TABLE users (
  id INTEGER,
  name VARCHAR(100),
  email VARCHAR(255),
  created_at TIMESTAMP_NTZ
);
```

## When to Use
- Cloud data warehousing
- Analytics and reporting
- Semi-structured data (JSON, Parquet)
- Data sharing across organizations

## Step-by-Step
1. Create warehouse and database
2. Load data from stage
3. Query with standard SQL
4. Set up cloning and time travel

## Dependencies
```sql
ALTER WAREHOUSE my_wh RESUME;
USE DATABASE analytics;
```

## Examples
```sql
SELECT
  DATE_TRUNC('MONTH', created_at) AS month,
  COUNT(*) AS signups
FROM users
WHERE created_at >= DATEADD(YEAR, -1, CURRENT_DATE())
GROUP BY month
ORDER BY month;
```

## Resources
- [Snowflake Docs](https://docs.snowflake.com)

## Validation
1. Warehouse starts and runs queries
2. Data loads from stage successfully
3. Time travel queries return historical data"""
    },
    # ai
    {
        "name": "openai-api",
        "description": "Integrates OpenAI API for chat completions, embeddings, and function calling in applications. Use for adding LLM capabilities.",
        "category": "ai",
        "tags": ["openai", "gpt", "api", "llm", "embeddings"],
        "models": ["sonnet", "opus"],
        "template": """# OpenAI API

> Integrate GPT models and embeddings into your applications.

## Quick Start
```python
from openai import OpenAI

client = OpenAI()
response = client.chat.completions.create(
  model="gpt-4o",
  messages=[{"role": "user", "content": "Hello!"}]
)
print(response.choices[0].message.content)
```

## When to Use
- Chat applications and assistants
- Content generation
- Embeddings for search
- Function calling and tool use

## Step-by-Step
1. Install: `pip install openai`
2. Set `OPENAI_API_KEY` environment variable
3. Use chat completions or embeddings
4. Handle streaming responses

## Dependencies
```bash
pip install openai
export OPENAI_API_KEY=sk-...
```

## Examples
```python
stream = client.chat.completions.create(
  model="gpt-4o",
  messages=[{"role": "user", "content": "Tell me a story"}],
  stream=True
)
for chunk in stream:
  print(chunk.choices[0].delta.content or "", end="")
```

## Resources
- [OpenAI API Reference](https://platform.openai.com/docs/api-reference)

## Validation
1. API key authenticates
2. Chat completion returns response
3. Streaming works correctly"""
    },
    {
        "name": "ollama",
        "description": "Runs large language models locally with Ollama, including model management, custom Modelfiles, and API integration. Use for private, offline LLM inference.",
        "category": "ai",
        "tags": ["ollama", "llm", "local", "offline", "llama"],
        "models": ["sonnet", "opus"],
        "template": """# Ollama

> Run LLMs locally with simple commands and a REST API.

## Quick Start
```bash
ollama pull llama3.2
ollama run llama3.2 "What is the capital of France?"
```

## When to Use
- Private/local LLM inference
- Offline AI applications
- Testing models without API costs
- Custom fine-tuned models

## Step-by-Step
1. Install Ollama from ollama.com
2. Pull a model: `ollama pull llama3.2`
3. Run interactively or via API
4. Create custom Modelfiles

## Dependencies
```bash
# Install from https://ollama.com
ollama pull llama3.2:3b
```

## Examples
```python
import requests
response = requests.post("http://localhost:11434/api/generate", json={
  "model": "llama3.2",
  "prompt": "Why is the sky blue?",
  "stream": False
})
print(response.json()["response"])
```

## Resources
- [Ollama GitHub](https://github.com/ollama/ollama)

## Validation
1. Ollama service is running
2. Model pulls and runs successfully
3. API returns responses at localhost:11434"""
    },
    # devops
    {
        "name": "circleci",
        "description": "Configures CI/CD pipelines with CircleCI using orbs, workspaces, and parallelism. Use for automating builds, tests, and deployments.",
        "category": "devops",
        "tags": ["circleci", "ci-cd", "pipelines", "automation", "devops"],
        "models": ["sonnet", "opus"],
        "template": """# CircleCI

> Continuous integration and delivery platform with powerful pipeline configuration.

## Quick Start
```yaml
version: 2.1
jobs:
  build:
    docker:
      - image: cimg/node:20.0
    steps:
      - checkout
      - run: npm ci
      - run: npm test
workflows:
  version: 2
  test:
    jobs:
      - build
```

## When to Use
- Automated testing on every commit
- Multi-environment deployments
- Parallel test execution
- Docker image builds

## Step-by-Step
1. Add `.circleci/config.yml` to repo
2. Configure jobs and workflows
3. Set environment variables in UI
4. Push to trigger pipeline

## Dependencies
```bash
# Local validation
circleci local execute --job build
```

## Examples
```yaml
jobs:
  deploy:
    docker:
      - image: cimg/python:3.11
    steps:
      - checkout
      - run: pip install -r requirements.txt
      - run: python deploy.py
```

## Resources
- [CircleCI Docs](https://circleci.com/docs)

## Validation
1. Pipeline triggers on git push
2. All jobs pass successfully
3. Artifacts are accessible"""
    },
    {
        "name": "gitlab-ci",
        "description": "Configures GitLab CI/CD pipelines with stages, jobs, and GitLab Runner. Use for Git-native automation and deployment.",
        "category": "devops",
        "tags": ["gitlab", "ci-cd", "pipelines", "runner", "devops"],
        "models": ["sonnet", "opus"],
        "template": """# GitLab CI/CD

> Git-integrated CI/CD with powerful pipeline orchestration.

## Quick Start
```yaml
stages:
  - test
  - build
  - deploy

test:
  stage: test
  image: node:20
  script:
    - npm ci
    - npm test

build:
  stage: build
  script:
    - npm run build
  artifacts:
    paths:
      - dist/
```

## When to Use
- GitLab-hosted repositories
- Auto DevOps deployments
- Multi-project pipelines
- Container registry integration

## Step-by-Step
1. Add `.gitlab-ci.yml` to repo root
2. Configure stages and jobs
3. Set up GitLab Runner
4. Push to trigger pipeline

## Dependencies
```bash
# Local runner
gitlab-runner register
```

## Examples
```yaml
deploy:
  stage: deploy
  only:
    - main
  script:
    - kubectl apply -f k8s/
  environment: production
```

## Resources
- [GitLab CI Docs](https://docs.gitlab.com/ee/ci)

## Validation
1. Pipeline starts on commit
2. All stages execute in order
3. Deployments succeed"""
    },
    {
        "name": "terraform-gcp",
        "description": "Provisions GCP infrastructure using Terraform modules for compute, networking, and managed services. Use for GCP infrastructure as code.",
        "category": "devops",
        "tags": ["terraform", "gcp", "infrastructure", "iac", "cloud"],
        "models": ["sonnet", "opus"],
        "template": """# Terraform GCP

> Infrastructure as code for Google Cloud Platform.

## Quick Start
```hcl
provider "google" {
  project = "my-project"
  region  = "us-central1"
}

resource "google_storage_bucket" "data" {
  name     = "my-data-bucket"
  location = "US"
}
```

## When to Use
- GCP resource provisioning
- Multi-cloud infrastructure
- Repeatable environments
- Compliance and policy as code

## Step-by-Step
1. Install Terraform
2. Configure GCP provider
3. Write resource definitions
4. Run: `terraform apply`

## Dependencies
```bash
terraform init
terraform plan
terraform apply
```

## Examples
```hcl
resource "google_compute_instance" "app" {
  name         = "app-server"
  machine_type = "e2-medium"
  zone         = "us-central1-a"

  boot_disk {
    initialize_params { image = "ubuntu-2204-lts" }
  }
}
```

## Resources
- [Terraform GCP Provider](https://registry.terraform.io/providers/hashicorp/google/latest/docs)

## Validation
1. `terraform plan` shows expected changes
2. Resources create successfully
3. `terraform destroy` cleans up"""
    },
    # qa
    {
        "name": "jest",
        "description": "Writes unit and integration tests with Jest, including mocks, snapshots, and code coverage. Use for JavaScript/TypeScript testing.",
        "category": "qa",
        "tags": ["jest", "testing", "javascript", "typescript", "unit-test"],
        "models": ["sonnet", "opus"],
        "template": """# Jest

> Delightful JavaScript testing with built-in mocking and assertions.

## Quick Start
```javascript
// sum.test.js
const sum = (a, b) => a + b;

test('adds 1 + 2 to equal 3', () => {
  expect(sum(1, 2)).toBe(3);
});
```

## When to Use
- Unit and integration tests
- React component testing
- API endpoint testing
- Snapshot testing

## Step-by-Step
1. Install: `npm install --save-dev jest`
2. Add `"test": "jest"` to package.json
3. Write tests in `*.test.js` files
4. Run: `npm test`

## Dependencies
```bash
npm install --save-dev jest @types/jest ts-jest
```

## Examples
```javascript
import axios from 'axios';
jest.mock('axios');

test('fetches users', async () => {
  axios.get.mockResolvedValue({ data: [{ id: 1 }] });
  const users = await fetchUsers();
  expect(users).toHaveLength(1);
});
```

## Resources
- [Jest Docs](https://jestjs.io/docs/getting-started)

## Validation
1. Tests pass with `npm test`
2. Coverage report generates
3. Mocks work correctly"""
    },
    {
        "name": "vitest",
        "description": "Runs fast unit and integration tests with Vitest, featuring Vite-native speed and Jest-compatible API. Use for modern Vite projects.",
        "category": "qa",
        "tags": ["vitest", "testing", "vite", "javascript", "typescript"],
        "models": ["sonnet", "opus"],
        "template": """# Vitest

> Blazing-fast unit test framework powered by Vite.

## Quick Start
```javascript
// sum.test.js
import { describe, it, expect } from 'vitest'

function sum(a, b) { return a + b }

describe('sum', () => {
  it('adds numbers', () => {
    expect(sum(1, 2)).toBe(3)
  })
})
```

## When to Use
- Vite-based projects
- Vue/React/Svelte component testing
- TypeScript-native testing
- Fast feedback development

## Step-by-Step
1. Install: `npm install --save-dev vitest`
2. Add `"test": "vitest"` to package.json
3. Write tests with Jest-compatible API
4. Run: `npm test`

## Dependencies
```bash
npm install --save-dev vitest @vue/test-utils jsdom
```

## Examples
```javascript
import { mount } from '@vue/test-utils'
import Counter from './Counter.vue'

it('increments on click', async () => {
  const wrapper = mount(Counter)
  await wrapper.find('button').trigger('click')
  expect(wrapper.text()).toContain('1')
})
```

## Resources
- [Vitest Guide](https://vitest.dev/guide)

## Validation
1. Tests pass with `vitest run`
2. Watch mode works: `vitest`
3. Coverage generates: `vitest --coverage`"""
    },
    # security
    {
        "name": "sonarqube",
        "description": "Analyzes code quality and security with SonarQube, detecting bugs, vulnerabilities, and code smells. Use for continuous code inspection.",
        "category": "security",
        "tags": ["sonarqube", "code-quality", "static-analysis", "security", "linting"],
        "models": ["sonnet", "opus"],
        "template": """# SonarQube

> Continuous code quality and security inspection platform.

## Quick Start
```bash
docker run -d --name sonarqube -p 9000:9000 sonarqube:community
```

## When to Use
- Code quality gate in CI/CD
- Security vulnerability detection
- Technical debt tracking
- Code review automation

## Step-by-Step
1. Start SonarQube server
2. Generate project token
3. Configure scanner in CI/CD
4. Run: `sonar-scanner`

## Dependencies
```bash
# Using Docker
docker run -d -p 9000:9000 sonarqube:community

# Scanner
sonar-scanner -Dsonar.projectKey=myapp -Dsonar.token=sq...
```

## Examples
```yaml
# .github/workflows/sonarqube.yml
- name: SonarQube Scan
  uses: SonarSource/sonarqube-scan-action@v2
  env:
    SONAR_TOKEN: ${{ secrets.SONAR_TOKEN }}
```

## Resources
- [SonarQube Docs](https://docs.sonarqube.org)

## Validation
1. SonarQube UI loads on port 9000
2. Analysis completes without errors
3. Quality gate passes"""
    },
    # mobile
    {
        "name": "capacitor",
        "description": "Builds cross-platform mobile apps with Capacitor, bridging web apps to native device features. Use for hybrid mobile development.",
        "category": "mobile",
        "tags": ["capacitor", "mobile", "hybrid", "ios", "android"],
        "models": ["sonnet", "opus"],
        "template": """# Capacitor

> Cross-platform native runtime for web apps with access to device APIs.

## Quick Start
```bash
npm install @capacitor/core @capacitor/cli
npx cap init MyApp com.example.myapp
npx cap add ios
npx cap add android
```

## When to Use
- Web to mobile app migration
- Accessing native device features
- Sharing code across platforms
- Progressive Web Apps to stores

## Step-by-Step
1. Build web app (React, Vue, etc.)
2. Add Capacitor: `npx cap init`
3. Add platforms: `npx cap add ios`
4. Sync: `npx cap sync`

## Dependencies
```bash
npm install @capacitor/core @capacitor/cli @capacitor/ios @capacitor/android
```

## Examples
```javascript
import { Camera } from '@capacitor/camera'

const image = await Camera.getPhoto({
  quality: 90,
  resultType: CameraResultType.Uri
})
```

## Resources
- [Capacitor Docs](https://capacitorjs.com/docs)

## Validation
1. App builds for iOS/Android
2. Native features work (camera, etc.)
3. Hot reload works: `npx cap run ios`"""
    },
    # design
    {
        "name": "shadcn-ui",
        "description": "Builds modern UI components with shadcn/ui, a collection of re-usable components built with Radix UI and Tailwind CSS. Use for beautiful, accessible React apps.",
        "category": "design",
        "tags": ["shadcn-ui", "react", "tailwind", "radix", "components"],
        "models": ["sonnet", "opus"],
        "template": """# shadcn/ui

> Beautifully designed components that you can copy and paste into your apps.

## Quick Start
```bash
npx shadcn@latest init
npx shadcn@latest add button card dialog
```

## When to Use
- Building React apps with Tailwind
- Need accessible, styled components
- Rapid UI development
- Consistent design system

## Step-by-Step
1. Init: `npx shadcn@latest init`
2. Add components: `npx shadcn@latest add button`
3. Import and use in your app
4. Customize with Tailwind classes

## Dependencies
```bash
npx shadcn@latest init
npx shadcn@latest add button card input dialog dropdown-menu
```

## Examples
```tsx
import { Button } from "@/components/ui/button"
import { Card, CardContent, CardHeader } from "@/components/ui/card"

export default function Login() {
  return (
    <Card>
      <CardHeader>Welcome Back</CardHeader>
      <CardContent>
        <Button variant="default">Sign In</Button>
      </CardContent>
    </Card>
  )
}
```

## Resources
- [shadcn/ui Docs](https://ui.shadcn.com)

## Validation
1. Components render correctly
2. Dark mode works via class toggle
3. Components are accessible (keyboard, screen reader)"""
    },
]

def create_skill(data):
    path = f'.claude/skills/{data["category"]}/{data["name"]}'
    os.makedirs(path, exist_ok=True)
    
    tags = '[' + ', '.join(data['tags']) + ']'
    models = '[' + ', '.join(data['models']) + ']'
    
    content = f"""---
name: {data['name']}
description: {data['description']}
category: {data['category']}
tags: {tags}
models: {models}
version: 1.0.0
created: 2026-05-14
---
{data['template']}
"""
    with open(f'{path}/SKILL.md', 'w', encoding='utf-8') as f:
        f.write(content.strip() + '\n')
    print(f'  Created {path}/SKILL.md')

print('Creating new skills...')
for skill in NEW_SKILLS:
    create_skill(skill)
print(f'\nDone! Created {len(NEW_SKILLS)} new skills.')
