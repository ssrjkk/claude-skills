# IAM

**What it is**  
Identity and Access Management. Управление доступом к ресурсам. 

**Why it matters**  
Фундамент безопасности облака. 

**Must know**  
Users, Groups, Roles, Policies (JSON). Least privilege. 

**Must be able to do**  
Создать IAM role для Lambda. Привязать policy. 

**Where it is used**  
Все облачные ресурсы. 

**Trade-offs**  
+Безопасность. -Сложность при масштабе. 

**Common mistakes**  
IAM Users вместо Roles. * политики (full access). 

**Interview check**  
Q: Role vs User? A: Role для сервисов. User для людей. 

**Mini example**  
Lambda role: AWSLambdaBasicExecutionRole + S3 read policy.