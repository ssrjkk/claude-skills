# serverless functions

**What it is**  
Запуск кода без управления серверами. Плата за выполнение. 

**Why it matters**  
Нулевые операционные расходы. Плата только за использование. 

**Must know**  
Lambda (AWS), Cloud Functions (GCP). Лимиты: 15 мин, 10GB RAM. Cold start: Go/Node 100мс, Java 1-3с. 

**Must be able to do**  
Выбрать для sporadic workloads. Настроить provisioned concurrency. 

**Where it is used**  
Event-driven (S3 upload -> process). Sporaadic workloads. 

**Trade-offs**  
+Ноль простоя оплаты. -Cold start, -лимиты по времени, -дороже при стабильном трафике. 

**Common mistakes**  
Lambda для 30-минутной обработки (timeout). Нет concurrency limit (1 баг -> $1000 счет). 

**Interview check**  
Q: Когда НЕ использовать serverless? A: Долгие процессы, стабильно высокий трафик. 

**Mini example**  
Image resize: S3 upload -> SQS -> Lambda. 10k images/мес = $0.20.