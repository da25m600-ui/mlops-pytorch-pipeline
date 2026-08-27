# mlops-pytorch-pipeline

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
