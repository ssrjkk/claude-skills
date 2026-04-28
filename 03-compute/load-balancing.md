# load balancing

**What it is**  
Распределение трафика между несколькими инстансами. 

**Why it matters**  
HA, масштабируемость, health checks. 

**Must know**  
L7 (ALB): HTTP/HTTPS, path-based routing. L4 (NLB): TCP/UDP, ultra-low latency. 

**Must be able to do**  
Выбрать ALB vs NLB. Настроить health checks (/health endpoint). 

**Where it is used**  
Веб-приложения: ALB. Games, real-time: NLB. 

**Trade-offs**  
ALB: +features (path routing), -чуть больше latency. NLB: +ultra-fast, -не понимает HTTP. 

**Common mistakes**  
NLB и ожидание path-based routing. Health check timeout слишком короткий. 

**Interview check**  
Q: ALB vs NLB? A: ALB = L7 (HTTP), path routing. NLB = L4 (TCP), минимум задержки. 

**Mini example**  
ALB слушает 443, терминирует SSL, роутит /api -> api-service.