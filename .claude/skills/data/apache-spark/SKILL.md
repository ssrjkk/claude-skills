---
name: apache-spark
description: Processes large-scale data with Apache Spark using DataFrames, RDDs, and Spark SQL. Use for big data ETL and analytics.
category: data
tags: [spark, big-data, dataframe, pyspark, analytics]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# Apache Spark

> Unified analytics engine for large-scale data processing.

## Quick Start
```python
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("MyApp").getOrCreate()
df = spark.read.csv("data/*.csv", header=True, inferSchema=True)
df.groupBy("category").agg({"amount": "sum"}).show()
```

## DataFrame API
```python
from pyspark.sql.functions import col, avg, when
result = df.filter(col("age") > 18) \
    .withColumn("adult", when(col("age") >= 21, "yes").otherwise("no")) \
    .groupBy("department").agg(avg("salary").alias("avg_salary"))
```

## Spark SQL
```python
df.createOrReplaceTempView("users")
result = spark.sql("SELECT department, AVG(salary) as avg_salary FROM users GROUP BY department")
```

## When to Use
- Terabyte-scale data processing
- ETL pipelines
- Interactive analytics
- ML feature engineering

## Validation
1. SparkContext initializes
2. DataFrame operations execute
3. Spark SQL queries return correct results
