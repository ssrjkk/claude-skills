# Observability

## CloudWatch

**What it is**  
AWS native monitoring. 

**Why it matters**  
Интегрировано с AWS сервисами. 

**Must know**  
Metrics, logs, alarms. Dashboards. 

**Must be able to do**  
Создать alarm на CPU >70%. 

**Where it is used**  
AWS environments. 

**Trade-offs**  
+AWS native. -AWS lock-in. 

**Common mistakes**  
Нет alarms. 

**Interview check**  
Q: CloudWatch metrics vs logs? A: Metrics = числовые данные, logs = текстовые записи. 

**Mini example**  
CloudWatch alarm: CPU >70% 5 мин -> SNS notification.

## Prometheus

**What it is**  
Open-source monitoring и alerting. 

**Why it matters**  
Standard для K8s. 

**Must know**  
Time-series DB, exporters, PromQL. 

**Must be able to do**  
Настроить Prometheus в K8s. 

**Where it is used**  
K8s, open-source стек. 

**Trade-offs**  
+Standard. -Setup сложнее. 

**Common mistakes**  
Нет retention политики. 

**Interview check**  
Q: Prometheus data model? A: Time series: metric name + labels. 

**Mini example**  
Prometheus scrape K8s pods every 15s.

## Grafana

**What it is**  
Open-source визуализация. 

**Why it matters**  
Dashboards для метрик. 

**Must know**  
Data sources (Prometheus, CloudWatch). Panels, queries. 

**Must be able to do**  
Создать dashboard с CPU метрикой. 

**Where it is used**  
Все monitoring стеки. 

**Trade-offs**  
+Visual. -Доп. инструмент. 

**Common mistakes**  
Hardcoded data sources. 

**Interview check**  
Q: Grafana vs CloudWatch dashboards? A: Grafana multi-source, лучше визуализация. 

**Mini example**  
Grafana dashboard: EKS cluster metrics.

## Tracing

**What it is**  
Отслеживание запросов через сервисы. 

**Why it matters**  
Понимание latency в distributed системах. 

**Must know**  
X-Ray (AWS), Jaeger, Zipkin. Spans, traces. 

**Must be able to do**  
Настроить X-Ray для Lambda. 

**Where it is used**  
Microservices. 

**Trade-offs**  
+Visibility. -Overhead. 

**Common mistakes**  
Нет sampling. 

**Interview check**  
Q: Trace vs span? A: Trace = полный запрос, span = шаг внутри. 

**Mini example**  
X-Ray: trace API -> Lambda -> DynamoDB.

## Alerts

**What it is**  
Уведомления о проблемах. 

**Why it matters**  
Быстрая реакция на инциденты. 

**Must know**  
SNS, PagerDuty, Slack. Severity levels. 

**Must be able to do**  
Настроить alert на 5xx errors. 

**Where it is used**  
Все продакшн системы. 

**Trade-offs**  
+Quick reaction. -Alert fatigue. 

**Common mistakes**  
Слишком много alerts. 

**Interview check**  
Q: Alert fatigue? A: Слишком много alerts, инженеры игнорируют. 

**Mini example**  
CloudWatch alarm -> SNS -> PagerDuty -> call on-call.