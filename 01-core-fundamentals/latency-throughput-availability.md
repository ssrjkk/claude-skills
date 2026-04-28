# latency / throughput / availability

**What it is**  
Latency = время операции. Throughput = операций/сек. Availability = % времени работы. 

**Why it matters**  
SLA, UX, выбор архитектуры. 

**Must know**  
Latency: p50, p95, p99. Throughput: RPS или B/s. Availability: 99.9% = 43.2 мин/мес. 

**Must be able to do**  
Измерить p99 latency. Выбрать оптимизацию (latency vs throughput). 

**Where it is used**  
Low latency: торговые системы. High throughput: логи, batch. 

**Trade-offs**  
Оптимизация latency = дороже. Оптимизация throughput = дешевле, но медленнее. 

**Common mistakes**  
Оптимизация p99 когда проблема в p50. 

**Interview check**  
Q: Как улучшить latency API? A: Кэш (Redis), read replicas, ближе к данным. 

**Mini example**  
API -> Lambda -> DynamoDB: p99 45мс. +ElastiCache: p99 12мс. +$30/мес.