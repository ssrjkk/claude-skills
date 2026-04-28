# CAP theorem

**What it is**  
Распределенная система может иметь только 2 из: Consistency, Availability, Partition tolerance. 

**Why it matters**  
Фундаментальный закон. Выбор БД и архитектуры. 

**Must know**  
CP: Consistency + Partition (финтех). AP: Availability + Partition (соцсети). CA: невозможно в distributed. 

**Must be able to do**  
Выбрать CP или AP. Объяснить, почему CA не существует. 

**Where it is used**  
CP: DynamoDB ConsistentRead, RDS. AP: DynamoDB default. 

**Trade-offs**  
CP: +согласованность, -доступность при partition. AP: +доступность, -eventual consistency. 

**Common mistakes**  
«Мы будем иметь все три». Eventual consistency для банковского леджера. 

**Interview check**  
Q: Можно ли иметь CA? A: Нет. Сетевые разделения неизбежны. 

**Mini example**  
DynamoDB default = AP. ConsistentRead=True = CP режим (2x RCU).