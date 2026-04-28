# file storage

**What it is**  
EFS, Cloud Filestore. Shared filesystem (NFS/SMB). 

**Why it matters**  
Shared access для нескольких инстансов. 

**Must know**  
NFSv4 (EFS), SMB (FSx). Throughput modes. 

**Must be able to do**  
Смонтировать EFS в EKS. 

**Where it is used**  
Shared configs, lift-and-shift приложения. 

**Trade-offs**  
+Shared. -Дороже, latency выше. 

**Common mistakes**  
EFS для high IOPS БД (медленно). 

**Interview check**  
Q: Когда EFS? A: Shared filesystem для нескольких EC2/EKS. 

**Mini example**  
EFS: $0.30/GB/мес. Throughput burst до 100MB/s.