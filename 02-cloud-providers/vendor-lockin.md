# Vendor Lock-in

**Уровни блокировки**:
1. ВМ со стандартной ОС -> низкая
2. Managed services (RDS) -> средняя
3. Serverless (Lambda) -> высокая
4. Проприетарные сервисы (DynamoDB) -> очень высокая

**Митигация**: Контейнеры (Docker). Стандартные протоколы (HTTP, gRPC). Абстракция cloud SDK.