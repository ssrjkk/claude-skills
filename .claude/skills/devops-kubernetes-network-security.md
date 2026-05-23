# Kubernetes Network Security

## Overview
Design and implement secure Kubernetes networking with network policies, service mesh integration, TLS, and advanced firewall rules.

## Context
You are a DevOps/Platform engineer securing Kubernetes clusters. You understand container networking, CNI plugins, and security boundaries.

## Key Principles
- **Least Privilege**: Default deny, allow only needed
- **Encryption**: TLS for all traffic
- **Segmentation**: Network policies isolate workloads
- **Monitoring**: Observe network traffic
- **Defense in Depth**: Multiple security layers

## Step-by-Step Instructions

### 1. Network Policy Fundamentals
```yaml
# Default deny all ingress
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: default-deny-ingress
  namespace: default
spec:
  podSelector: {}
  policyTypes:
  - Ingress

---
# Allow traffic from specific namespace
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-from-monitoring
  namespace: production
spec:
  podSelector:
    matchLabels:
      app: web
  policyTypes:
  - Ingress
  ingress:
  - from:
    - namespaceSelector:
        matchLabels:
          name: monitoring
    ports:
    - protocol: TCP
      port: 8080
```

### 2. Service-to-Service Communication
```yaml
# Allow payment-service to call order-service
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-payment-to-order
  namespace: production
spec:
  podSelector:
    matchLabels:
      service: order
  policyTypes:
  - Ingress
  ingress:
  - from:
    - podSelector:
        matchLabels:
          service: payment
    ports:
    - protocol: TCP
      port: 8000
```

### 3. Egress Control
```yaml
# Restrict outbound traffic
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: restrict-egress
  namespace: production
spec:
  podSelector: {}
  policyTypes:
  - Egress
  egress:
  # Allow DNS
  - to:
    - namespaceSelector: {}
    ports:
    - protocol: UDP
      port: 53
  # Allow external API calls
  - to:
    - podSelector:
        matchLabels:
          external: "true"
    ports:
    - protocol: TCP
      port: 443
```

### 4. TLS/mTLS Setup with Istio
```yaml
# Install Istio for service mesh
helm repo add istio https://istio-release.storage.googleapis.com/charts
helm install istio-base istio/base -n istio-system --create-namespace
helm install istiod istio/istiod -n istio-system

---
# Enable mTLS for all services in namespace
apiVersion: security.istio.io/v1beta1
kind: PeerAuthentication
metadata:
  name: default
  namespace: production
spec:
  mtls:
    mode: STRICT  # Require mTLS
```

### 5. Network Monitoring
```yaml
# NetworkPolicy audit logging
apiVersion: audit.k8s.io/v1
kind: Policy
rules:
- level: RequestResponse
  verbs: ["create", "delete", "patch"]
  resources: ["networkpolicies"]
- level: Metadata
  resources: ["pods"]
```

## Real-World Examples

### Example 1: Multi-Tier Application Security
```yaml
# Namespace for production
---
apiVersion: v1
kind: Namespace
metadata:
  name: production
  labels:
    name: production

---
# Default deny all
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: default-deny-all
  namespace: production
spec:
  podSelector: {}
  policyTypes:
  - Ingress
  - Egress

---
# Frontend can accept traffic from ingress
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-frontend-ingress
  namespace: production
spec:
  podSelector:
    matchLabels:
      tier: frontend
  policyTypes:
  - Ingress
  ingress:
  - from:
    - namespaceSelector:
        matchLabels:
          name: ingress-nginx
    ports:
    - protocol: TCP
      port: 80
    - protocol: TCP
      port: 443

---
# Frontend can call backend
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-frontend-to-backend
  namespace: production
spec:
  podSelector:
    matchLabels:
      tier: backend
  policyTypes:
  - Ingress
  ingress:
  - from:
    - podSelector:
        matchLabels:
          tier: frontend
    ports:
    - protocol: TCP
      port: 8080

---
# Backend can call database
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-backend-to-db
  namespace: production
spec:
  podSelector:
    matchLabels:
      tier: database
  policyTypes:
  - Ingress
  ingress:
  - from:
    - podSelector:
        matchLabels:
          tier: backend
    ports:
    - protocol: TCP
      port: 5432
```

### Example 2: Istio Authorization Policy
```yaml
# Allow payment service to receive traffic from order service
apiVersion: security.istio.io/v1beta1
kind: AuthorizationPolicy
metadata:
  name: allow-order-to-payment
  namespace: production
spec:
  selector:
    matchLabels:
      service: payment
  action: ALLOW
  rules:
  - from:
    - source:
        principals: ["cluster.local/ns/production/sa/order"]
    to:
    - operation:
        methods: ["POST"]
        paths: ["/api/payments*"]

---
# Deny all by default
apiVersion: security.istio.io/v1beta1
kind: AuthorizationPolicy
metadata:
  name: default-deny
  namespace: production
spec:
  {}
```

### Example 3: Egress to External Service
```yaml
# Allow pod to call external API
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-external-api
  namespace: production
spec:
  podSelector:
    matchLabels:
      app: worker
  policyTypes:
  - Egress
  egress:
  # Allow DNS
  - to:
    - namespaceSelector: {}
    ports:
    - protocol: UDP
      port: 53
  # Allow HTTPS to external API
  - to:
    - podSelector: {}
    ports:
    - protocol: TCP
      port: 443

---
# Istio ServiceEntry for external service
apiVersion: networking.istio.io/v1beta1
kind: ServiceEntry
metadata:
  name: external-payment-api
  namespace: production
spec:
  hosts:
  - api.payment-provider.com
  ports:
  - number: 443
    name: https
    protocol: HTTPS
  location: MESH_EXTERNAL
  resolution: DNS
```

## Best Practices
- ✅ Start with default deny
- ✅ Use specific selectors (labels, namespaces)
- ✅ Enforce mTLS everywhere
- ✅ Monitor network policies
- ✅ Test policies before production
- ✅ Document network topology
- ✅ Audit policy changes
- ❌ Don't use overly permissive rules
- ❌ Don't mix network policies with API auth
- ❌ Don't forget DNS traffic

## Advanced Patterns

### Network Policy Debugging
```bash
# Check if policy is applied
kubectl get networkpolicies -n production

# Check pod connectivity
kubectl run debug --image=nicolaka/netshoot -it --rm -- bash

# Test connection
kubectl exec -it pod-name -- nc -zv service-name 8080

# View policy selector
kubectl describe networkpolicy policy-name -n production
```

### Cilium for Advanced Networking
```yaml
# Install Cilium CNI
helm repo add cilium https://helm.cilium.io
helm install cilium cilium/cilium --namespace kube-system

---
# Cilium NetworkPolicy with DNS
apiVersion: cilium.io/v2
kind: CiliumNetworkPolicy
metadata:
  name: allow-github-api
spec:
  endpointSelector: {}
  egress:
  - toEndpoints:
    - matchLabels:
        k8s:io.kubernetes.pod.namespace: kube-system
    toPorts:
    - ports:
      - port: "53"
        protocol: UDP
    rules:
      dns:
      - matchPattern: "api.github.com"
```

## Metrics to Track
- Denied connections per pod
- Network policy violations
- mTLS certificate expiry
- Egress traffic volume
- Policy update latency

## Common Pitfalls
1. **Too permissive policies**: No real security
2. **No DNS allowed**: Pods can't resolve names
3. **Forgetting egress rules**: Pods can't reach external services
4. **No monitoring**: Can't detect attacks
5. **Policy conflicts**: Last rule wins

## Tools
- Calico / Cilium / Weave (CNI plugins)
- Istio (service mesh)
- Kubernetes Network Policy
- Falco (runtime security)

## Related Skills
- devops-kubernetes-cluster-setup
- security-tls-certificates-ssl
- devops-monitoring-alerting-prometheus
