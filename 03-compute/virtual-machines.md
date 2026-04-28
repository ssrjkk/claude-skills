# virtual machines

**What it is**  
Эмулированные серверы с полной ОС. 

**Why it matters**  
Фундамент облаков. Нужен когда нужен контроль ОС. 

**Must know**  
EC2, Compute Engine, Virtual Machines. On-demand, Reserved (-72%), Spot (-90%). 

**Must be able to do**  
Выбрать тип инстанса. Настроить ASG. Перейти на Graviton (ARM). 

**Where it is used**  
Lift-and-shift, специфичная ОС, GPU workloads, steady load. 

**Trade-offs**  
+Полный контроль. -Операционные расходы, -медленнее развертывание. 

**Common mistakes**  
Over-provisioning «на всякий случай». Нес использование Reserved. VMs как pets. 

**Interview check**  
Q: Как снизить стоимость EC2? A: Reserved для steady-state, Spot для fault-tolerant. 

**Mini example**  
EC2 c6i.4xlarge $0.68/час = $490/мес. CPU 20% -> Fargate $37/мес (8ч/день).