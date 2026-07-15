---
name: ssl-tls
description: "Configures SSL/TLS certificates for web servers, including Let's Encrypt, certbot, and HTTPS hardening."
category: security
tags: [ssl, tls, https, certificates, encryption]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# SSL/TLS
> Secure communication with SSL/TLS certificates.
## Quick Start
```bash
sudo certbot --nginx -d example.com -d www.example.com
sudo certbot renew
```
## Nginx HTTPS
```nginx
listen 443 ssl http2; server_name example.com;
ssl_certificate /etc/letsencrypt/live/example.com/fullchain.pem;
ssl_certificate_key /etc/letsencrypt/live/example.com/privkey.pem;
ssl_protocols TLSv1.2 TLSv1.3;
add_header Strict-Transport-Security "max-age=63072000" always;
```
## When to Use
- HTTPS enforcement; Certificate lifecycle; Security compliance
## Validation
1. SSL Labs test gets A+; 2. Certificate not expired; 3. HTTP to HTTPS redirect works
