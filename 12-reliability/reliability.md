# Reliability

## SLO / SLI / SLA

**What it is**  
Service Level Objectives / Indicators / Agreements. 

**Why it matters**  
Измерение надежности. 

**Must know**  
SLI: метрика (availability, latency). SLO: цель (99.9%). SLA: контракт. 

**Must be able to do**  
Определить SLO для API. 

**Where it is used**  
Все сервисы. 

**Trade-offs**  
+Measurable. -Может быть сложно достичь. 

**Common mistakes**  
SLO 100% (невозможно). 

**Interview check**  
Q: SLO vs SLA? A: SLO внутренний, SLA контракт с клиентом. 

**Mini example**  
API SLO: 99.9% availability, p99 latency <100ms.

## Error Budgets

**What it is**  
Бюджет ошибок (1 - SLO). 

**Why it matters**  
Баланс между скоростью релизов и надежностью. 

**Must know**  
Если budget исчерпан -> замедлить релизы. 

**Must be able to do**  
Рассчитать error budget. 

**Where it is used**  
SRE практики. 

**Trade-offs**  
+Balance. -Может блокировать релизы. 

**Common mistakes**  
Игнорирование error budget. 

**Interview check**  
Q: Error budget? A: Количество допустимых ошибок, 1 - SLO. 

**Mini example**  
SLO 99.9% -> error budget 0.1% downtime/мес = 43.2 мин.

## Chaos Engineering

**What it is**  
Намеренное внесение сбоев для проверки устойчивости. 

**Why it matters**  
Выявление слабых мест до реальных аварий. 

**Must know**  
Chaos Monkey, FIS (AWS). 

**Must be able to do**  
Запустить chaos experiment: terminate EC2. 

**Where it is used**  
High-reliability системы. 

**Trade-offs**  
+Resilience. -Риск. 

**Common mistakes**  
Chaos в продакшене без подготовки. 

**Interview check**  
Q: Chaos Engineering? A: Эксперименты с отказами для проверки HA. 

**Mini example**  
FIS: terminate 10% ECS tasks, проверить recovery.