# region / availability zone / edge

**What it is**  
Region = гео-зона. AZ = изолированная зона внутри. Edge = точки у клиента. 

**Why it matters**  
HA, latency, Disaster Recovery. 

**Must know**  
Region: 100+ км между. AZ: независимое электричество. Edge: CloudFront/PoP. 

**Must be able to do**  
Развернуть HA в 3 AZ. Спроектировать DR в другом регионе. 

**Where it is used**  
Multi-AZ: продакшн. Multi-region: DR. Edge: CDN, IoT. 

**Trade-offs**  
Multi-AZ: +HA, +30% стоимости. Multi-region: +DR, +100% стоимости. 

**Common mistakes**  
Single AZ «HA». Все регионы стоят одинаково. Edge для внутренних API. 

**Interview check**  
Q: AZ vs Region? A: AZ внутри региона, физически разделены. 

**Mini example**  
ALB в 3 AZ, EKS nodes в 3 AZ. Сбой AZ -> 0 downtime.