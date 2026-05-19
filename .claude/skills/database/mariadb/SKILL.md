---
name: mariadb
description: Manages MariaDB databases with Galera clustering, performance optimization, and InnoDB tuning.
category: database
tags: [mariadb, database, mysql, clustering, sql]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# MariaDB
> Enhanced drop-in replacement for MySQL with additional features.
## Quick Start
```sql
CREATE DATABASE myapp;
CREATE USER 'app'@'localhost' IDENTIFIED BY 'password';
GRANT ALL ON myapp.* TO 'app'@'localhost';
```
## Galera Cluster
```cnf
[galera] wsrep_on=ON; wsrep_provider=/usr/lib/galera/libgalera_smm.so
wsrep_cluster_address=gcomm://192.168.1.10:4567,192.168.1.11:4567
wsrep_cluster_name=my_cluster; wsrep_node_name=node1
```
## When to Use
- MySQL-compatible workloads; High-availability clustering; Data warehousing
## Validation
1. MariaDB service starts; 2. Galera replication syncs; 3. Queries use indexes
