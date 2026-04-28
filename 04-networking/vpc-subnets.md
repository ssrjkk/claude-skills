# VPC / subnets

**What it is**  
Изолированная сеть в облаке. Приватные IP, routing tables. 

**Why it matters**  
Фундамент безопасности и connectivity. 

**Must know**  
CIDR blocks (/16, /24). Public subnet (IGW). Private subnet (NAT Gateway). 

**Must be able to do**  
Спроектировать VPC (/16). Разбить на public/private subnets. 

**Where it is used**  
Все облачные deployments. 

**Trade-offs**  
Public: +доступ из интернета, -риск. Private: +безопасно, -нужен NAT для исходящего. 

**Common mistakes**  
/24 на VPC (не хватит IP). Public subnets для БД. 

**Interview check**  
Q: Чем public отличается от private subnet? A: Public имеет route to IGW. Private -> NAT Gateway. 

**Mini example**  
VPC 10.0.0.0/16. Public: 10.0.1.0/24 (ALB). Private: 10.0.2.0/24 (ECS tasks).