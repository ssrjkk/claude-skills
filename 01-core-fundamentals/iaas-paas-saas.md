# IaaS / PaaS / SaaS

**What it is**  
Уровни абстракции: инфраструктура, платформа или софт как сервис.

**Why it matters**  
Определяет операционную нагрузку и гибкость. 

**Must know**  
IaaS = вы управляете ОС. PaaS = вы управляете только кодом. SaaS = готовый продукт. 

**Must be able to do**  
Выбрать правильный уровень под задачу. Объяснить trade-offs. 

**Where it is used**  
IaaS: lift-and-shift. PaaS: веб-API. SaaS: почта, CRM. 

**Trade-offs**  
IaaS: +контроль, -операционка. PaaS: +быстро, -ограничения. SaaS: +готово, -lock-in. 

**Common mistakes**  
IaaS для простого API. PaaS когда нужен custom kernel. SaaS для бизнес-логики. 

**Interview check**  
Q: IaaS vs PaaS? A: IaaS когда нужен контроль ОС. PaaS когда нужен быстрый релиз. 

**Mini example**  
EC2 $300/мес -> Beanstalk $150/мес -> Lambda $40/мес. Lambda cold start +800мс.