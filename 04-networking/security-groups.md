# security groups / NACL

**What it is**  
Stateful firewall (SG) и stateless (NACL) на уровне сети. 

**Why it matters**  
Первый рубеж защиты. 

**Must know**  
SG: allow only, stateful (возвратный трафик разрешен). NACL: allow/deny, stateless. 

**Must be able to do**  
Настроить SG: только 443 inbound. NACL: блокировка IP. 

**Where it is used**  
Все ресурсы в VPC. 

**Trade-offs**  
SG: +просто, -нельзя deny. NACL: +можно блокировать, -сложнее. 

**Common mistakes**  
0.0.0.0/0 на SSH (22). SG между ресурсами через public IP. 

**Interview check**  
Q: SG vs NACL? A: SG stateful, allow-only. NACL stateless, allow/deny. 

**Mini example**  
SG: inbound 443 from ALB SG. Outbound: 5432 to RDS SG. 0.0.0.0/0 закрыт.