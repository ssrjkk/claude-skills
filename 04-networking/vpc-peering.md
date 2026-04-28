# VPC peering / Transit Gateway

**What it is**  
Соединение VPC между собой или с on-prem. 

**Why it matters**  
Hybrid cloud, multi-account connectivity. 

**Must know**  
Peering: point-to-point, no transitive. Transit Gateway: hub-and-spoke, transitive. 

**Must be able to do**  
Настроить peering между prod и staging. TGW для 10+ VPCs. 

**Where it is used**  
Multi-account AWS (org). Hybrid (Direct Connect -> TGW). 

**Trade-offs**  
Peering: +просто, -не транзитивно. TGW: +транзитивно, +centralized routing, -дороже ($0.05/hour per attachment). 

**Common mistakes**  
Overlapping CIDR blocks (peering не работает). Peering вместо TGW для 5+ VPCs. 

**Interview check**  
Q: Почему peering не транзитивно? A: Трафик не маршрутизируется через промежуточную VPC. 

**Mini example**  
VPC A (10.0.0.0/16) peering VPC B (10.1.0.0/16). TGW: 20 VPCs -> $600/мес.