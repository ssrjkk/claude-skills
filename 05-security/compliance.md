# compliance

**What it is**  
Соответствие стандартам (GDPR, HIPAA, PCI-DSS). 

**Why it matters**  
Штрафы, потеря клиентов. 

**Must know**  
AWS Artifact (документы). Encryption at rest/transit. Audit logs. 

**Must be able to do**  
Включить CloudTrail. Шифровать S3 (AES-256). 

**Where it is used**  
Финтех, медицина, госсектор. 

**Trade-offs**  
+Compliance. -Сложнее настройка. 

**Common mistakes**  
Отключение CloudTrail. Нет шифрования. 

**Interview check**  
Q: Как соответствовать GDPR? A: Data residency, right to be forgotten, encryption. 

**Mini example**  
S3: bucket policy запрещает нешифрованные uploads.