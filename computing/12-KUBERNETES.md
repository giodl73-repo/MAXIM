# 12 — Kubernetes

## The Big Picture

```
The Problem Docker Alone Doesn't Solve
========================================

Docker gives you containers. It doesn't give you:

  ✗ "Run 5 copies of this container"
  ✗ "Restart it if it crashes"
  ✗ "Roll out a new version without downtime"
  ✗ "Route traffic only to healthy instances"
  ✗ "Give container A 2 CPU cores, container B 512MB RAM"
  ✗ "Store my database password securely"

Kubernetes (K8s) solves all of that.
It is a container orchestrator — a platform that runs containers
at scale, keeps them healthy, and manages their networking and config.
```

```
Kubernetes — Full Architecture
================================

  ┌─────────────────────────────────────────────────────────────────────┐
  │  Cluster                                                            │
  │                                                                     │
  │  ┌──────────────────────────────┐                                   │
  │  │  Control Plane               │    kubectl  ──►  API Server       │
  │  │                              │                                   │
  │  │  API Server                  │    You talk to the API Server.    │
  │  │  etcd (state store)          │    Everything else is internal.   │
  │  │  Scheduler                   │                                   │
  │  │  Controller Manager          │                                   │
  │  └──────────────────────────────┘                                   │
  │                                                                     │
  │  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐              │
  │  │  Node (VM)   │  │  Node (VM)   │  │  Node (VM)   │              │
  │  │              │  │              │  │              │              │
  │  │  kubelet     │  │  kubelet     │  │  kubelet     │              │
  │  │  kube-proxy  │  │  kube-proxy  │  │  kube-proxy  │              │
  │  │              │  │              │  │              │              │
  │  │  [Pod]       │  │  [Pod][Pod]  │  │  [Pod]       │              │
  │  └──────────────┘  └──────────────┘  └──────────────┘              │
  │                                                                     │
  └─────────────────────────────────────────────────────────────────────┘

  Control Plane = the brain (managed by cloud provider in AKS/EKS/GKE)
  Node = a VM that runs your containers
  Pod = smallest deployable unit (one or more containers)
  kubelet = agent on each node that talks to control plane
```

<!-- @editor[diagram/P1]: Missing K8s object relationship landscape diagram. The calibration note is explicit: "K8s objects (Pod/ReplicaSet/Deployment/Service/Ingress/ConfigMap/Secret) need a landscape diagram showing the relationship between objects." The cluster architecture diagram above shows physical topology (nodes, control plane) but not the logical object hierarchy. A second diagram showing Deployment → ReplicaSet → Pod with Service pointing at Pods, Ingress pointing at Service, ConfigMap/Secret injected into Pod — this is what the learner needs to orient to the object model before drilling into each. Place between the intro and the first ##. -->

<!-- @editor[bridge/P1]: No Azure Service Fabric bridge. The calibration note flags this as a primary bridge: the learner knows Service Fabric (Microsoft's internal orchestrator). The concepts map directly: Service Fabric Application → K8s Deployment; Service Fabric Service → K8s Service; Service Fabric partition → K8s ReplicaSet; Service Fabric health model → readinessProbe/livenessProbe; SF upgrade domains → rolling update strategy. This is the single strongest anchor for this learner and it's completely absent. A named comparison table or bridge box belongs here at the intro, before the Core Concepts section. -->

---

## Core Concepts — Bottom Up

### Pod

The atomic unit. A Pod wraps one or more containers that share a network namespace and storage. Almost always one container per pod in practice.

```
Pod
───
┌──────────────────────────────────┐
│  ip: 10.244.1.5                  │
│  ┌────────────────┐              │
│  │  Container     │              │
│  │  image: myapp  │              │
│  │  port: 3000    │              │
│  └────────────────┘              │
│  Volumes (shared by containers)  │
└──────────────────────────────────┘

Pods are ephemeral. When a pod dies, it's gone.
Its IP is gone. Any state written to the container layer is gone.
Never rely on a pod's identity or IP directly — use Services.
```

### Deployment

A Deployment manages a set of identical Pods (a ReplicaSet). You declare desired state; K8s makes it so — and keeps it so.

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: api
spec:
  replicas: 3                         # keep 3 pods running at all times
  selector:
    matchLabels:
      app: api
  template:
    metadata:
      labels:
        app: api                      # pods get this label
    spec:
      containers:
        - name: api
          image: myregistry.azurecr.io/myapp:v1.2.3
          ports:
            - containerPort: 3000
          resources:
            requests:
              memory: "128Mi"         # what it's guaranteed
              cpu: "250m"             # 250 millicores = 0.25 CPU
            limits:
              memory: "256Mi"         # hard ceiling
              cpu: "500m"
          readinessProbe:             # only route traffic when this passes
            httpGet:
              path: /health
              port: 3000
            initialDelaySeconds: 5
            periodSeconds: 10
          livenessProbe:              # restart if this fails
            httpGet:
              path: /health
              port: 3000
            failureThreshold: 3
```

```
Deployment → manages → ReplicaSet → manages → Pods

  Deployment
  ├── replicas: 3
  └── ReplicaSet
      ├── Pod (api-7d8f9b-abc)
      ├── Pod (api-7d8f9b-def)
      └── Pod (api-7d8f9b-xyz)

  If a pod dies → ReplicaSet creates a replacement
  If you update the image → Deployment creates new ReplicaSet, drains old one
```

### Service

Pods come and go. Services give you a stable DNS name and IP that load-balances across all matching pods.

```yaml
apiVersion: v1
kind: Service
metadata:
  name: api
spec:
  selector:
    app: api                          # routes to all pods with label app=api
  ports:
    - port: 80                        # service port
      targetPort: 3000                # container port
  type: ClusterIP                     # internal only (default)
```

```
Service types:

  ClusterIP    Internal to cluster only. Default. Use for service-to-service.
               http://api  (other pods reach it by service name)

  NodePort     Exposes on a port on every node. Used for testing.
               External → NodeIP:30080 → Service → Pods

  LoadBalancer Creates a cloud load balancer (Azure LB, AWS ELB).
               External → public IP → Service → Pods
               This is how you expose a public API.
```

### Ingress

A LoadBalancer Service gives one IP per service — expensive. Ingress puts a single HTTP router in front of many services.

```
                        Ingress Controller (nginx / Traefik / AGIC)
                        ┌──────────────────────────────────────────┐
  internet              │                                          │
  ──────────►  :443     │  /api/*     →  api-service:80            │
                        │  /auth/*    →  auth-service:80           │
                        │  /static/*  →  cdn or static-service     │
                        └──────────────────────────────────────────┘
```

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: main
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
spec:
  rules:
    - host: myapp.example.com
      http:
        paths:
          - path: /api
            pathType: Prefix
            backend:
              service:
                name: api
                port:
                  number: 80
```

<!-- @editor[bridge/P2]: No bridge from Application Gateway / ARR (IIS Application Request Routing) to Ingress. The learner configured ARR and URL rewriting in IIS extensively. Ingress is the same concept: a reverse proxy with URL-based routing rules sitting in front of backend services. AGIC (Application Gateway Ingress Controller) is literally "use Azure Application Gateway as your K8s Ingress" — this is the exact bridge and it gets only a mention in the AKS integrations list rather than a named explanation here where the learner would benefit most. -->

### ConfigMap & Secret

```yaml
# ConfigMap — non-sensitive config
apiVersion: v1
kind: ConfigMap
metadata:
  name: api-config
data:
  NODE_ENV: production
  LOG_LEVEL: info

---
# Secret — base64-encoded sensitive values
apiVersion: v1
kind: Secret
metadata:
  name: api-secrets
type: Opaque
data:
  DATABASE_URL: cG9zdGdyZXM6Ly8...   # base64 of actual value
```

```yaml
# Reference in Deployment
envFrom:
  - configMapRef:
      name: api-config
  - secretRef:
      name: api-secrets

# Or mount as files (good for TLS certs, JSON key files)
volumes:
  - name: secrets-vol
    secret:
      secretName: api-secrets
volumeMounts:
  - name: secrets-vol
    mountPath: /etc/secrets
    readOnly: true
```

Note: Secrets are base64-encoded, not encrypted by default. In production use Azure Key Vault + CSI driver, AWS Secrets Manager, or Sealed Secrets — something that keeps the real value out of git.

### Namespace

Logical isolation within a cluster. Like a folder. Team A and Team B can run services with the same name in different namespaces.

```bash
kubectl get pods -n production
kubectl get pods -n staging
kubectl get pods --all-namespaces
```

Default namespace is `default`. Don't use it in production — name your namespaces.

---

## Persistent Storage

Containers are stateless. Databases need durable storage that outlives pods.

```yaml
# PersistentVolumeClaim — request storage
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: postgres-pvc
spec:
  accessModes:
    - ReadWriteOnce           # one pod at a time (most block storage)
  resources:
    requests:
      storage: 20Gi
  storageClassName: managed-premium   # Azure Premium SSD

---
# Use in a Pod
volumes:
  - name: postgres-storage
    persistentVolumeClaim:
      claimName: postgres-pvc
volumeMounts:
  - name: postgres-storage
    mountPath: /var/lib/postgresql/data
```

For stateful apps (databases, message queues), prefer **StatefulSet** over Deployment — it gives pods stable identities and ordered startup/shutdown.

---

## Rolling Updates & Rollbacks

```
Rolling Update (default strategy)
==================================

  Before:  [v1] [v1] [v1]

  Step 1:  [v2] [v1] [v1]   ← one new pod, one old removed
  Step 2:  [v2] [v2] [v1]
  Step 3:  [v2] [v2] [v2]   ← zero downtime

  Each new pod must pass readinessProbe before traffic shifts
```

```bash
# Trigger a rollout (update image)
kubectl set image deployment/api api=myapp:v1.3.0

# Watch rollout progress
kubectl rollout status deployment/api

# Undo last rollout
kubectl rollout undo deployment/api

# Roll back to specific revision
kubectl rollout history deployment/api
kubectl rollout undo deployment/api --to-revision=2
```

---

## Horizontal Pod Autoscaler (HPA)

Scale pod count automatically based on CPU/memory or custom metrics.

```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: api-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: api
  minReplicas: 2
  maxReplicas: 20
  metrics:
    - type: Resource
      resource:
        name: cpu
        target:
          type: Utilization
          averageUtilization: 70    # scale up when avg CPU > 70%
```

---

## Key kubectl Commands

```bash
# Context / cluster management
kubectl config get-contexts            # list clusters you can talk to
kubectl config use-context my-cluster  # switch cluster

# Inspect
kubectl get pods                       # pods in default namespace
kubectl get pods -n production         # specific namespace
kubectl get pods -o wide               # show node, IP
kubectl get all                        # pods, services, deployments, etc.
kubectl describe pod api-7d8f9b-abc    # full detail + events (use for debugging)
kubectl get events --sort-by=.metadata.creationTimestamp

# Logs
kubectl logs api-7d8f9b-abc            # pod logs
kubectl logs -f api-7d8f9b-abc         # follow
kubectl logs deployment/api            # logs from any pod in deployment
kubectl logs deployment/api --previous # previous container (after crash)

# Debug
kubectl exec -it api-7d8f9b-abc -- sh  # shell into pod
kubectl port-forward pod/api-7d8f9b-abc 3000:3000   # local access to pod
kubectl port-forward service/api 3000:80             # local access via service

# Apply / delete
kubectl apply -f deployment.yaml       # create or update
kubectl apply -f ./k8s/               # apply all files in directory
kubectl delete -f deployment.yaml
kubectl delete pod api-7d8f9b-abc      # K8s will recreate it via Deployment

# Scale manually
kubectl scale deployment api --replicas=5
```

---

## Managed Kubernetes (AKS, EKS, GKE)

You almost never run your own control plane. Cloud providers manage it.

```
Self-managed K8s                   AKS / EKS / GKE
================                   ================

You manage:                        You manage:
  Control plane VMs                  Node pools (VMs)
  etcd backups                       Your workloads
  K8s upgrades                       kubectl access
  HA setup

Provider manages:                  Provider manages:
  (nothing — it's all you)           Control plane
                                     etcd
                                     API server HA
                                     K8s version upgrades (optional)
                                     Cloud LB integration
                                     Storage class provisioners
```

### Azure Kubernetes Service (AKS)

```bash
# Create cluster (via CLI)
az aks create \
  --resource-group myRG \
  --name myAKS \
  --node-count 3 \
  --node-vm-size Standard_D4s_v3 \
  --generate-ssh-keys

# Get credentials (populates ~/.kube/config)
az aks get-credentials --resource-group myRG --name myAKS

# Now use kubectl normally
kubectl get nodes
```

Key AKS integrations:
- **ACR pull**: attach your ACR so nodes can pull private images without credentials
- **Managed Identity**: pods get Azure identities via Workload Identity — no secrets
- **Azure Monitor**: container insights, log analytics
- **AGIC**: Application Gateway Ingress Controller (Azure LB as ingress)

<!-- @editor[bridge/P1]: Missing Azure Container Apps comparison. The calibration note specifically calls out: "AKS, Azure Container Apps, and Service Fabric comparisons are bridges worth making." Azure Container Apps (ACA) is K8s with the operational complexity abstracted — no nodes to manage, no kubectl required, built on KEDA for scale-to-zero. For the learner's context (Azure App Service → containerization), ACA is often the right answer before AKS. The decision boundary (ACA vs AKS) belongs here in the Managed Kubernetes section as a named comparison. -->

---

## Helm — Package Manager for K8s

Raw YAML gets unwieldy fast. Helm is to Kubernetes what npm is to Node.js.

```
Helm Chart
==========
A packaged set of K8s manifests with templating.

chart/
├── Chart.yaml          name, version, description
├── values.yaml         default values
└── templates/
    ├── deployment.yaml
    ├── service.yaml
    └── ingress.yaml

The templates use Go templating:
  replicas: {{ .Values.replicaCount }}
  image: {{ .Values.image.repository }}:{{ .Values.image.tag }}
```

```bash
# Install a chart (e.g., nginx ingress controller)
helm repo add ingress-nginx https://kubernetes.github.io/ingress-nginx
helm install my-ingress ingress-nginx/ingress-nginx

# Install your own chart with custom values
helm install myapp ./chart --values prod-values.yaml

# Upgrade a release
helm upgrade myapp ./chart --values prod-values.yaml

# Rollback
helm rollback myapp 1

# List releases
helm list

# Delete
helm uninstall myapp
```

---

## Common Confusion Points

**Pod vs Deployment.**
You'll rarely create a Pod directly. You create a Deployment, which creates a ReplicaSet, which creates Pods. If you `kubectl delete pod api-xyz`, K8s immediately creates a replacement. To remove pods, delete the Deployment.

**Why is my pod in `CrashLoopBackOff`?**
The container is starting and immediately exiting. The process inside is crashing. First step: `kubectl logs deployment/api --previous` to see the last crash's stdout. Usually a missing env var, bad config, or unhandled startup error.

**Why is my pod in `Pending`?**
It can't be scheduled. Common causes: not enough CPU/memory on any node (`kubectl describe pod` → Events section), or PVC can't bind (storage class issue).

**`kubectl apply` vs `kubectl create`.**
`create` fails if the resource already exists. `apply` creates or updates. Always use `apply` in CI/CD.

**Services and DNS inside the cluster.**
A Service named `api` in namespace `production` is reachable at:
- `api` from within the same namespace
- `api.production` from another namespace
- `api.production.svc.cluster.local` (FQDN)

**Requests vs Limits.**
`requests` = what the scheduler uses to place the pod (guaranteed). `limits` = hard ceiling (container is killed/throttled if exceeded). Set both. A pod with no limits can consume an entire node and starve neighbors.

**Secrets are not encrypted by default.**
They're base64-encoded in etcd. Treat K8s Secrets as a transport mechanism, not a vault. In production, use cloud secrets stores (Azure Key Vault, AWS Secrets Manager) with the CSI driver.

---

## Old World Bridge

| Azure / Windows / VSTS Concept | Kubernetes Equivalent |
|---|---|
| Azure App Service Plan (scale units) | Node Pool |
| Azure App Service (web app) | Deployment + Service |
| Deployment slot (staging) | Separate namespace or separate Deployment |
| App Service autoscale rules | HorizontalPodAutoscaler (HPA) |
| Azure Load Balancer | Service (type: LoadBalancer) |
| Application Gateway + URL routing | Ingress + Ingress Controller |
| web.config / App Settings | ConfigMap + Secret + envFrom |
| Azure Key Vault | K8s Secret + CSI driver → Azure Key Vault |
| Azure Container Registry | Image registry (pull in pod spec) |
| Azure Monitor / App Insights | Prometheus + Grafana + OpenTelemetry (15-OBSERVABILITY) |
| VSTS Release Pipeline stages | kubectl apply in CI/CD pipeline (13-CICD) |
| Blue/green deployment | Two Deployments + Service selector switch |

<!-- @editor[bridge/P1]: The Old World Bridge table is missing Service Fabric entirely. The calibration note calls it out explicitly as a primary bridge. The learner built systems on Service Fabric — it is Microsoft's own container/microservice orchestrator. The mapping: SF cluster → K8s cluster; SF application → K8s namespace; SF service → K8s Deployment + Service; SF partition → ReplicaSet; SF health model (primary/secondary) → readinessProbe/livenessProbe; SF upgrade domains → rolling update maxUnavailable/maxSurge; SF named partitions → StatefulSet. This is the most relevant old-world anchor for this entire guide and it's absent from the bridge table. -->

---

## Decision Cheat Sheet

| I want to... | Use |
|---|---|
| Run containers at scale with automatic restarts | Kubernetes Deployment |
| Expose a service inside the cluster | Service (ClusterIP) |
| Expose a service to the internet | Service (LoadBalancer) or Ingress |
| Route traffic to multiple services via URL paths | Ingress |
| Store non-secret config (env vars) | ConfigMap |
| Store secrets (DB passwords, API keys) | Secret (+ Key Vault in prod) |
| Persist database data across pod restarts | PersistentVolumeClaim + StatefulSet |
| Auto-scale based on CPU | HorizontalPodAutoscaler |
| Deploy without downtime | Rolling update (default Deployment strategy) |
| Roll back a bad deploy | `kubectl rollout undo` |
| Package and version K8s manifests | Helm chart |
| Isolate teams or environments in one cluster | Namespaces |
| Run K8s without managing control plane | AKS / EKS / GKE |
| Run K8s serverlessly (no node management) | AKS with Virtual Nodes / Fargate |
| Debug a crashing pod | `kubectl logs --previous` + `kubectl describe pod` |

<!-- @editor[structure/P2]: Missing AKS vs Azure Container Apps vs Service Fabric decision row in the cheat sheet. The calibration note flags the decision between these three as primary value for this learner. The cheat sheet has "Run K8s without managing control plane → AKS" but no "I want App-Service-like simplicity with containers → Azure Container Apps" or "I'm already on Service Fabric, should I migrate → ?" row. These are the decisions this learner will actually face. -->
