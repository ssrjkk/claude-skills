# stateless vs stateful systems

**What it is**  
Stateless = не хранит состояние. Stateful = хранит. 

**Why it matters**  
Масштабируемость, HA, простота. 

**Must know**  
Stateless: легко масштабировать. Stateful: сложнее (нужна синхронизация). 

**Must be able to do**  
Сделать приложение stateless. Перенести state в Redis/БД. 

**Where it is used**  
Stateless: веб-API, microservices. Stateful: БД, кэши, сессии. 

**Trade-offs**  
Stateless: +масштабируемость, -нужно внешнее хранилище state. 

**Common mistakes**  
Сессии в памяти (инстанс падает = пользователи вылогинились). 

**Interview check**  
Q: Как сделать приложение stateless? A: Сессии в Redis. Состояние в БД. 

**Mini example**  
Было: сессии в памяти EC2. Стало: сессии в ElastiCache. Масштабирование без проблем.