import os

def sk(name, desc, cat, tags, models, content):
    path = f'.claude/skills/{cat}/{name}'
    os.makedirs(path, exist_ok=True)
    t = '[' + ', '.join(tags) + ']'
    m = '[' + ', '.join(models) + ']'
    with open(f'{path}/SKILL.md', 'w', encoding='utf-8') as f:
        f.write(f"---\nname: {name}\ndescription: {desc}\ncategory: {cat}\ntags: {t}\nmodels: {m}\nversion: 1.0.0\ncreated: 2026-05-14\n---\n{content}\n")
    print(f'  {cat}/{name}')

# === AI ===
sk("anthropic-api", "Integrates Anthropic's Claude API for chat completions, messages, and tool use in applications.", "ai", ["anthropic", "claude", "api", "llm", "messages"], ["sonnet", "opus"], """# Anthropic API
> Build applications with Claude's Messages API and tool use.
## Quick Start
```python
from anthropic import Anthropic
client = Anthropic()
response = client.messages.create(model="claude-sonnet-4-20250514", max_tokens=1024, messages=[{"role": "user", "content": "Hello!"}])
print(response.content[0].text)
```
## Messages with System Prompt
```python
response = client.messages.create(model="claude-sonnet-4-20250514", max_tokens=1024, system="You are a helpful coding assistant.", messages=[{"role": "user", "content": "Write a Python function to sort a list"}])
```
## Tool Use
```python
tools = [{"name": "get_weather", "description": "Get current weather", "input_schema": {"type": "object", "properties": {"location": {"type": "string"}, "unit": {"type": "string", "enum": ["c", "f"]}}, "required": ["location"]}}]
response = client.messages.create(model="claude-sonnet-4-20250514", max_tokens=1024, messages=[...], tools=tools)
```
## When to Use
- Building with Claude models; Tool-use agents; Multi-turn conversations
## Validation
1. API key authenticates; 2. Messages API returns completions; 3. Tool use requests are properly formatted""")

sk("gemini-api", "Integrates Google's Gemini API for text generation, vision, embeddings, and function calling.", "ai", ["gemini", "google", "api", "llm", "multimodal"], ["sonnet", "opus"], """# Gemini API
> Google's multimodal AI model API with text, vision, and code capabilities.
## Quick Start
```python
import google.generativeai as genai
genai.configure(api_key="YOUR_API_KEY")
model = genai.GenerativeModel('gemini-pro')
response = model.generate_content("Explain quantum computing")
print(response.text)
```
## Chat & Vision
```python
chat = model.start_chat(history=[]); response = chat.send_message("Tell me a joke")
import PIL.Image; model = genai.GenerativeModel('gemini-pro-vision')
image = PIL.Image.open('diagram.png'); response = model.generate_content(["Explain this", image])
```
## When to Use
- Multimodal analysis; Code generation; Embeddings; Google Cloud integration
## Validation
1. API key authenticates; 2. Text generation returns content; 3. Vision processes images""")

sk("llama-index", "Builds data-augmented LLM applications with LlamaIndex, including indexing, retrieval, and query engines.", "ai", ["llamaindex", "rag", "llm", "indexing", "retrieval"], ["sonnet", "opus"], """# LlamaIndex
> Data framework for building LLM applications with custom data.
## Quick Start
```python
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
documents = SimpleDirectoryReader('data').load_data()
index = VectorStoreIndex.from_documents(documents)
response = index.as_query_engine().query("What is the main topic?")
```
## Index Types
```python
from llama_index.core import VectorStoreIndex, SummaryIndex, KeywordTableIndex
vector_index = VectorStoreIndex.from_documents(docs)
summary_index = SummaryIndex.from_documents(docs)
keyword_index = KeywordTableIndex.from_documents(docs)
```
## When to Use
- Document Q&A; Custom knowledge bases; RAG pipelines
## Validation
1. Documents index successfully; 2. Query engines return relevant results; 3. Retrieval returns top-k nodes""")

sk("autogen", "Creates multi-agent AI systems with AutoGen, enabling agent conversations, tool use, and group chats.", "ai", ["autogen", "agents", "multi-agent", "conversation", "ai"], ["sonnet", "opus"], """# AutoGen
> Multi-agent conversation framework for building AI agent systems.
## Quick Start
```python
import autogen
config_list = [{"model": "gpt-4", "api_key": "..."}]
assistant = autogen.AssistantAgent(name="assistant", llm_config={"config_list": config_list})
user_proxy = autogen.UserProxyAgent(name="user", human_input_mode="NEVER")
user_proxy.initiate_chat(assistant, message="Write a Python script to fetch stock prices")
```
## Group Chat
```python
group_chat = autogen.GroupChat(agents=[agent1, agent2, agent3], messages=[], max_round=10)
manager = autogen.GroupChatManager(groupchat=group_chat, llm_config={...})
```
## When to Use
- Multi-agent problem-solving; Code generation; Research assistance
## Validation
1. Agents initiate conversations; 2. Tools discovered and called; 3. Group chat reaches consensus""")

sk("crewai", "Orchestrates AI agent teams with CrewAI, role-based agents, tasks, and sequential/parallel workflows.", "ai", ["crewai", "agents", "orchestration", "tasks", "ai"], ["sonnet", "opus"], """# CrewAI
> Framework for orchestrating role-based AI agent teams.
## Quick Start
```python
from crewai import Agent, Task, Crew, Process
researcher = Agent(role='Researcher', goal='Find accurate information', backstory='Expert researcher')
writer = Agent(role='Writer', goal='Write engaging content', backstory='Professional writer')
research = Task(description='Research AI trends', agent=researcher, expected_output='Notes')
write = Task(description='Write blog post about AI', agent=writer, expected_output='Blog post')
crew = Crew(agents=[researcher, writer], tasks=[research, write], process=Process.sequential)
result = crew.kickoff()
```
## When to Use
- Content creation pipelines; Research workflows; Automated report generation
## Validation
1. Agents assigned correct roles; 2. Tasks execute in order; 3. Final output is cohesive""")

sk("haystack", "Builds NLP pipelines with Haystack for document search, QA, and LLM-powered applications.", "ai", ["haystack", "nlp", "search", "qa", "pipelines"], ["sonnet", "opus"], """# Haystack
> NLP framework for building search and QA systems.
## Quick Start
```python
from haystack import Pipeline
from haystack.components.retrievers import InMemoryBM25Retriever
from haystack_integrations.components.generators import OpenAIGenerator
pipeline = Pipeline()
pipeline.add_component("retriever", InMemoryBM25Retriever(top_k=3))
pipeline.add_component("llm", OpenAIGenerator())
pipeline.connect("retriever.documents", "llm.documents")
result = pipeline.run({"retriever": {"query": "What is Haystack?"}})
```
## When to Use
- Document retrieval; QA over custom data; Hybrid search; NLP pipelines
## Validation
1. Pipeline compiles; 2. Retrieval returns relevant docs; 3. LLM generates context-based answers""")

sk("streamlit", "Builds interactive data apps and ML demos with Streamlit, using pure Python widgets and charts.", "ai", ["streamlit", "python", "data-app", "dashboard", "ml"], ["sonnet", "opus"], """# Streamlit
> Turn Python scripts into interactive web apps in seconds.
## Quick Start
```python
import streamlit as st
st.title('My Data App')
name = st.text_input('Enter your name')
if st.button('Say Hello'): st.write(f'Hello, {name}!')
```
## Widgets & Caching
```python
uploaded_file = st.file_uploader("Upload CSV", type=['csv'])
if uploaded_file:
    import pandas as pd; import plotly.express as px
    df = pd.read_csv(uploaded_file); st.dataframe(df)
    fig = px.histogram(df, x=st.selectbox("Column", df.columns)); st.plotly_chart(fig)
@st.cache_data
def load_data(): return pd.read_csv('large.csv')
```
## When to Use
- ML model demos; Data analysis dashboards; Internal tools; Rapid prototyping
## Validation
1. App runs with streamlit run; 2. Widgets update interactively; 3. Charts render correctly""")

sk("gradio", "Creates ML demo interfaces with Gradio, supporting images, text, audio, and video inputs/outputs.", "ai", ["gradio", "python", "ml", "demo", "interactive"], ["sonnet", "opus"], """# Gradio
> Build demo web apps for machine learning models.
## Quick Start
```python
import gradio as gr
def greet(name, intensity): return "Hello " + name + "!" * intensity
demo = gr.Interface(fn=greet, inputs=[gr.Textbox(label="Name"), gr.Slider(1, 5, value=2)], outputs=gr.Textbox())
demo.launch()
```
## Blocks Layout
```python
with gr.Blocks() as demo:
    gr.Markdown("# My App")
    with gr.Row():
        with gr.Column(): input_img = gr.Image(); btn = gr.Button("Process")
        with gr.Column(): output_img = gr.Image()
    btn.click(fn=process, inputs=input_img, outputs=output_img)
```
## When to Use
- ML model demos; Team sharing; User testing; API prototyping
## Validation
1. Interface launches on shareable URL; 2. Input types work; 3. Function returns expected output""")

sk("pinecone", "Manages vector embeddings with Pinecone for semantic search, recommendation, and RAG pipelines.", "ai", ["pinecone", "vector-database", "embeddings", "search", "rag"], ["sonnet", "opus"], """# Pinecone
> Managed vector database for semantic search and RAG.
## Quick Start
```python
from pinecone import Pinecone, ServerlessSpec
pc = Pinecone(api_key="YOUR_API_KEY")
pc.create_index(name="my-index", dimension=384, metric="cosine", spec=ServerlessSpec(cloud="aws", region="us-east-1"))
```
## Indexing & Query
```python
index = pc.Index("my-index")
index.upsert(vectors=[{"id": "doc1", "values": [0.1, 0.2], "metadata": {"text": "Document 1"}}])
results = index.query(vector=query_embedding, top_k=5, include_metadata=True)
```
## When to Use
- Semantic search; RAG vector storage; Recommendation systems
## Validation
1. Index creation succeeds; 2. Upsert operations complete; 3. Query returns relevant results""")

sk("weaviate", "Deploys Weaviate vector database with hybrid search, modules, and GraphQL API.", "ai", ["weaviate", "vector-database", "search", "graphql", "ai"], ["sonnet", "opus"], """# Weaviate
> Open-source vector database with hybrid search and GraphQL API.
## Quick Start
```python
import weaviate
client = weaviate.connect_to_local()
client.collections.create("Document", vectorizer_config=weaviate.classes.config.Configure.Vectorizer.text2vec_openai())
```
## Hybrid Search
```python
collection = client.collections.get("Document")
response = collection.query.hybrid(query="machine learning basics", alpha=0.5, limit=5)
```
## When to Use
- Hybrid search applications; AI-native data management; Knowledge graphs
## Validation
1. Weaviate instance starts; 2. Vectorizer module loads; 3. Hybrid search returns combined results""")

# === SECURITY ===
sk("keycloak", "Configures Keycloak for identity and access management, including SSO, OAuth2, SAML, and user federation.", "security", ["keycloak", "iam", "sso", "oauth2", "authentication"], ["sonnet", "opus"], """# Keycloak
> Open-source identity and access management with SSO.
## Quick Start
```bash
docker run -d -p 8080:8080 -e KEYCLOAK_ADMIN=admin -e KEYCLOAK_ADMIN_PASSWORD=admin quay.io/keycloak/keycloak:latest start-dev
```
## Client Setup
```json
{"clientId": "my-app", "protocol": "openid-connect", "publicClient": true, "redirectUris": ["http://localhost:3000/*"]}
```
## JS Integration
```javascript
const keycloak = new Keycloak({ url: 'http://localhost:8080', realm: 'my-realm', clientId: 'my-app' })
await keycloak.init({ onLoad: 'login-required' })
```
## When to Use
- Centralized authentication; SSO; Multi-tenant identity; Enterprise IAM
## Validation
1. Admin console loads; 2. Users log in via Keycloak; 3. JWT tokens have correct claims""")

sk("auth0", "Integrates Auth0 for authentication, authorization, and user management with social login and MFA.", "security", ["auth0", "authentication", "authorization", "sso", "identity"], ["sonnet", "opus"], """# Auth0
> Authentication and authorization as a service.
## Quick Start
```javascript
import { createAuth0 } from '@auth0/auth0-vue'
const app = createApp(App)
app.use(createAuth0({ domain: 'YOUR_DOMAIN.auth0.com', clientId: 'YOUR_CLIENT_ID', authorizationParams: { redirect_uri: window.location.origin } }))
```
## Login & API Protection
```javascript
const { loginWithRedirect, logout, user, isAuthenticated, getAccessTokenSilently } = useAuth0()
const handleLogin = () => loginWithRedirect({ authorizationParams: { screen_hint: 'signup' } })
const token = await getAccessTokenSilently()
const response = await fetch('/api/protected', { headers: { Authorization: Bearer ${token} } })
```
## When to Use
- Social login (Google, GitHub); Enterprise SSO; MFA; User management
## Validation
1. Auth0 tenant configures correctly; 2. Login flow redirects; 3. API tokens authenticate""")

sk("cert-manager", "Manages TLS certificates in Kubernetes with cert-manager, Let's Encrypt, and auto-renewal.", "security", ["cert-manager", "tls", "kubernetes", "lets-encrypt", "certificates"], ["sonnet", "opus"], """# cert-manager
> Automated certificate management for Kubernetes.
## Quick Start
```bash
kubectl apply -f https://github.com/cert-manager/cert-manager/releases/download/v1.15.0/cert-manager.yaml
```
## Issuer & Certificate
```yaml
apiVersion: cert-manager.io/v1; kind: ClusterIssuer; metadata: { name: letsencrypt-prod }
spec:
  acme: { server: https://acme-v02.api.letsencrypt.org/directory, email: admin@example.com, privateKeySecretRef: { name: letsencrypt-prod-key }, solvers: [{ http01: { ingress: { class: nginx } } }] }
---
apiVersion: cert-manager.io/v1; kind: Certificate; metadata: { name: example-com-tls }
spec: { secretName: example-com-tls, issuerRef: { name: letsencrypt-prod, kind: ClusterIssuer }, dnsNames: [example.com] }
```
## When to Use
- Automatic TLS in Kubernetes; Let's Encrypt; Multi-domain certs
## Validation
1. cert-manager pods are running; 2. Certificate becomes Ready=True; 3. TLS secret created""")

sk("secrets-vault", "Manages secrets with HashiCorp Vault for dynamic secrets, encryption, and access policies.", "security", ["vault", "secrets", "hashicorp", "encryption", "security"], ["sonnet", "opus"], """# HashiCorp Vault
> Secrets management, encryption, and access control.
## Quick Start
```bash
vault server -dev; export VAULT_ADDR='http://127.0.0.1:8200'; vault login <root-token>
```
## KV & Dynamic Secrets
```bash
vault secrets enable -path=secret kv-v2
vault kv put secret/myapp/config api_key=abc123
vault write database/config/my-db plugin_name=postgresql-database-plugin allowed_roles="readonly" connection_url="postgresql://..."
```
## Policies
```hcl
path "secret/data/myapp/*" { capabilities = ["read", "list"] }
```
## When to Use
- API key storage; Dynamic database credentials; Encryption as a service
## Validation
1. Vault unseals; 2. Secrets read/write correctly; 3. Policies enforce access control""")

sk("ssl-tls", "Configures SSL/TLS certificates for web servers, including Let's Encrypt, certbot, and HTTPS hardening.", "security", ["ssl", "tls", "https", "certificates", "encryption"], ["sonnet", "opus"], """# SSL/TLS
> Secure communication with SSL/TLS certificates.
## Quick Start
```bash
sudo certbot --nginx -d example.com -d www.example.com
sudo certbot renew
```
## Nginx HTTPS
```nginx
listen 443 ssl http2; server_name example.com;
ssl_certificate /etc/letsencrypt/live/example.com/fullchain.pem;
ssl_certificate_key /etc/letsencrypt/live/example.com/privkey.pem;
ssl_protocols TLSv1.2 TLSv1.3;
add_header Strict-Transport-Security "max-age=63072000" always;
```
## When to Use
- HTTPS enforcement; Certificate lifecycle; Security compliance
## Validation
1. SSL Labs test gets A+; 2. Certificate not expired; 3. HTTP to HTTPS redirect works""")

sk("waf", "Configures Web Application Firewall protection with ModSecurity, CRS rules, and blocking policies.", "security", ["waf", "modsecurity", "firewall", "rules", "protection"], ["sonnet", "opus"], """# WAF (Web Application Firewall)
> Protect web applications from common attacks.
## Quick Start
```bash
sudo apt-get install libnginx-mod-modsecurity
sudo cp /etc/modsecurity/modsecurity.conf-recommended /etc/modsecurity/modsecurity.conf
```
## OWASP CRS & Custom Rules
```conf
Include /etc/modsecurity/crs/crs-setup.conf.example
Include /etc/modsecurity/crs/rules/*.conf
SecRule ARGS "@detectSQLi" "id:1000,phase:2,deny,status:403,msg:'SQL Injection blocked'"
SecRule ARGS "@detectXSS" "id:1001,phase:2,deny,status:403,msg:'XSS blocked'"
SecRule IP:REQUEST_RATE "@gt 100" "id:2000,phase:2,deny,status:429,msg:'Rate limit exceeded'"
```
## When to Use
- Production web app protection; PCI DSS; OWASP Top 10; DDoS mitigation
## Validation
1. ModSecurity loads; 2. Attack payloads blocked (403); 3. Legitimate traffic passes""")

sk("snyk", "Scans dependencies, containers, and IaC for vulnerabilities with Snyk in CI/CD pipelines.", "security", ["snyk", "vulnerability", "dependencies", "security-scanning", "ci-cd"], ["sonnet", "opus"], """# Snyk
> Developer security platform for vulnerability scanning.
## Quick Start
```bash
npm install -g snyk; snyk auth; snyk test; snyk monitor
```
## Scanning Types
```bash
snyk test --all-projects          # Node.js / npm
snyk container test node:20        # Docker images
snyk iac test main.tf              # Terraform IaC
snyk test --severity-threshold=high # Only high/critical
```
## CI/CD Integration
```yaml
- name: Snyk Scan
  uses: snyk/actions/node@master
  env: { SNYK_TOKEN: ${{ secrets.SNYK_TOKEN }} }
  with: { args: --severity-threshold=high }
```
## When to Use
- Open source scanning; Container scanning; IaC validation; License compliance
## Validation
1. snyk test finds vulnerabilities; 2. Fix PRs generated; 3. IaC scanning detects misconfigs""")

# === QA ===
sk("pytest", "Writes Python tests with pytest, including fixtures, parameterization, and plugins for coverage.", "qa", ["pytest", "python", "testing", "fixtures", "unit-test"], ["sonnet", "opus"], """# Pytest
> Python testing framework with fixtures and parameterized tests.
## Quick Start
```python
def test_add(): assert 1 + 1 == 2
def test_subtract(): assert 3 - 1 == 2
```
```bash
pytest test_calc.py -v
```
## Fixtures & Parameterization
```python
import pytest
@pytest.fixture
def db_connection(): conn = create_database(); yield conn; conn.close()
@pytest.mark.parametrize("input,expected", [(1, 2), (2, 4), (3, 6)])
def test_double(input, expected): assert input * 2 == expected
```
## When to Use
- Python unit tests; API testing; Data pipeline validation; TDD
## Validation
1. pytest discovers all tests; 2. Fixtures setup/teardown correctly; 3. Coverage reports""")

sk("puppeteer", "Automates browser testing with Puppeteer, headless Chrome, and page interaction APIs.", "qa", ["puppeteer", "browser", "automation", "testing", "headless"], ["sonnet", "opus"], """# Puppeteer
> Browser automation library for Node.js with headless Chrome.
## Quick Start
```javascript
import puppeteer from 'puppeteer'
const browser = await puppeteer.launch(); const page = await browser.newPage()
await page.goto('https://example.com'); await page.screenshot({ path: 'screenshot.png' })
await browser.close()
```
## Page Interaction
```javascript
await page.goto('https://example.com/login')
await page.type('#email', 'user@example.com'); await page.click('#submit')
await page.waitForNavigation(); const title = await page.title()
```
## When to Use
- Automated screenshots; PDF generation; E2E testing; Web scraping
## Validation
1. Browser launches headless; 2. Page interactions work; 3. Screenshots capture correctly""")

sk("detox", "Tests React Native applications E2E with Detox, gray box testing, and device synchronization.", "qa", ["detox", "react-native", "e2e", "mobile-testing", "automation"], ["sonnet", "opus"], """# Detox
> Gray-box E2E testing for React Native apps.
## Quick Start
```javascript
describe('Login', () => {
  beforeAll(async () => { await device.launchApp() })
  it('should login successfully', async () => {
    await element(by.id('email-input')).typeText('user@example.com')
    await element(by.id('password-input')).typeText('password123')
    await element(by.id('login-button')).tap()
    await expect(element(by.id('welcome-screen'))).toBeVisible()
  })
})
```
## When to Use
- React Native E2E testing; CI/CD mobile testing; Cross-platform tests
## Validation
1. Detox builds the app correctly; 2. Tests run on simulator; 3. Element matching works""")

sk("locust", "Performs load testing with Locust, Python-based distributed testing, and real-time web UI.", "qa", ["locust", "load-testing", "python", "performance", "stress-test"], ["sonnet", "opus"], """# Locust
> Distributed load testing framework in Python.
## Quick Start
```python
from locust import HttpUser, task, between
class WebsiteUser(HttpUser):
    wait_time = between(1, 3)
    @task(5)
    def browse(self): self.client.get("/products")
    @task(1)
    def checkout(self): self.client.post("/checkout", json={"item": "book"})
```
```bash
locust -f locustfile.py --web-host localhost
```
## When to Use
- API load testing; Performance regression; Capacity planning; Spike testing
## Validation
1. Locust UI shows metrics; 2. RPS displays correctly; 3. Test stops and reports""")

sk("cucumber", "Implements Behavior-Driven Development with Cucumber, Gherkin scenarios, and step definitions.", "qa", ["cucumber", "bdd", "gherkin", "testing", "acceptance"], ["sonnet", "opus"], """# Cucumber
> BDD testing with Gherkin scenarios and step definitions.
## Quick Start
```gherkin
Feature: User Login
  Scenario: Successful login
    Given I am on the login page
    When I enter "user@example.com" as email
    And I enter "password123" as password
    And I click "Sign In"
    Then I should see the dashboard
```
## Step Definitions
```javascript
const { Given, When, Then } = require('@cucumber/cucumber')
Given('I am on the login page', async function () { await this.page.goto('https://example.com/login') })
Then('I should see the dashboard', async function () { await expect(this.page.locator('#dashboard')).toBeVisible() })
```
## When to Use
- Business-readable tests; ATDD; Cross-team communication; Living documentation
## Validation
1. Features parse without errors; 2. All scenarios pass; 3. Reports with pass/fail status""")

sk("artillery", "Load tests APIs and applications with Artillery, supporting HTTP, WebSocket, and Socket.io.", "qa", ["artillery", "load-testing", "performance", "http", "websocket"], ["sonnet", "opus"], """# Artillery
> Cloud-scale load testing with YAML configuration.
## Quick Start
```yaml
config:
  target: "https://api.example.com"
  phases: [{ duration: 60, arrivalRate: 5, rampTo: 20, name: "Warm up" }]
scenarios:
  - flow:
      - get: { url: "/api/users" }
      - post: { url: "/api/users", json: { name: "Alice" } }
```
```bash
artillery run config.yaml
```
## WebSocket Testing
```yaml
scenarios:
  - engine: "ws"
    flow: [{ connect: "ws://localhost:8080" }, { send: '{"event": "join", "room": "general"}' }]
```
## When to Use
- API load testing; WebSocket perf testing; CI/CD performance gates
## Validation
1. Artillery runs and produces metrics; 2. Response times tracked; 3. p50/p95/p99 shown""")

# === DESIGN ===
sk("radix-ui", "Builds accessible React UI primitives with Radix UI, including dialogs, dropdowns, and tooltips.", "design", ["radix-ui", "react", "accessibility", "headless", "components"], ["sonnet", "opus"], """# Radix UI
> Headless React UI primitives with full accessibility support.
## Quick Start
```bash
npm install @radix-ui/react-dialog @radix-ui/react-dropdown-menu @radix-ui/react-tooltip
```
## Dialog
```tsx
import * as Dialog from '@radix-ui/react-dialog'
<Dialog.Root><Dialog.Trigger asChild><button>Open</button></Dialog.Trigger>
<Dialog.Portal><Dialog.Overlay /><Dialog.Content>
  <Dialog.Title>Edit Profile</Dialog.Title>
  <Dialog.Close asChild><button>Close</button></Dialog.Close>
</Dialog.Content></Dialog.Portal></Dialog.Root>
```
## When to Use
- Accessible components; Custom design systems; ARIA-compliant UIs
## Validation
1. Keyboard navigation works; 2. Screen reader announces roles; 3. Focus management correct""")

sk("ant-design", "Builds enterprise UIs with Ant Design, including pre-built components, theming, and i18n support.", "design", ["ant-design", "react", "ui-library", "enterprise", "components"], ["sonnet", "opus"], """# Ant Design
> Enterprise UI design system with React components.
## Quick Start
```tsx
import { Button, DatePicker, Table, Space } from 'antd'
export default function App() {
  return <Space><Button type="primary">Search</Button><DatePicker /></Space>
}
```
## Theming
```tsx
import { ConfigProvider } from 'antd'
<ConfigProvider theme={{ token: { colorPrimary: '#00b96b', borderRadius: 6 } }}>
  <App />
</ConfigProvider>
```
## When to Use
- Enterprise dashboards; Admin panels; Data-heavy interfaces
## Validation
1. Components render without errors; 2. Theme tokens apply; 3. Pagination and sorting work""")

sk("framer-motion", "Creates animations in React with Framer Motion, including layout, gesture, and scroll animations.", "design", ["framer-motion", "animation", "react", "gestures", "ui"], ["sonnet", "opus"], """# Framer Motion
> Production-ready animation library for React.
## Quick Start
```bash
npm install framer-motion
```
```tsx
import { motion } from 'framer-motion'
<motion.div initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} exit={{ opacity: 0, scale: 0.5 }}>Content</motion.div>
```
## Gestures & Layout
```tsx
<motion.div whileHover={{ scale: 1.1 }} whileTap={{ scale: 0.9 }} drag="x" dragConstraints={{ left: -100, right: 100 }} />
<AnimatePresence mode="wait">{selected && <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }} exit={{ opacity: 0 }} />}</AnimatePresence>
```
## When to Use
- UI micro-interactions; Page transitions; Gesture-based interactions; Scroll animations
## Validation
1. Animations play without jank; 2. Gestures respond to input; 3. AnimatePresence handles mount/unmount""")

sk("threejs", "Creates 3D graphics on the web with Three.js, including scenes, cameras, animations, and WebGL.", "design", ["threejs", "3d", "webgl", "graphics", "animation"], ["sonnet", "opus"], """# Three.js
> 3D JavaScript library for the web with WebGL.
## Quick Start
```javascript
import * as THREE from 'three'
const scene = new THREE.Scene(); const camera = new THREE.PerspectiveCamera(75, innerWidth/innerHeight, 0.1, 1000)
const renderer = new THREE.WebGLRenderer(); renderer.setSize(innerWidth, innerHeight); document.body.appendChild(renderer.domElement)
const cube = new THREE.Mesh(new THREE.BoxGeometry(1,1,1), new THREE.MeshStandardMaterial({ color: 0x00ff00 }))
scene.add(cube); camera.position.z = 5
function animate() { requestAnimationFrame(animate); cube.rotation.x += 0.01; renderer.render(scene, camera) }
animate()
```
## When to Use
- 3D product viewers; Interactive visualizations; Game-like web experiences
## Validation
1. Scene renders without WebGL errors; 2. Animations run at 60fps; 3. Lighting affects materials""")

sk("color-system", "Designs color systems and design tokens for consistent UI theming across light and dark modes.", "design", ["color", "design-tokens", "theming", "accessibility", "ui"], ["sonnet", "opus"], """# Color System
> Designing scalable color systems for UI theming.
## Quick Start
```css
:root { --gray-50: #f9fafb; --gray-500: #6b7280; --gray-900: #111827; --primary-500: #3b82f6; --color-success: #10b981; --color-warning: #f59e0b; --color-error: #ef4444; }
[data-theme="dark"] { --gray-50: #1e293b; --gray-500: #64748b; --gray-900: #f8fafc; }
```
## WCAG Requirements
- AA Normal text: 4.5:1; AA Large text: 3:1; AAA Normal text: 7:1
## When to Use
- Design system foundations; Dark mode theming; Accessibility compliance
## Validation
1. Token pairs meet WCAG AA; 2. Dark mode switches smoothly; 3. Semantic tokens consistently used""")

sk("typography-system", "Creates scalable typography systems with type scale, line height, and responsive text tokens.", "design", ["typography", "fonts", "design-tokens", "responsive", "type-scale"], ["sonnet", "opus"], """# Typography System
> Building consistent type scales and typography tokens.
## Quick Start
```css
:root { --text-xs: 0.75rem; --text-sm: 0.875rem; --text-base: 1rem; --text-lg: 1.125rem; --text-xl: 1.25rem; --text-2xl: 1.5rem; --text-3xl: 1.875rem; --text-4xl: 2.25rem; --leading-tight: 1.25; --leading-normal: 1.5; --font-normal: 400; --font-bold: 700; }
```
## Text Styles
```css
.heading-1 { font-size: var(--text-4xl); font-weight: var(--font-bold); line-height: var(--leading-tight); }
.body { font-size: var(--text-base); font-weight: var(--font-normal); line-height: var(--leading-normal); }
```
## When to Use
- Design system foundations; Responsive typography; Brand consistency
## Validation
1. Type scale maintains consistent ratio; 2. Text meets WCAG size requirements; 3. Responsive sizes adapt""")

# === PRODUCT ===
sk("okr", "Defines Objectives and Key Results (OKRs) for product teams, including goal setting and progress tracking.", "product", ["okr", "goals", "metrics", "product", "objectives"], ["sonnet", "opus"], """# OKR (Objectives & Key Results)
> Goal-setting framework for product and engineering teams.
## Quick Start
```markdown
Objective: Deliver a world-class onboarding experience
KR1: Increase 7-day retention from 40% to 60%
KR2: Reduce time-to-value from 5 days to 1 day
KR3: Achieve NPS score of 50+ for onboarding
```
## Writing Good KRs
Bad: "Improve app performance" | Good: "Reduce P95 latency from 800ms to 200ms"
## When to Use
- Quarterly planning; Team alignment; Performance tracking; Strategy execution
## Validation
1. KRs are measurable with targets; 2. Progress tracked weekly; 3. Objectives are aspirational""")

sk("product-analytics", "Implements product analytics with Mixpanel, Amplitude, or PostHog for user behavior tracking.", "product", ["analytics", "mixpanel", "amplitude", "product", "metrics"], ["sonnet", "opus"], """# Product Analytics
> User behavior analytics for product decisions.
## Quick Start (PostHog)
```javascript
import posthog from 'posthog-js'
posthog.init('YOUR_API_KEY', { api_host: 'https://app.posthog.com' })
posthog.capture('signup_completed', { plan: 'premium' })
posthog.identify('user_123', { email: 'alice@example.com' })
```
## Event Taxonomy
```javascript
[Object] [Action] [Context] — e.g., Project Created, Task Completed
Properties: user attributes, timestamps, device info
```
## Funnel Analysis
```javascript
const funnel = [{ event: 'app_opened' }, { event: 'signup_started' }, { event: 'signup_completed' }]
```
## When to Use
- User behavior understanding; Funnel optimization; Feature adoption; Retention analysis
## Validation
1. Events fire correctly in dev tools; 2. Funnel shows drop-offs; 3. User properties captured""")

sk("aarrr-metrics", "Tracks startup growth metrics using the AARRR (Pirate Metrics) framework: Acquisition, Activation, Retention, Revenue, Referral.", "product", ["aarrr", "pirate-metrics", "growth", "saas", "metrics"], ["sonnet", "opus"], """# AARRR Pirate Metrics
> Growth framework for tracking user journey from acquisition to referral.
## Quick Start
```markdown
Acquisition: Users who visit → 10,000
Activation: Complete onboarding → 25% → 2,500
Retention: Return after 7 days → 40% → 1,000
Revenue: Pay for subscription → 10% → 100
Referral: Invite others → 20% → 20
```
## When to Use
- Startup growth tracking; Funnel optimization; Product-market fit; Growth strategy
## Validation
1. Each metric has clear definition; 2. Funnel shows biggest drop-offs; 3. Actions tied to stages""")

# === IOT ===
sk("raspberry-pi", "Configures and deploys applications on Raspberry Pi, including GPIO, camera, and headless setup.", "iot", ["raspberry-pi", "gpio", "python", "embedded", "linux"], ["sonnet", "opus"], """# Raspberry Pi
> Single-board computer for embedded projects and IoT.
## Quick Start
```bash
# Enable SSH & WiFi on fresh SD card
touch /boot/ssh
cat > /boot/wpa_supplicant.conf << EOF
network={ ssid="MyWiFi" psk="mypassword" }
EOF
```
## GPIO Python
```python
import RPi.GPIO as GPIO; import time
GPIO.setmode(GPIO.BCM); GPIO.setup(18, GPIO.OUT); GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
while True:
    if GPIO.input(23) == GPIO.LOW: GPIO.output(18, GPIO.HIGH); time.sleep(1); GPIO.output(18, GPIO.LOW)
```
## When to Use
- IoT sensor projects; Home automation; Media centers; Robotics
## Validation
1. Pi boots and SSH accessible; 2. GPIO Python scripts work; 3. Camera captures images""")

sk("home-assistant", "Automates smart home devices with Home Assistant, integrations, automations, and custom dashboards.", "iot", ["home-assistant", "smart-home", "automation", "iot", "dashboard"], ["sonnet", "opus"], """# Home Assistant
> Open-source home automation platform.
## Quick Start
```bash
docker run -d --name home-assistant -p 8123:8123 -v ./config:/config ghcr.io/home-assistant/home-assistant:stable
```
## Automations
```yaml
automation:
  - alias: "Turn on lights at sunset"
    trigger: [{ platform: sun, event: sunset }]
    action: [{ service: light.turn_on, target: { entity_id: "light.living_room" }, data: { brightness: 200 } }]
```
## When to Use
- Smart home integration; Automated routines; Energy monitoring
## Validation
1. UI loads on port 8123; 2. Devices discovered; 3. Automations trigger correctly""")

sk("esp-idf", "Programs ESP32 microcontrollers using ESP-IDF framework with FreeRTOS, Wi-Fi, and Bluetooth.", "iot", ["esp-idf", "esp32", "freertos", "embedded", "c"], ["sonnet", "opus"], """# ESP-IDF
> Official development framework for ESP32 microcontrollers.
## Quick Start
```bash
git clone --recursive https://github.com/espressif/esp-idf.git
cd esp-idf && ./install.sh && . ./export.sh
idf.py create-project my_project; idf.py set-target esp32; idf.py build flash monitor
```
## Wi-Fi & GPIO
```c
#include "esp_wifi.h"; #include "driver/gpio.h"
void wifi_init_sta(void) { esp_netif_init(); esp_event_loop_create_default(); esp_netif_create_default_wifi_sta(); wifi_init_config_t cfg = WIFI_INIT_CONFIG_DEFAULT(); esp_wifi_init(&cfg); }
gpio_set_direction(GPIO_NUM_2, GPIO_MODE_OUTPUT); gpio_set_level(GPIO_NUM_2, 1);
```
## When to Use
- Advanced ESP32 projects; Wi-Fi/Bluetooth apps; IoT gateways
## Validation
1. Firmware builds; 2. Device connects to Wi-Fi; 3. GPIO outputs change state""")

sk("node-red", "Creates IoT and automation flows with Node-RED, visual programming for event-driven applications.", "iot", ["node-red", "flow-based", "iot", "automation", "visual-programming"], ["sonnet", "opus"], """# Node-RED
> Flow-based visual programming for IoT and automation.
## Quick Start
```bash
npm install -g node-red && node-red
# UI at http://localhost:1880
```
## Function Node (JavaScript)
```javascript
msg.payload = { temperature: (msg.payload.temp * 9/5) + 32, unit: "F", timestamp: Date.now() }
return msg;
```
## Flow Components
- Inject: Trigger events; Function: JS transformation; MQTT: Pub/sub; HTTP: REST endpoints; Dashboard: UI widgets
## When to Use
- Visual IoT pipelines; MQTT message processing; Home automation; API integrations
## Validation
1. Editor loads in browser; 2. Deployed flow executes; 3. Debug panel shows messages""")

# === GAMEDEV ===
sk("blender", "Creates 3D models, animations, and scenes in Blender using Python scripting and the bpy module.", "gamedev", ["blender", "3d-modeling", "animation", "python", "bpy"], ["sonnet", "opus"], """# Blender
> Open-source 3D creation suite with Python API.
## Quick Start
```python
import bpy
bpy.ops.mesh.primitive_cube_add(size=2, location=(0, 0, 0))
mat = bpy.data.materials.new(name="Red")
mat.use_nodes = True; mat.node_tree.nodes["Principled BSDF"].inputs[0].default_value = (1, 0, 0, 1)
bpy.context.object.data.materials.append(mat)
```
## Animation
```python
obj = bpy.context.object; obj.location = (0, 0, 0); obj.keyframe_insert(data_path="location", frame=1)
obj.location = (5, 0, 0); obj.keyframe_insert(data_path="location", frame=50)
```
## When to Use
- 3D asset creation for games; Procedural content generation; Automated modeling
## Validation
1. Scripts execute in Blender; 2. Mesh creation correct; 3. Keyframes animate""")

sk("procedural-gen", "Generates game content algorithmically with procedural generation techniques for terrains, dungeons, and textures.", "gamedev", ["procedural-generation", "gamedev", "terrain", "algorithms", "content"], ["sonnet", "opus"], """# Procedural Generation
> Algorithmic content creation for games.
## Quick Start (Terrain)
```python
import noise, numpy as np
def generate_heightmap(width, height, scale=10.0, octaves=6):
    terrain = np.zeros((width, height))
    for x in range(width):
        for z in range(height):
            terrain[x][z] = noise.pnoise2(x/scale, z/scale, octaves=octaves, repeatx=1024, repeaty=1024, base=42)
    return terrain
```
## Dungeon Generation (BSP)
```python
def generate_dungeon(width, height, min_room=5):
    grid = [[1] * width for _ in range(height)]
    rooms = []
    def split(x, y, w, h, depth=0):
        if depth > 3 or (w < min_room*2 and h < min_room*2):
            rw, rh = random.randint(min_room, w-2), random.randint(min_room, h-2)
            rx, ry = x + random.randint(1, w-rw-1), y + random.randint(1, h-rh-1)
            for ry in range(ry, ry+rh):
                for rx in range(rx, rx+rw): grid[ry][rx] = 0
            return
        split_h = random.choice([True, False])
        if split_h: split(x, y, w, h//2, depth+1); split(x, y+h//2, w, h-h//2, depth+1)
    split(0, 0, width, height); return grid, rooms
```
## When to Use
- Infinite worlds; Roguelike dungeons; Texture/terrain creation; Level design
## Validation
1. Generated content playable; 2. Parameters produce varied output; 3. Performance acceptable""")

# === DESKTOP ===
sk("pyqt", "Creates desktop applications with PyQt6, Qt Widgets, signals/slots, and Qt Designer.", "desktop", ["pyqt", "qt", "desktop", "python", "gui"], ["sonnet", "opus"], """# PyQt6
> Python bindings for Qt desktop application framework.
## Quick Start
```python
import sys; from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel
class MainWindow(QWidget):
    def __init__(self):
        super().__init__(); self.setWindowTitle("My App"); layout = QVBoxLayout()
        self.label = QLabel("Hello!"); button = QPushButton("Click Me"); button.clicked.connect(self.on_click)
        layout.addWidget(self.label); layout.addWidget(button); self.setLayout(layout)
    def on_click(self): self.label.setText("Clicked!")
app = QApplication(sys.argv); w = MainWindow(); w.show(); sys.exit(app.exec())
```
## When to Use
- Cross-platform desktop apps; Data analysis tools with GUI; Internal business apps
## Validation
1. Window displays all widgets; 2. Signals/slots work; 3. Layouts resize correctly""")

sk("flutter-desktop", "Builds desktop applications with Flutter for Windows, macOS, and Linux from a single codebase.", "desktop", ["flutter", "desktop", "cross-platform", "dart", "gui"], ["sonnet", "opus"], """# Flutter Desktop
> Build native desktop apps for Windows, macOS, and Linux.
## Quick Start
```bash
flutter create --platforms=windows,macos,linux my_desktop_app
cd my_desktop_app && flutter run -d windows
```
## Window Management
```dart
import 'package:window_manager/window_manager'
void main() async {
  WidgetsFlutterBinding.ensureInitialized(); await windowManager.ensureInitialized()
  await windowManager.setSize(const Size(1280, 800)); await windowManager.setTitle('My App')
  runApp(MyApp())
}
```
## When to Use
- Cross-platform desktop apps; Material Design desktop; Existing Flutter mobile to desktop
## Validation
1. App builds for all platforms; 2. Window size settings apply; 3. Platform channels work""")

# === BLOCKCHAIN ===
sk("hardhat", "Develops, tests, and deploys Ethereum smart contracts with Hardhat, including local node and debugging.", "block", ["hardhat", "ethereum", "smart-contracts", "solidity", "testing"], ["sonnet", "opus"], """# Hardhat
> Ethereum development environment for smart contracts.
## Quick Start
```bash
npm install --save-dev hardhat
npx hardhat init
npx hardhat node     # Local Ethereum node
npx hardhat test     # Run tests
```
## Hardhat Config
```javascript
require("@nomicfoundation/hardhat-toolbox")
module.exports = { solidity: "0.8.20", networks: { hardhat: { chainId: 1337 } } }
```
## Testing with Hardhat
```javascript
const { expect } = require("chai")
describe("Token", function () {
  it("should deploy correctly", async function () {
    const Token = await ethers.getContractFactory("Token")
    const token = await Token.deploy()
    expect(await token.totalSupply()).to.equal(ethers.utils.parseEther("1000000"))
  })
})
```
## When to Use
- Ethereum smart contract development; Testing; Local blockchain simulation
## Validation
1. hardhat node starts; 2. Contracts compile; 3. Tests pass""")

sk("ethersjs", "Interacts with Ethereum blockchain using ethers.js library for transactions, contracts, and accounts.", "block", ["ethersjs", "web3", "ethereum", "transactions", "contracts"], ["sonnet", "opus"], """# ethers.js
> JavaScript library for interacting with Ethereum blockchain.
## Quick Start
```javascript
import { ethers } from 'ethers'
const provider = new ethers.JsonRpcProvider('https://mainnet.infura.io/v3/YOUR_KEY')
const balance = await provider.getBalance('vitalik.eth')
console.log(ethers.formatEther(balance))
```
## Smart Contract Interaction
```javascript
const contract = new ethers.Contract(contractAddress, abi, signer)
const tx = await contract.transfer('0x...', ethers.parseEther('1.0'))
await tx.wait()
```
## When to Use
- DApp frontend development; Transaction signing; Contract interaction
## Validation
1. Provider connects; 2. Contract calls return data; 3. Transactions send correctly""")

# === PAYMENTS ===
sk("paddle", "Integrates Paddle for SaaS payment processing, subscriptions, and checkout management.", "payments", ["paddle", "payments", "subscriptions", "saas", "billing"], ["sonnet", "opus"], """# Paddle
> SaaS payment platform for global subscription billing.
## Quick Start
```javascript
import { initializePaddle } from '@paddle/paddle-js'
const paddle = await initializePaddle({ token: 'YOUR_CLIENT_TOKEN', environment: 'sandbox' })
paddle.Checkout.open({ items: [{ priceId: 'pri_123', quantity: 1 }] })
```
## Webhooks
```javascript
app.post('/webhooks/paddle', express.raw({type: 'application/json'}), (req, res) => {
  const event = req.body
  if (event.event_type === 'transaction.completed') {
    // Fulfill order
  }
  res.send('OK')
})
```
## When to Use
- SaaS subscription billing; Global payments; Tax and compliance handling
## Validation
1. Checkout opens correctly; 2. Webhook events received; 3. Subscription lifecycle works""")

print(f'Batch 2 complete: 32 skills created')
