---
name: cert-manager
description: Manages TLS certificates in Kubernetes with cert-manager, Let's Encrypt, and auto-renewal.
category: security
tags: [cert-manager, tls, kubernetes, lets-encrypt, certificates]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# cert-manager
> Automated certificate management for Kubernetes.
## Quick Start
```bash
kubectl apply -f https://github.com/cert-manager/cert-manager/releases/download/v1.15.0/cert-manager.yaml
```
## Issuer & Certificate
```yaml
apiVersion: cert-manager.io/v1; kind: ClusterIssuer; metadata: { name: letsencrypt-prod }
spec:
  acme: { server: https://acme-v02.api.letsencrypt.org/directory, email: admin@example.com, privateKeySecretRef: { name: letsencrypt-prod-key }, solvers: [{ http01: { ingress: { class: nginx } } }] }
---
apiVersion: cert-manager.io/v1; kind: Certificate; metadata: { name: example-com-tls }
spec: { secretName: example-com-tls, issuerRef: { name: letsencrypt-prod, kind: ClusterIssuer }, dnsNames: [example.com] }
```
## When to Use
- Automatic TLS in Kubernetes; Let's Encrypt; Multi-domain certs
## Validation
1. cert-manager pods are running; 2. Certificate becomes Ready=True; 3. TLS secret created
