import os

skills = [
    ("aspnet-core", "Builds web APIs and applications with ASP.NET Core, controllers, Entity Framework, and middleware.", "backend", ["aspnet", "dotnet", "csharp", "web-api", "entity-framework"], ["sonnet", "opus"], """# ASP.NET Core
> Cross-platform framework for building modern web apps with .NET.
## Quick Start
```csharp
var builder = WebApplication.CreateBuilder(args); builder.Services.AddControllers();
var app = builder.Build(); app.MapControllers(); app.Run();
[ApiController, Route("api/[controller]")]
public class UsersController : ControllerBase {
    [HttpGet] public IActionResult GetUsers() => Ok(new[] { new { Id = 1, Name = "Alice" } });
}
```
## When to Use
- Enterprise .NET APIs; Microservices; Cross-platform C# applications
## Validation
1. Server starts; 2. Endpoints return correct data; 3. EF Core queries execute"""),
    ("bootstrap", "Creates responsive, mobile-first websites with Bootstrap, grid system, components, and utilities.", "frontend", ["bootstrap", "css", "responsive", "ui", "framework"], ["sonnet", "opus"], """# Bootstrap
> Most popular CSS framework for responsive, mobile-first sites.
## Quick Start
```html
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3/dist/css/bootstrap.min.css" rel="stylesheet">
<div class="container"><div class="row"><div class="col-md-6">Left</div><div class="col-md-6">Right</div></div></div>
```
## Components
```html
<button class="btn btn-primary">Primary</button>
<div class="card"><div class="card-body"><h5 class="card-title">Card</h5></div></div>
<nav class="navbar navbar-expand-lg navbar-light bg-light">...</nav>
```
## When to Use
- Rapid prototyping; Marketing sites; Admin dashboards; Responsive layouts
## Validation
1. Grid system responsive; 2. Components render correctly; 3. Utilities apply"""),
    ("xamarin", "Builds native mobile apps with Xamarin and .NET MAUI, sharing C# code across iOS, Android, and Windows.", "mobile", ["xamarin", "dotnet", "mobile", "csharp", "maui"], ["sonnet", "opus"], """# Xamarin / .NET MAUI
> Build native cross-platform apps with .NET and C#.
## Quick Start
```xml
<ContentPage xmlns="http://schemas.microsoft.com/dotnet/2021/maui" x:Class="MyApp.MainPage">
  <VerticalStackLayout Padding="30">
    <Label Text="Hello, MAUI!" FontSize="32" />
    <Button Text="Click Me" Clicked="OnButtonClicked" />
  </VerticalStackLayout>
</ContentPage>
```
```csharp
public partial class MainPage : ContentPage {
    int count = 0;
    private void OnButtonClicked(object sender, EventArgs e) => count++;
}
```
## When to Use
- .NET cross-platform mobile apps; Enterprise C# mobile; Code sharing
## Validation
1. App builds for all platforms; 2. UI renders correctly; 3. Platform-specific code works"""),
    ("packer", "Creates identical machine images for multiple platforms with Packer, including AWS AMIs and Docker images.", "devops", ["packer", "images", "ami", "iac", "immutable"], ["sonnet", "opus"], """# Packer
> Build automated machine images for multiple platforms.
## Quick Start
```hcl
source "amazon-ebs" "ubuntu" {
  ami_name = "my-app-{{timestamp}}"; instance_type = "t2.micro"; region = "us-east-1"
  source_ami_filter { filters = { virtualization-type = "hvm", name = "ubuntu/images/*ubuntu-jammy-*" }; owners = ["099720109477"] }
  ssh_username = "ubuntu"
}
build { sources = ["source.amazon-ebs.ubuntu"]; provisioner "shell" { inline = ["sudo apt-get update", "sudo apt-get install -y nginx"] } }
```
## When to Use
- Golden AMI pipelines; Immutable infrastructure; CI/CD image building
## Validation
1. packer validate passes; 2. Image builds successfully; 3. Provisioner executes"""),
    ("vagrant", "Creates and manages portable development environments with Vagrant, VirtualBox, and provisioners.", "devops", ["vagrant", "virtualbox", "dev-environment", "provisioning", "vm"], ["sonnet", "opus"], """# Vagrant
> Reproducible development environments as code.
## Quick Start
```ruby
Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/jammy64"
  config.vm.network "forwarded_port", guest: 80, host: 8080
  config.vm.provision "shell", inline: "apt-get update && apt-get install -y nginx"
end
```
```bash
vagrant up && vagrant ssh
```
## Multi-Machine
```ruby
config.vm.define "web" do |web| web.vm.network "private_network", ip: "192.168.33.10" end
config.vm.define "db" do |db| db.vm.network "private_network", ip: "192.168.33.11" end
```
## When to Use
- Team dev environments; Cross-platform testing; Reproducible demos
## Validation
1. vagrant up creates VM; 2. Port forwarding works; 3. Provisioning executes"""),
    ("great-expectations", "Validates data quality with Great Expectations, creating expectations, suites, and data docs.", "data", ["great-expectations", "data-quality", "validation", "testing", "data-pipeline"], ["sonnet", "opus"], """# Great Expectations
> Data quality validation and documentation framework.
## Quick Start
```python
import great_expectations as gx
context = gx.get_context()
datasource = context.sources.add_pandas("my_data")
data_asset = datasource.add_dataframe_asset("my_asset")
batch_request = data_asset.build_batch_request(dataframe=df)
expectation_suite = context.add_expectation_suite("my_suite")
validator = context.get_validator(batch_request=batch_request, expectation_suite_name="my_suite")
validator.expect_column_values_to_not_be_null("user_id")
validator.expect_column_values_to_be_between("age", min_value=0, max_value=120)
validator.save_expectation_suite()
checkpoint = context.add_or_update_checkpoint(name="my_checkpoint", validator=validator)
checkpoint.run()
```
## When to Use
- Data pipeline quality gates; Data warehouse validation; ML data validation
## Validation
1. Expectations created; 2. Validation runs pass/fail; 3. Data docs generated"""),
    ("mariadb", "Manages MariaDB databases with Galera clustering, performance optimization, and InnoDB tuning.", "database", ["mariadb", "database", "mysql", "clustering", "sql"], ["sonnet", "opus"], """# MariaDB
> Enhanced drop-in replacement for MySQL with additional features.
## Quick Start
```sql
CREATE DATABASE myapp;
CREATE USER 'app'@'localhost' IDENTIFIED BY 'password';
GRANT ALL ON myapp.* TO 'app'@'localhost';
```
## Galera Cluster
```cnf
[galera] wsrep_on=ON; wsrep_provider=/usr/lib/galera/libgalera_smm.so
wsrep_cluster_address=gcomm://192.168.1.10:4567,192.168.1.11:4567
wsrep_cluster_name=my_cluster; wsrep_node_name=node1
```
## When to Use
- MySQL-compatible workloads; High-availability clustering; Data warehousing
## Validation
1. MariaDB service starts; 2. Galera replication syncs; 3. Queries use indexes"""),
    ("perplexity-api", "Integrates Perplexity AI's online LLM API for web-connected search and generation with real-time information.", "ai", ["perplexity", "api", "search", "llm", "online"], ["sonnet", "opus"], """# Perplexity API
> Online LLM API with real-time web search capabilities.
## Quick Start
```python
import requests
response = requests.post("https://api.perplexity.ai/chat/completions", json={
  "model": "sonar-pro",
  "messages": [{"role": "user", "content": "What is the latest news about AI?"}]
}, headers={"Authorization": "Bearer YOUR_API_KEY", "Content-Type": "application/json"})
print(response.json()["choices"][0]["message"]["content"])
```
## When to Use
- Real-time web-connected Q&A; Research assistance; Current events; Factual queries
## Validation
1. API key authenticates; 2. Responses include citations; 3. Web search returns current info"""),
    ("matter-protocol", "Builds smart home devices with Matter protocol, the unified standard for IoT interoperability.", "iot", ["matter", "iot", "smart-home", "connectivity", "protocol"], ["sonnet", "opus"], """# Matter Protocol
> Unified smart home standard for device interoperability.
## Quick Start
```bash
git clone https://github.com/project-chip/connectedhomeip.git
cd connectedhomeip && ./scripts/checkout_submodules.sh && source ./scripts/activate.sh
```
## When to Use
- Smart home device development; Cross-platform IoT; Matter accessories
## Validation
1. Device commissions; 2. Controls work across ecosystems; 3. Certification tests pass"""),
]

base = '.claude/skills'
for name, desc, cat, tags, models, content in skills:
    path = f'{base}/{cat}/{name}'
    os.makedirs(path, exist_ok=True)
    t = '[' + ', '.join(tags) + ']'
    m = '[' + ', '.join(models) + ']'
    with open(f'{path}/SKILL.md', 'w', encoding='utf-8') as f:
        f.write(f"---\nname: {name}\ndescription: {desc}\ncategory: {cat}\ntags: {t}\nmodels: {m}\nversion: 1.0.0\ncreated: 2026-05-14\n---\n{content}\n")
    print(f'  {cat}/{name}')

print(f'\nDone: {len(skills)} skills')
