# scalability / elasticity

**What it is**  
Scalability = рост. Elasticity = авто-масштабирование. 

**Why it matters**  
Пиковые нагрузки, оптимизация затрат. 

**Must know**  
Vertical: больше CPU/RAM. Horizontal: больше инстансов. Elastic: auto-scaling. 

**Must be able to do**  
Настроить HPA/EKS ASG. Выбрать vert vs horiz. 

**Where it is used**  
Horizontal: веб-сервисы, stateless. Vertical: монолиты, БД. 

**Trade-offs**  
Horizontal: +HA, -сложнее. Vertical: +проще, -single point of failure. 

**Common mistakes**  
Вертикальное масштабирование БД до упора. Autoscaling без ограничений. 

**Interview check**  
Q: Vertical vs Horizontal? A: Vertical — больше ресурсов одному. Horizontal — больше инстансов. 

**Mini example**  
ECS Fargate: CPU >70% -> +1 task. Max 50 tasks. $0 пока нет трафика.