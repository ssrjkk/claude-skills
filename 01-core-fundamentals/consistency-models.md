# consistency models

**What it is**  
Правила того, когда записанные данные видны читателям. 

**Why it matters**  
Корректность данных, UX, производительность. 

**Must know**  
Strong: читатель всегда видит последнюю запись. Eventual: может увидеть старые данные. 

**Where it is used**  
Strong: деньги, auth state. Eventual: каталог товаров, аналитика. 

**Trade-offs**  
Strong: +корректность, -latency. Eventual: +fast, -stale data. 

**Common mistakes**  
Eventual для инвентаря (перепродажа). Strong для всех (убивает доступность). 

**Interview check**  
Q: Как обеспечить strong consistency? A: Raft/Paxos (etcd) или strong БД (RDS). 

**Mini example**  
Bank ledger: Strong. Shopping cart: Eventual OK (пользователь не заметит 100мс).