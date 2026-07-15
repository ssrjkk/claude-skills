---
name: neo4j
description: "Models graph data with Neo4j and Cypher query language for connected data and relationship-rich domains."
category: database
tags: [neo4j, graph, cypher, nosql, relationships]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# Neo4j

> Graph database for connected data with Cypher query language.

## Quick Start
```cypher
CREATE (alice:Person {name: 'Alice', age: 30})
CREATE (bob:Person {name: 'Bob', age: 25})
CREATE (alice)-[:KNOWS {since: 2020}]->(bob)
MATCH (n:Person) RETURN n.name, n.age
```

## Graph Queries
```cypher
MATCH path = shortestPath((alice:Person {name: 'Alice'})-[:KNOWS*]-(charlie:Person {name: 'Charlie'}))
RETURN path
MATCH (user:Person {name: 'Alice'})-[:PURCHASED]->(product)<-[:PURCHASED]-(other)-[:PURCHASED]->(rec)
WHERE NOT (user)-[:PURCHASED]->(rec)
RETURN rec.name, COUNT(*) as score ORDER BY score DESC LIMIT 5
```

## When to Use
- Social networks
- Recommendation engines
- Fraud detection
- Knowledge graphs

## Validation
1. Neo4j service is running
2. Nodes and relationships created
3. Cypher queries return expected patterns
