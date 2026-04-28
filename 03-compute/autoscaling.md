# autoscaling

**What it is**  
Автоматическое добавление/удаление инстансов под нагрузку. 

**Why it matters**  
Cost optimization + HA. 

**Must know**  
ASG: min/max/desired, scaling policies (CPU, network). Target tracking: держать CPU 70%. 

**Must be able to do**  
Настроить ASG policies. Установить max limit. 

**Where it is used**  
Продакшн с переменной нагрузкой. Веб-приложения. 

**Trade-offs**  
+Cost efficient, +HA. -Нужна stateless архитектура, cold start 2-3 мин. 

**Common mistakes**  
Нет max limit (auto-scaling до бесконечности при баге). 

**Interview check**  
Q: Как работает ASG? A: CloudWatch alarm -> trigger scaling policy -> добавить/удалить. 

**Mini example**  
ASG: min 2, desired 3, max 10. CPU >70% 3 мин -> +1 инстанс.