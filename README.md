# mlops-pytorch-pipeline
# Repository Creation
Repository created mlops-pytorch-pipeline

The project directory is initialised with the following structure: 

mlops-pytorch-pipeline/ 

··· README.md 

··· src/ 

· ··· train.py 

· ··· model.py 

· ··· dataset.py 

· ··· serve.py 

··· configs/

· ··· training_config.yaml

··· docker/

· ··· Dockerfile.train 

· ··· Dockerfile.serve 

··· k8s/ 

· ··· namespace.yaml 

· ··· training-job.yaml 

· ··· serving-deployment.yaml 

· ··· serving-service.yaml 

· ··· configmap.yaml 

· ··· hpa.yaml 

··· requirements/ 

· ··· train.txt 

· ··· serve.txt 

All files are merged to 'main' branch via pull requests.


# Docker Results

**Docker build docker train**

C:\Users\nitis\Desktop\mlops-pytorch-pipeline>docker build -f docker/Dockerfile.train -t mlops-train:v1 .

[+] Building 70.3s (14/14) FINISHED docker:desktop-linux

=> [internal] load build definition from Dockerfile.train 0.1s

=> => transferring dockerfile: 770B 0.0s

=> [internal] load metadata for docker.io/library/python:3.11-slim 0.1s

=> [internal] load .dockerignore 0.0s

=> => transferring context: 2B 0.0s

=> [builder 1/5] FROM docker.io/library/python:3.11-slim@sha256:b27df5841f3355e9473f9a516d38a6783b6c8dfeacaf2d14 0.0s

=> => resolve docker.io/library/python:3.11-slim@sha256:b27df5841f3355e9473f9a516d38a6783b6c8dfeacaf2d14a240f443 0.0s

=> [internal] load build context 0.1s

=> => transferring context: 6.96kB 0.0s

=> CACHED [builder 2/5] WORKDIR /app 0.0s

=> [builder 3/5] RUN apt-get update && apt-get install -y --no-install-recommends build-essential && rm 17.4s

=> [builder 4/5] COPY requirements/train.txt . 0.1s

=> [builder 5/5] RUN pip install --no-cache-dir --user -r train.txt 23.6s

=> [training 3/6] COPY --from=builder /root/.local /root/.local 3.0s

=> [training 4/6] COPY src/ ./src/ 0.2s

=> [training 5/6] COPY configs/ ./configs/ 0.1s

=> [training 6/6] RUN mkdir -p /app/data /app/checkpoints 0.3s

=> exporting to image 23.9s

=> => exporting layers 17.3s

=> => exporting manifest sha256:06c0410022b9e4824963af1cb5fa821cf35f4de0884216f823e4dab4ead35513 0.0s

=> => exporting config sha256:a0e256506fbcf1657dc595c876bad9d2523abb482343ff708768413ebbff6d75 0.0s

=> => exporting attestation manifest sha256:d6c6c1a0332576109524abfb1e099bfaed224f4c10c6247bce567b7124ffa388 0.0s

=> => exporting manifest list sha256:f0472a187541596cab458b0c7af112285cc74a557cfcd795ac9a61ca7b1bdc3d 0.0s

=> => naming to docker.io/library/mlops-train:v1 0.0s

=> => unpacking to docker.io/library/mlops-train:v1 6.4s

View build details: docker-desktop://dashboard/build/desktop-linux/desktop-linux/z3rx3fodvi91co96tqhhtxrjt


**Docker run docker_train**

C:\Users\nitis\Desktop\mlops-pytorch-pipeline>docker run --rm -e PYTHONPATH=/app mlops-train:v1

Downloading https://cave.cs.toronto.edu/kriz/cifar-10-python.tar.gz to ./data/cifar-10-python.tar.gz
100.0%

Extracting ./data/cifar-10-python.tar.gz to ./data

Files already downloaded and verified

{"epoch": 1, "train_loss": 1.6173385976791381, "train_acc": 0.407125, "val_loss": 1.4954723567962647, "val_acc": 0.4614}

{"epoch": 2, "train_loss": 1.2633779099464417, "train_acc": 0.547525, "val_loss": 1.2328836559295655, "val_acc": 0.5627}

{"epoch": 3, "train_loss": 1.0905128046035766, "train_acc": 0.613325, "val_loss": 1.219293517971039, "val_acc": 0.5783}

{"epoch": 4, "train_loss": 0.9813409231185913, "train_acc": 0.6572, "val_loss": 0.94351400680542, "val_acc": 0.6724}

{"epoch": 5, "train_loss": 0.9032020175933838, "train_acc": 0.683775, "val_loss": 0.972112654876709, "val_acc": 0.6571}

{"epoch": 6, "train_loss": 0.8430239446163178, "train_acc": 0.70455, "val_loss": 0.8373573637008667, "val_acc": 0.7056}

{"epoch": 7, "train_loss": 0.7915509615898132, "train_acc": 0.725875, "val_loss": 0.7784155526161194, "val_acc": 0.7231}

{"epoch": 8, "train_loss": 0.7525458303928375, "train_acc": 0.739475, "val_loss": 0.7517169303894043, "val_acc": 0.7374}

{"epoch": 9, "train_loss": 0.7141366448879242, "train_acc": 0.751325, "val_loss": 0.737249662399292, "val_acc": 0.7436}

{"epoch": 10, "train_loss": 0.6854890860080719, "train_acc": 0.7621, "val_loss": 0.7164984763145447, "val_acc": 0.7522}


**Docker build docker_serve**

C:\Users\nitis\Desktop\mlops-pytorch-pipeline>docker build -f docker/Dockerfile.serve -t mlops-serve:v1 .

[+] Building 52.2s (12/12) FINISHED docker:desktop-linux

=> [internal] load build definition from Dockerfile.serve 0.0s

=> => transferring dockerfile: 790B 0.0s

=> [internal] load metadata for docker.io/library/python:3.11-slim 0.1s

=> [internal] load .dockerignore 0.0s

=> => transferring context: 2B 0.0s

=> [1/7] FROM docker.io/library/python:3.11-slim@sha256:b27df5841f3355e9473f9a516d38a6783b6c8dfeacaf2d14a240f443b368ddb6 0.0s

=> => resolve docker.io/library/python:3.11-slim@sha256:b27df5841f3355e9473f9a516d38a6783b6c8dfeacaf2d14a240f443b368ddb6 0.0s

=> [internal] load build context 0.0s

=> => transferring context: 491B 0.0s

=> CACHED [2/7] WORKDIR /app 0.0s

=> [3/7] RUN useradd -u 8888 -m appuser && mkdir -p /app/checkpoints && chown -R appuser:appuser /app 0.4s

=> [4/7] COPY --chown=appuser:appuser requirements/serve.txt . 0.1s

=> [5/7] RUN pip install --no-cache-dir --user -r serve.txt 27.3s

=> [6/7] COPY --chown=appuser:appuser src/ ./src/ 0.2s

=> [7/7] COPY --chown=appuser:appuser configs/ ./configs/ 0.1s

=> exporting to image 23.8s

=> => exporting layers 17.2s

=> => exporting manifest sha256:9852d228744831d998dc5b9c62a0b9b5af56b4414428acec275c5d664e9e94a1 0.0s

=> => exporting config sha256:4dd97ce18001dcaa811c8a9cd452a0b40c61a8fcbc06ebd17f2b36fc5ea4f32b 0.0s

=> => exporting attestation manifest sha256:a8093ee52a1fb330b29c052c9d52b270dd151975218a1bc4345a82b9365e6bdf 0.0s

=> => exporting manifest list sha256:176c8c56d8e3411e8f3a7b5c9e69e1bc9f979d431d66b9073b7b4c1c314e4774 0.0s

=> => naming to docker.io/library/mlops-serve:v1 0.0s

=> => unpacking to docker.io/library/mlops-serve:v1 6.4s

View build details: docker-desktop://dashboard/build/desktop-linux/desktop-linux/jo5s4oxtayoa2m4f3p3ehhsdp


**Docker run docker_serve**

PS C:\Users\nitis\Desktop\mlops-pytorch-pipeline> docker run --rm -e PYTHONPATH=/app mlops-serve:v1

INFO: Started server process [1]

INFO: Waiting for application startup.

/app/src/serve.py:34: FutureWarning: You are using torch.load with weights_only=False (the current default value), which uses the default pickle module implicitly. It is possible to construct malicious pickle data which will execute arbitrary code during unpickling (See https://github.com/pytorch/pytorch/blob/main/SECURITY.md#untrusted-models for more details). In a future release, the default value for weights_only will be flipped to True. This limits the functions that could be executed during unpickling. Arbitrary objects will no longer be allowed to be loaded via this mode unless they are explicitly allowlisted by the user via torch.serialization.add_safe_globals. We recommend you start setting weights_only=True for any use case where you don't have full control of the loaded file. Please open an issue on GitHub for any issues related to this experimental feature.
model.load_state_dict(torch.load("/app/checkpoints/best_model.pth", map_location=device))

INFO: Application startup complete.

INFO: Uvicorn running on http://0.0.0.0:8080 (Press CTRL+C to quit)


# k8s Results

**Namespace**

PS C:\Users\nitis\Desktop\mlops-pytorch-pipeline> kubectl apply -f k8s/namespace.yaml

namespace/ml-training created

PS C:\Users\nitis\Desktop\mlops-pytorch-pipeline> kubectl describe namespace ml-training

Name:         ml-training

Labels:       framework=pytorch
              kubernetes.io/metadata.name=ml-training
              project=mlops-pytorch-pipeline
              type=pipeline

Annotations:  <none>

Status:       Active

No resource quota.

No LimitRange resource.


**Configmap**

PS C:\Users\nitis\Desktop\mlops-pytorch-pipeline> kubectl apply -f k8s/configmap.yaml   

configmap/training-config created

PS C:\Users\nitis\Desktop\mlops-pytorch-pipeline> kubectl describe configmap -n ml-training

Name:         kube-root-ca.crt

Namespace:    ml-training

Labels:       <none>

Annotations:  kubernetes.io/description:
                Contains a CA bundle that can be used to verify the kube-apiserver when using internal endpoints such as the internal service IP or kubern...

-----BEGIN CERTIFICATE-----
MIIDBTCCAe2gAwIBAgIIAmCN+qDBBhwwDQYJKoZIhvcNAQELBQAwFTETMBEGA1UE
AxMKa3ViZXJuZXRlczAeFw0yNjA4MjYxMDUwMjhaFw0zNjA4MjMxMDU1MjhaMBUx
EzARBgNVBAMTCmt1YmVybmV0ZXMwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEK
AoIBAQDVxfd9jsDu4n8zwMpkqhkl2vMacWs0l+DfS/H8rSoVHQePrkPShSh+tMPL
TPwiLl/tXv85KQ9XX3YAAGG4NVGjb54WwoP2BR6+afafPVrRJrjvexFSiJ9kw6cu
K908Y4b4AEBapJqoqL5CvWQmzYbI4Ce3NzBXZAnpIBx6MHUPlumFid4c8ca7w5qu
eZaUXbRMSCYVkVEeFZ5yJg24N5stAyh83C3kZU1OalnfU2Zf+/qUnlUYI3lufAmn
vytpJxeLcZPkLMGisriSkZ2vDoXr6WDNMgWHR1QP+D8rCXXCUHYb/eECDBj2runN
8YbmEwzpZJjzl1CmYYCvVoxW9GKfAgMBAAGjWTBXMA4GA1UdDwEB/wQEAwICpDAP
BgNVHRMBAf8EBTADAQH/MB0GA1UdDgQWBBRFZ/O72lhsqvuYnqz/XBMSorgflDAV
BgNVHREEDjAMggprdWJlcm5ldGVzMA0GCSqGSIb3DQEBCwUAA4IBAQC0IUHjCK1v
X7YBXIV8u4Y4Xaa5vaVGAjJNNFjmcTY8q6Yr6DvIyC4ncqrQUdqOg2hXtsGo1fYJ
yUsgkP377k1hnNjipyjzHuVLSlOqVyBs8ofBSVZ2gt+Lod449JYlxgYfL8s1HKRN
NkbFLTi0Rjqf2a4npGIl0O1QOPiCPPJnTK+dVp/DUd5FUBgopYUJURuaUDh510pI
pPQ2pC/BZ+hqz0qZn49lc3yCRMKtWZNhumTZe4pQ5aieiDpbtGZh5PtmNSXLGd+4
UODFcUNd3APkj+ddDxTvDT2bAWiFxvypCqEiRN7QpPdqyoWe2vBCR81rRmMvZARe
wGBSKguhMyv2
-----END CERTIFICATE-----



Name:         training-config

Namespace:    ml-training

Labels:       <none>

Annotations:  <none>

training_config.yaml:

----

model:
  architecture: resnet18
  num_classes: "10"

training:
  epochs: "10"
  batch_size: "64"
  learning_rate: "0.001"
  early_stopping_patience: "3"

data:
  dataset: cifar10
  data_dir: /app/data

output:
  checkpoint_dir: /app/checkpoints
  model_name: classifier_v1.pt



**k8s Training**

PS C:\Users\nitis\Desktop\mlops-pytorch-pipeline> kubectl apply -f k8s/training-job.yaml

job.batch/ml-training-job created

PS C:\Users\nitis\Desktop\mlops-pytorch-pipeline> kubectl describe job -n ml-training      

Name:             ml-training-job

Namespace:        ml-training

Selector:         batch.kubernetes.io/controller-uid=8741b430-4611-4dfa-b620-d6d361d82238

Labels:           batch.kubernetes.io/controller-uid=8741b430-4611-4dfa-b620-d6d361d82238
                  batch.kubernetes.io/job-name=ml-training-job
                  controller-uid=8741b430-4611-4dfa-b620-d6d361d82238
                  job-name=ml-training-job

Annotations:      <none>

Parallelism:      1

Completions:      1

Completion Mode:  NonIndexed

Suspend:          false

Backoff Limit:    2

Start Time:       Wed, 26 Aug 2026 18:48:18 +0530

Pods Statuses:    1 Active (0 Ready) / 0 Succeeded / 0 Failed

Pod Template:
  
  Labels:  batch.kubernetes.io/controller-uid=8741b430-4611-4dfa-b620-d6d361d82238
           batch.kubernetes.io/job-name=ml-training-job
           controller-uid=8741b430-4611-4dfa-b620-d6d361d82238
           job-name=ml-training-job
  
  Containers:
   
   trainer:
    Image:      mlops-train:v1
    Port:       <none>
    Host Port:  <none>
    Limits:
      cpu:             2
      memory:          4Gi
      nvidia.com/gpu:  1
    Requests:
      cpu:             2
      memory:          4Gi
      nvidia.com/gpu:  1
    Environment:
      TRAINING_CONFIG_PATH:  /app/configs/training_config.yaml
    Mounts:
      /app/checkpoints from storage-volume (rw,path="checkpoints")
      /app/configs from config-volume (rw)
      /app/data from storage-volume (rw,path="data")
  
  Volumes:
   config-volume:
    Type:      ConfigMap (a volume populated by a ConfigMap)
    Name:      training-config
    Optional:  false
   storage-volume:
    Type:          PersistentVolumeClaim (a reference to a PersistentVolumeClaim in the same namespace)
    ClaimName:     ml-storage-pvc
    ReadOnly:      false
  
  Node-Selectors:  accelerator=nvidia-gpu
  
  Tolerations:     nvidia.com/gpu:NoSchedule op=Exists

Events:            <none>


**k8s Deployment**

PS C:\Users\nitis\Desktop\mlops-pytorch-pipeline> kubectl apply -f k8s/serving-deployment.yaml 

deployment.apps/model-serving created

PS C:\Users\nitis\Desktop\mlops-pytorch-pipeline> kubectl describe deployment -n ml-training

Name:                   model-serving

Namespace:              ml-training

CreationTimestamp:      Wed, 26 Aug 2026 18:48:45 +0530

Labels:                 app=model-serving

Annotations:            deployment.kubernetes.io/revision: 1

Selector:               app=model-serving

Replicas:               2 desired | 2 updated | 2 total | 0 available | 2 unavailable

StrategyType:           RollingUpdate

MinReadySeconds:        0

RollingUpdateStrategy:  0 max unavailable, 1 max surge

Pod Template:
  
  Labels:  app=model-serving
  
  Containers:
   serving-runtime:
    Image:      mlops-serve:v1
    Port:       8080/TCP
    Host Port:  0/TCP
    Limits:
      cpu:     1
      memory:  2Gi
    Requests:
      cpu:        500m
      memory:     1Gi
    Liveness:     http-get http://:8080/health delay=0s timeout=1s period=10s #success=1 #failure=3    
    Readiness:    http-get http://:8080/health delay=15s timeout=1s period=5s #success=1 #failure=3    
    Environment:  <none>
    Mounts:
      /app/checkpoints from checkpoint-volume (ro,path="checkpoints")
  
  Volumes:
   checkpoint-volume:
    Type:          PersistentVolumeClaim (a reference to a PersistentVolumeClaim in the same namespace)
    ClaimName:     ml-storage-pvc
    ReadOnly:      false
  
  Node-Selectors:  <none>
  
  Tolerations:     <none>

Conditions:
  Type           Status  Reason
  ----           ------  ------
  Available      False   MinimumReplicasUnavailable
  Progressing    False   ProgressDeadlineExceeded

OldReplicaSets:  <none>

NewReplicaSet:   model-serving-64dd4cdcd8 (2/2 replicas created)

Events:          <none>


**k8s Service**

PS C:\Users\nitis\Desktop\mlops-pytorch-pipeline> kubectl apply -f k8s/serving-service.yaml

service/model-serving created

PS C:\Users\nitis\Desktop\mlops-pytorch-pipeline> kubectl describe service -n ml-training   

Name:                     model-serving

Namespace:                ml-training

Labels:                   <none>

Annotations:              <none>

Selector:                 app=model-serving

Type:                     ClusterIP

IP Family Policy:         SingleStack

IP Families:              IPv4

IP:                       10.96.55.62

IPs:                      10.96.55.62

Port:                     <unset>  80/TCP

TargetPort:               8080/TCP

Endpoints:

Session Affinity:         None

Internal Traffic Policy:  Cluster

Events:                   <none>


**k8s HPA**

PS C:\Users\nitis\Desktop\mlops-pytorch-pipeline> kubectl apply -f k8s/hpa.yaml

horizontalpodautoscaler.autoscaling/model-serving-hpa created

PS C:\Users\nitis\Desktop\mlops-pytorch-pipeline> kubectl describe hpa -n ml-training   

Name:                                                  model-serving-hpa

Namespace:                                             ml-training

Labels:                                                <none>

Annotations:                                           <none>

CreationTimestamp:                                     Wed, 26 Aug 2026 18:49:35 +0530

Reference:                                             Deployment/model-serving

Metrics:                                               ( current / target )
  resource cpu on pods  (as a percentage of request):  <unknown> / 80%

Min replicas:                                          2

Max replicas:                                          5

Deployment pods:                                       2 current / 0 desired

Conditions:
  
  Type           Status  Reason                   Message
  
  ----           ------  ------                   -------
  
  AbleToScale    True    SucceededGetScale        the HPA controller was able to get the target's current scale
  
  ScalingActive  False   FailedGetResourceMetric  the HPA was unable to compute the replica count: failed to get cpu utilization: unable to get metrics for resource cpu: 
  unable to fetch metrics from resource metrics API: the server could not find the requested resource (get pods.metrics.k8s.io)

Events:

  Type     Reason                   Age                    From                       Message
  
  ----     ------                   ----                   ----                       -------
  
  Warning  FailedGetResourceMetric  2m14s (x857 over 19h)  horizontal-pod-autoscaler  failed to get cpu utilization: unable to get metrics for resource cpu: unable to fetch 
  metrics from resource metrics API: the server could not find the requested resource (get pods.metrics.k8s.io)


**k8s Running PODS**

PS C:\Users\nitis\Desktop\mlops-pytorch-pipeline> kubectl get pods -n ml-training 

NAME                             READY   STATUS      RESTARTS   AGE

ml-training-job-zlh88            0/1     Pending     0          19h

model-serving-64dd4cdcd8-cnfv7   0/1     Pending     0          19h

model-serving-64dd4cdcd8-hhftw   0/1     Pending     0          19h


**k8s Describe Deployment Serving**

PS C:\Users\nitis\Desktop\mlops-pytorch-pipeline> kubectl describe deployment model-serving -n ml-training

Name:                   model-serving

Namespace:              ml-training

CreationTimestamp:      Wed, 26 Aug 2026 18:48:45 +0530

Labels:                 app=model-serving

Annotations:            deployment.kubernetes.io/revision: 1

Selector:               app=model-serving

Replicas:               2 desired | 2 updated | 2 total | 0 available | 2 unavailable

StrategyType:           RollingUpdate

MinReadySeconds:        0

RollingUpdateStrategy:  0 max unavailable, 1 max surge

Pod Template:

  Labels:  app=model-serving
  
  Containers:
   serving-runtime:
    Image:      mlops-serve:v1
    Port:       8080/TCP
    Host Port:  0/TCP
    Limits:
      cpu:     1
      memory:  2Gi
    Requests:
      cpu:        500m
      memory:     1Gi
    Liveness:     http-get http://:8080/health delay=0s timeout=1s period=10s #success=1 #failure=3    
    Readiness:    http-get http://:8080/health delay=15s timeout=1s period=5s #success=1 #failure=3    
    Environment:  <none>
    Mounts:
      /app/checkpoints from checkpoint-volume (ro,path="checkpoints")
  
  Volumes:
   checkpoint-volume:
    Type:          PersistentVolumeClaim (a reference to a PersistentVolumeClaim in the same namespace)
    ClaimName:     ml-storage-pvc
    ReadOnly:      false
  
  Node-Selectors:  <none>
  
  Tolerations:     <none>

Conditions:
  
  Type           Status  Reason
  
  ----           ------  ------
  
  Available      False   MinimumReplicasUnavailable
  
  Progressing    False   ProgressDeadlineExceeded

OldReplicaSets:  <none>

NewReplicaSet:   model-serving-64dd4cdcd8 (2/2 replicas created)

Events:          <none>


**k8s Port-Forwarding**

PS C:\Users\nitis\Desktop\mlops-pytorch-pipeline> kubectl port-forward svc/model-serving 8080:80 -n ml-training

error: unable to forward port because pod is not running. Current status=Pending


# Challenges Faced

The Most Challenging Part of MLOps Pipeline SetupBuilding a CIFAR-10 classifier (model.py, dataset.py, train.py) is straightforward in a local script environment. 

However, turning that code into a production-ready pipeline exposed the true complexities of MLOps across Git, Docker, and Kubernetes.

1. Managing Container Parity and CUDA BloatPyTorch dependencies are heavy. Splitting dependencies into train.txt and serve.txt helped keep the inference image lean, but aligning the CUDA runtime versions inside Dockerfile.train and Dockerfile.serve was difficult. A small mismatch between the host driver, the container CUDA toolkit, and the PyTorch wheel version caused hardware fallback errors or silent crashes. Tuning multi-stage Docker builds to solve this without creating massive image sizes took careful adjustment.

2. Kubernetes Resource Limits and OOM CrashesMoving workloads into Kubernetes (training-job.yaml and serving-deployment.yaml) introduced strict hardware boundaries. During training, aggressive batch sizes and PyTorch data loaders frequently triggered Out-Of-Memory (OOM) errors when container limits were set too tight. Balancing CPU, memory, and GPU requests alongside environment configurations (configmap.yaml) required extensive testing. Furthermore, setting up the Horizontal Pod Autoscaler (hpa.yaml) for inference (serve.py) demanded precise traffic and load thresholds to prevent latency spikes without wasting cluster resources.
