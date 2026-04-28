# shared responsibility model

**What it is**  
Провайдер защищает облако. Вы защищаете то, что в облаке. 

**Why it matters**  
Определяет границу безопасности. 

**Must know**  
AWS управляет: физика, гипервизор, патчинг managed сервисов. Вы: данные, IAM, патчинг ОС (EC2). 

**Must be able to do**  
Объяснить, кто отвечает за патчинг RDS (AWS) vs EC2 (вы). 

**Where it is used**  
Всегда. Каждое взаимодействие с облаком. 

**Common mistakes**  
«AWS всё шифрует». IAM users вместо roles. Открытые S3 бакеты. 

**Interview check**  
Q: Кто патчит ОС на RDS? A: AWS. Это managed service. 

**Mini example**  
Capital One 2019: WAF misconfiguration (клиентская ответственность) -> 100M записей утекло.