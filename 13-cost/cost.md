# Cost Optimization

## Strategies

**What it is**  
Снижение облачных затрат. 

**Why it matters**  
Облако может быть дорогим без контроля. 

**Must know**  
Rightsizing, reserved instances, spot instances, storage lifecycle. 

**Must be able to do**  
Найти overspend с помощью Cost Explorer. 

**Where it is used**  
Все облачные аккаунты. 

**Trade-offs**  
+Экономия. -Время на оптимизацию. 

**Common mistakes**  
Over-provisioning. Нет budgeting. 

**Interview check**  
Q: Как снизить cost? A: Rightsizing, Reserved, Spot, lifecycle policies. 

**Mini example**  
EC2 t2.large $70/мес -> t2.medium $35/мес (CPU 30%).

## Budgets

**What it is**  
Лимиты на затраты. 

**Why it matters**  
Предотвращение неожиданных счетов. 

**Must know**  
AWS Budgets, alerts. Forecast. 

**Must be able to do**  
Настроить budget $1000/мес, alert at 80%. 

**Where it is used**  
Все аккаунты. 

**Trade-offs**  
+Control. -Может ограничивать масштаб. 

**Common mistakes**  
Нет alerts. 

**Interview check**  
Q: AWS Budgets? A: Устанавливает лимиты и alerts на затраты. 

**Mini example**  
Budget $500, alert при $400, $450, $500.

## Reserved Instances

**What it is**  
Предоплата за инстансы (1-3 года). 

**Why it matters**  
Скидка до 72%. 

**Must know**  
Standard vs Convertible. Regional vs Zonal. 

**Must be able to do**  
Купить Reserved для steady-state workloads. 

**Where it is used**  
Steady workloads (prod DB, always-on). 

**Trade-offs**  
+Скидка. -Commitment. 

**Common mistakes**  
Reserved для dev/staging. 

**Interview check**  
Q: Reserved vs On-demand? A: Reserved дешевле при длительном использовании. 

**Mini example**  
EC2 m5.large: On-demand $0.10/час, Reserved $0.06/час.

## Spot Instances

**What it is**  
Неиспользуемые инстансы со скидкой до 90%. 

**Why it matters**  
Дешево для fault-tolerant workloads. 

**Must know**  
Могут быть отозваны с 2 мин notice. 

**Must be able to do**  
Использовать Spot для batch processing. 

**Where it is used**  
Batch, CI/CD, stateless workloads. 

**Trade-offs**  
+Дешево. -Могут быть отозваны. 

**Common mistakes**  
Spot для stateful БД. 

**Interview check**  
Q: Когда использовать Spot? A: Fault-tolerant, прерываемые задачи. 

**Mini example**  
Spot fleet: 10 instances, $0.03/час вместо $0.10.

## Tagging

**What it is**  
Метки ресурсов (Key=Value). 

**Why it matters**  
Cost allocation, automation. 

**Must know**  
Tags: Environment, Owner, CostCenter. 

**Must be able to do**  
Тегировать все ресурсы. 

**Where it is used**  
Все ресурсы. 

**Trade-offs**  
+Visibility. -Нужно поддерживать. 

**Common mistakes**  
Нет стандарта тегов. 

**Interview check**  
Q: Зачем теги? A: Cost allocation, automation, поиск ресурсов. 

**Mini example**  
Tag: Environment=Prod, Owner=BackendTeam.