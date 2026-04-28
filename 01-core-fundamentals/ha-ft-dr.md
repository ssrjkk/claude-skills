# high availability / fault tolerance / disaster recovery

**What it is**  
HA = работа при сбоях. FT = ноль downtime. DR = восстановление региона. 

**Why it matters**  
SLA, репутация, деньги. 

**Must know**  
HA: Multi-AZ, redundant, failover < минуты. FT: active-active, 2x стоимости. DR: RPO, RTO. 

**Must be able to do**  
Спроектировать HA (Multi-AZ). Настроить DR (cross-region replica). 

**Where it is used**  
HA: любой продакшн. FT: финтех. DR: enterprise контракты. 

**Trade-offs**  
HA: +доступность, +30% стоимости. FT: +ноль простоя, +100% стоимости. 

**Common mistakes**  
«HA» с single AZ. DR не тестировали. Путаница backup vs DR. 

**Interview check**  
Q: HA vs FT? A: HA допускает краткий простой. FT = ноль простоя (active-active). 

**Mini example**  
RDS Multi-AZ: failover 2-5 мин. DR: cross-region replica, RTO <15 мин.