# block storage

**What it is**  
EBS, Persistent Disk. Виртуальные диски для VMs. 

**Why it matters**  
Производительность БД и OS. 

**Must know**  
SSD (gp3) vs HDD (st1). IOPS, throughput. Snapshots. 

**Must be able to do**  
Выбрать gp3 для БД. Настроить snapshots каждые 6ч. 

**Where it is used**  
Boot volumes, БД, файловые системы. 

**Trade-offs**  
+Производительность. -Цена, привязка к AZ. 

**Common mistakes**  
gp2 вместо gp3 (дороже). Нет snapshots. 

**Interview check**  
Q: gp3 vs gp2? A: gp3 дешевле, IOPS независимы от размера. 

**Mini example**  
gp3: 3000 IOPS, 125 MB/s = $0.09/GB + $0.005/provisioned IOPS.