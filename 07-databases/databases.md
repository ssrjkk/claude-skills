# databases

## SQL vs NoSQL

**What it is**  
Реляционные (SQL) vs нереляционные (NoSQL) БД. 

**Why it matters**  
Выбор БД определяет масштабируемость и консистентность. 

**Must know**  
SQL: ACID, структурированные данные, сложные запросы. NoSQL: BASE, горизонтальное масштабирование, flexible schema. 

**Must be able to do**  
Выбрать SQL для транзакций, NoSQL для high throughput. 

**Where it is used**  
SQL: финтех, ERP. NoSQL: соцсети, IoT. 

**Trade-offs**  
SQL: +консистентность, -масштабируемость. NoSQL: +масштабируемость, -консистентность. 

**Common mistakes**  
NoSQL для сложных JOIN-ов. SQL для petabyte-scale. 

**Interview check**  
Q: SQL vs NoSQL? A: SQL для ACID и структуры. NoSQL для масштаба и гибкости. 

**Mini example**  
Bank transactions: PostgreSQL. User sessions: DynamoDB.

## DynamoDB

**What it is**  
Managed NoSQL key-value и document store от AWS. 

**Why it matters**  
Serverless, auto-scaling, single-digit ms latency. 

**Must know**  
Partition key, sort key. RCU/WCU. On-demand vs provisioned. 

**Must be able to do**  
Спроектировать key schema. Рассчитать RCU/WCU. 

**Where it is used**  
Session stores, cart, real-time bidding. 

**Trade-offs**  
+Serverless, +fast. -Vendor lock-in, -сложные запросы. 

**Common mistakes**  
Sequential keys (hot partitions). Недостаточно RCU. 

**Interview check**  
Q: Как избежать hot partitions? A: High-cardinality partition key. 

**Mini example**  
UserID (partition) + OrderID (sort). 1000 RCU = $0.125/час.

## RDS

**What it is**  
Managed relational database (PostgreSQL, MySQL, etc). 

**Why it matters**  
Не нужно администрировать БД. 

**Must know**  
Multi-AZ, read replicas. Backup retention. 

**Must be able to do**  
Настроить Multi-AZ. Создать read replica. 

**Where it is used**  
Любые SQL workloads. 

**Trade-offs**  
+Managed, +HA. -Дороже self-managed, -меньше контроля. 

**Common mistakes**  
Single AZ в продакшене. Нет read replicas для чтения. 

**Interview check**  
Q: RDS Multi-AZ failover? A: 2-5 мин, automatic. 

**Mini example**  
PostgreSQL Multi-AZ: $0.50/час. Read replica: +$0.50/час.

## Aurora

**What it is**  
Cloud-native relational DB от AWS. 

**Why it matters**  
В 5 раз быстрее MySQL, до 128TB. 

**Must know**  
Storage auto-scaling. Aurora Serverless v2. 

**Must be able to do**  
Мигрировать с RDS на Aurora. 

**Where it is used**  
High-performance SQL workloads. 

**Trade-offs**  
+Performance, +scale. -Vendor lock-in, -дороже RDS. 

**Common mistakes**  
Aurora для маленьких БД (дорого). 

**Interview check**  
Q: Aurora vs RDS? A: Aurora cloud-native, лучше performance и scale. 

**Mini example**  
Aurora Serverless v2: $0.10/hour per ACU.

## Backups

**What it is**  
Резервные копии БД. 

**Why it matters**  
Disaster recovery, point-in-time recovery. 

**Must know**  
Automated backups (RDS 35 дней). Manual snapshots. 

**Must be able to do**  
Настроить backup retention. Восстановить из snapshot. 

**Where it is used**  
Все БД. 

**Trade-offs**  
+Protection. -Стоимость хранения. 

**Common mistakes**  
Нет backups. Retention 1 день. 

**Interview check**  
Q: RDS backup retention? A: До 35 дней automated. 

**Mini example**  
RDS snapshot: 100GB = $1.50/мес.