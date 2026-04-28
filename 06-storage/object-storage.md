# object storage

**What it is**  
S3, Cloud Storage, Blob. Ключ-значение в облаке. 

**Why it matters**  
Unlimited scale, дешево, durable (99.999999999%). 

**Must know**  
Buckets, keys, prefixes. Storage classes (Standard, IA, Glacier). 

**Must be able to do**  
Настроить lifecycle policies. S3 -> Glacier после 30 дней. 

**Where it is used**  
Backups, static sites, data lakes. 

**Trade-offs**  
+Cheap, +durable. -Higher latency чем block storage. 

**Common mistakes**  
Хранение активных данных в Glacier. Нет lifecycle policies. 

**Interview check**  
Q: S3 durability? A: 11 9's (99.999999999%). 

**Mini example**  
100TB в S3 Standard $2300/мес. -> Glacier $400/мес.