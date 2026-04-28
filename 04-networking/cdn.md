# CDN / CloudFront

**What it is**  
Content Delivery Network. Кеширование контента ближе к пользователю. 

**Why it matters**  
Latency (снижение на 50-80%), защита от DDoS. 

**Must know**  
Edge locations. Cache policies (TTL). Origin (S3, ALB). 

**Must be able to do**  
Настроить CloudFront поверх S3. Cache policy: /images -> 1 day. 

**Where it is used**  
Static assets, видео, API gateway (edge-optimized). 

**Trade-offs**  
+Latency, +DDoS protection. -Cache invalidation сложнее, -стоимость за запрос. 

**Common mistakes**  
Cache everything (включая API POST). Нет invalidation стратегии. 

**Interview check**  
Q: Зачем CDN для API? A: Можно кешировать GET запросы (справочники). 

**Mini example**  
S3 -> CloudFront. p95 latency US: 400мс -> 80мс. $0.60/GB + $0.02/10k requests.