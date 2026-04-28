# secrets management

**What it is**  
Хранение паролей, API ключей, сертификатов. 

**Why it matters**  
Утечка секретов = взлом. 

**Must know**  
Secrets Manager, Parameter Store, Key Vault. Никаких секретов в коде. 

**Must be able to do**  
Получить секрет из Secrets Manager в Lambda. 

**Where it is used**  
БД credentials, API keys. 

**Trade-offs**  
+Безопасность. -Latency на получение. 

**Common mistakes**  
Секреты в env vars. Коммит .env в git. 

**Interview check**  
Q: Где хранить БД password? A: Secrets Manager, ротация автоматическая. 

**Mini example**  
Secrets Manager: password rotation каждые 30 дней. $0.40/secret/мес.