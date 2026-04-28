# DNS / Cloud DNS

**What it is**  
Система имен (domain -> IP). Route 53, Cloud DNS, Azure DNS. 

**Why it matters**  
Service discovery, routing. 

**Must know**  
A record (name -> IPv4). CNAME (alias). TTL (caching). Alias records (AWS). 

**Must be able to do**  
Настроить failover DNS (primary -> secondary). Geo-routing. 

**Where it is used**  
Все публичные endpoints. 

**Trade-offs**  
Lower TTL: +быстрый failover, -больше запросов. Higher TTL: +кеширование, -медленнее обновление. 

**Common mistakes**  
TTL 300с для критичного failover. CNAME на apex domain (нельзя, используй Alias). 

**Interview check**  
Q: A vs CNAME? A: A -> IPv4. CNAME -> другой домен. 

**Mini example**  
api.example.com CNAME -> elb-123.us-east-1.elb.amazonaws.com. TTL 60с для быстрого failover.