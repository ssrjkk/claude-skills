# least privilege

**What it is**  
Давать минимум прав для выполнения задачи. 

**Why it matters**  
Снижение blast radius при компрометации. 

**Must know**  
Никаких *. Только нужные actions. Регулярный audit. 

**Must be able to do**  
Написать policy с конкретными actions. 

**Where it is used**  
Все IAM политики. 

**Trade-offs**  
+Безопасность. -Время на настройку. 

**Common mistakes**  
Admin access для приложения. 

**Interview check**  
Q: Как проверить least privilege? A: IAM Access Analyzer. 

**Mini example**  
S3 policy: s3:GetObject только для bucket-name.