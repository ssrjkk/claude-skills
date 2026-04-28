# Real-World Scenarios

## Scenario 1: High latency API

Проблема: API p99 500ms. 
Решение: Добавить ElastiCache Redis для частых запросов. 
Результат: p99 50ms, +$30/мес.

## Scenario 2: Cost overruns

Проблема: EC2 cost вырос в 3 раза. 
Решение: Rightsizing (t2.large -> t2.medium), Reserved Instances. 
Результат: Cost -60%.

## Scenario 3: DB bottleneck

Проблема: RDS CPU 90%. 
Решение: Добавить read replicas, перенести аналитические запросы. 
Результат: CPU 30%.

## Scenario 4: S3 public access

Проблема: Открытый S3 bucket. 
Решение: Block public access, bucket policy. 
Результат: Secure.

## Scenario 5: Lambda timeout

Проблема: Lambda 15 min timeout. 
Решение: Перенести в Fargate (до 1 час). 
Результат: Задача выполняется.