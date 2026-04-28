# lifecycle / glacier

**What it is**  
Автоматическое перемещение данных в холодные классы. 

**Why it matters**  
Cost optimization для старых данных. 

**Must know**  
Transition (Standard -> IA -> Glacier). Expiration (удаление). 

**Must be able to do**  
Настроить lifecycle: 30 дней -> IA, 90 дней -> Glacier. 

**Where it is used**  
Backups, логи, compliance архивы. 

**Trade-offs**  
+Дешевле. -Glacier retrieval 3-5 часов. 

**Common mistakes**  
Glacier для часто читаемых данных. 

**Interview check**  
Q: Glacier retrieval time? A: Standard 3-5 часов, Expedited 1-5 мин. 

**Mini example**  
S3 lifecycle: после 90 дней -> Glacier Deep Archive $0.00099/GB.