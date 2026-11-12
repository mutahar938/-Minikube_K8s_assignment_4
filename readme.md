Minikube Installation & Cluster Setup 

winget install Kubernetes.minikube
winget install Kubernetes.kubectl

----------------------------------------------------------------------------------------

Verify the installation: 

PS C:\Users\Muhammad Mutahar\Desktop\DevOps\minikube-assignment-04> minikube version
minikube version: v1.39.0
commit: 7a9f6a841470a207de8cf4bafcccee0969d8ba10

PS C:\Users\Muhammad Mutahar\Desktop\DevOps\minikube-assignment-04> kubectl version --client
Client Version: v1.36.1
Kustomize Version: v5.8.1

----------------------------------------------------------------------------------------

Start the Minikube cluster using the Docker driver: 

PS C:\Users\Muhammad Mutahar\Desktop\DevOps\minikube-assignment-04> minikube start --driver=docker
😄  minikube v1.39.0 on Microsoft Windows 11 Home 25H2
✨  Using the docker driver based on user configuration
📌  Using Docker Desktop driver with root privileges
👍  Starting "minikube" primary control-plane node in "minikube" cluster
🚜  Pulling base image v0.0.51 ...
🔥  Creating docker container (CPUs=2, Memory=8000MB) ...
📦  Preparing Kubernetes v1.37.0 on containerd 2.3.4 ...
🔗  Configuring CNI (Container Networking Interface) ...
🔎  Verifying Kubernetes components...
    ▪ Using image gcr.io/k8s-minikube/storage-provisioner:v5
🌟  Enabled addons: storage-provisioner, default-storageclass
🏄  Done! kubectl is now configured to use "minikube" cluster and "default" namespace by default

PS C:\Users\Muhammad Mutahar\Desktop\DevOps\minikube-assignment-04> minikube status
minikube
type: Control Plane
host: Running
kubelet: Running
apiserver: Running
kubeconfig: Configured


----------------------------------------------------------------------------------------


PS C:\Users\Muhammad Mutahar\Desktop\DevOps\minikube-assignment-04> docker build -t custom-pod-app:v1 .
[+] Building 9.4s (10/10) FINISHED                                                                       docker:default
 => [internal] load build definition from Dockerfile                                                               0.1s
 => => transferring dockerfile: 205B                                                                               0.0s
 => [internal] load metadata for docker.io/library/python:3.11-slim                                                1.3s
 => [internal] load .dockerignore                                                                                  0.0s
 => => transferring context: 2B                                                                                    0.0s
 => [1/5] FROM docker.io/library/python:3.11-slim@sha256:07d4824036af339fa1b6ef769cc99d9c10a141769538b52b3b597c84  6.1s
 => => resolve docker.io/library/python:3.11-slim@sha256:07d4824036af339fa1b6ef769cc99d9c10a141769538b52b3b597c84  0.0s
 => => sha256:b701198cb708b68d9413ca67d6311bd97c9389a2c5fe4da0511fc652642366cd 1.75kB / 1.75kB                     0.0s
 => => sha256:896edfbcbf0c29ad15681617a8886cb9871b7f24c5fde4606114c8ee6bfe4c70 5.49kB / 5.49kB                     0.0s
 => => sha256:37fb86c2a767b88d500c6872195f88078f64765fe0d2f9cc375cc2efbd4c0a41 29.86MB / 29.86MB                   3.8s
 => => sha256:53daecf7856e9b7235583f1ec326387aae7d29af3d5cd2efc20246259ab817cc 1.29MB / 1.29MB                     0.9s
 => => sha256:7efbce397249e9202b070b8e638baff71160948c640b9a44f2226419a71f410d 14.46MB / 14.46MB                   3.0s
 => => sha256:07d4824036af339fa1b6ef769cc99d9c10a141769538b52b3b597c84f7a7b535 10.37kB / 10.37kB                   0.0s
 => => sha256:bbe7053e6def9842d628414346e26f25e499463adb6ca48c0c8932e036e44000 249B / 249B                         1.2s
 => => extracting sha256:37fb86c2a767b88d500c6872195f88078f64765fe0d2f9cc375cc2efbd4c0a41                          1.0s
 => => extracting sha256:53daecf7856e9b7235583f1ec326387aae7d29af3d5cd2efc20246259ab817cc 

-----------------------------------------------------------------------------------------

Create a Custom Docker Image 
app.py 
requirements.txt 
Dockerfile 

----------------------------------------------------------------------------------------


Build the Docker image directly inside Minikube's Docker daemon (so Minikube can find the local image without needing to pull from Docker Hub): 

PS C:\Users\Muhammad Mutahar\Desktop\DevOps\minikube-assignment-04> & minikube -p minikube docker-env --shell powershell | Invoke-Expression

PS C:\Users\Muhammad Mutahar\Desktop\DevOps\minikube-assignment-04> docker build -t custom-pod-app:v1 .
[+] Building 9.4s (10/10) FINISHED                                                                       docker:default
 => [internal] load build definition from Dockerfile                                                               0.1s
 => => transferring dockerfile: 205B                                                                               0.0s
 => [internal] load metadata for docker.io/library/python:3.11-slim                                                1.3s
 => [internal] load .dockerignore                                                                                  0.0s
 => => transferring context: 2B                                                                                    0.0s
 => [1/5] FROM docker.io/library/python:3.11-slim@sha256:07d4824036af339fa1b6ef769cc99d9c10a141769538b52b3b597c84  6.1s
 => => resolve docker.io/library/python:3.11-slim@sha256:07d4824036af339fa1b6ef769cc99d9c10a141769538b52b3b597c84  0.0s
 => => sha256:b701198cb708b68d9413ca67d6311bd97c9389a2c5fe4da0511fc652642366cd 1.75kB / 1.75kB                     0.0s
 => => sha256:896edfbcbf0c29ad15681617a8886cb9871b7f24c5fde4606114c8ee6bfe4c70 5.49kB / 5.49kB              

----------------------------------------------------------------------------------------

Create Deployment & Service YAML Manifests 
deployment-clusterip.yaml 
deployment-nodeport.yaml 
deployment-loadbalancer.yaml 

----------------------------------------------------------------------------------------


Apply Manifests & Verify Deployments and Services 

Apply all three manifests: 

PS C:\Users\Muhammad Mutahar\Desktop\DevOps\minikube-assignment-04> kubectl apply -f k8s-manifests/
deployment.apps/app-clusterip-deploy created
service/service-clusterip created
deployment.apps/app-lb-deploy created
service/service-loadbalancer created
deployment.apps/app-nodeport-deploy created
service/service-nodeport created


Verify pods and deployments: 

PS C:\Users\Muhammad Mutahar\Desktop\DevOps\minikube-assignment-04> kubectl get deployments
NAME                   READY   UP-TO-DATE   AVAILABLE   AGE
app-clusterip-deploy   0/2     2            0           70s
app-lb-deploy          0/2     2            0           70s
app-nodeport-deploy    0/2     2            0           70s

PS C:\Users\Muhammad Mutahar\Desktop\DevOps\minikube-assignment-04> kubectl get pods -o wide
NAME                                    READY   STATUS             RESTARTS      AGE   IP           NODE       NOMINATED NODE   READINESS GATES
app-clusterip-deploy-744f8d8848-2zb27   0/1     CrashLoopBackOff   3 (47s ago)   89s   10.244.0.3   minikube   <none>           <none>
app-clusterip-deploy-744f8d8848-zmtc6   0/1     Completed          4 (50s ago)   89s   10.244.0.6   minikube   <none>           <none>
app-lb-deploy-67dfcf6df7-vgsl8          0/1     Completed          4 (46s ago)   89s   10.244.0.4   minikube   <none>           <none>
app-lb-deploy-67dfcf6df7-ztqbr          0/1     Completed          4 (48s ago)   89s   10.244.0.5   minikube   <none>           <none>
app-nodeport-deploy-757d998d9b-55pn8    0/1     Completed          3 (76s ago)   89s   10.244.0.8   minikube   <none>           <none>
app-nodeport-deploy-757d998d9b-fckxt    0/1     Completed          3 (73s ago)   89s   10.244.0.7   minikube   <none>   


Verify services: 

NAME                   TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
kubernetes             ClusterIP      10.96.0.1       <none>        443/TCP          9m19s
service-clusterip      ClusterIP      10.107.109.28   <none>        80/TCP           2m7s
service-loadbalancer   LoadBalancer   10.106.21.226   <pending>     8080:30322/TCP   2m7s
service-nodeport       NodePort       10.97.207.137   <none>        80:30080/TCP     2m7s





Accessibility Demonstration 

A. ClusterIP Service (Internal Only) 

PS C:\Users\Muhammad Mutahar\Desktop\DevOps\minikube-assignment-04> kubectl run curl-test --image=curlimages/curl -it --rm -- curl http://service-clusterip
All commands and output from this session will be recorded in container logs, including credentials and sensitive information passed through the command prompt.
If you don't see a command prompt, try pressing enter.
warning: couldn't attach to pod/curl-test, falling back to streaming logs: Internal error occurred: unable to upgrade connection: rpc error: code = Unknown desc = container not running (6e68641f4c9a8b4bc0eb6c1373d8835b214d044181921b2eeeefc740996f8ed9)
<h1>Hello from Kubernetes!</h1><p>Served by Pod: <b>app-clusterip-deploy-6898c9785-lgwsg</b></p>pod "curl-test" deleted from default namespace


PS C:\Users\Muhammad Mutahar\Desktop\DevOps\minikube-assignment-04> minikube ssh "curl -s http://localhost:30080"
<h1>Hello from Kubernetes!</h1><p>Served by Pod: <b>app-nodeport-deploy-757d998d9b-f5t5x</b></p>






PS C:\Users\Muhammad Mutahar\Desktop\DevOps\minikube-assignment-04> kubectl get svc service-loadbalancer
NAME                   TYPE           CLUSTER-IP     EXTERNAL-IP   PORT(S)          AGE
service-loadbalancer   LoadBalancer   10.98.196.53   127.0.0.1     8080:31114/TCP   27m


 LoadBalancer Service 


PS C:\Users\Muhammad Mutahar\Desktop\DevOps\minikube-assignment-04> minikube tunnel
✅  Tunnel successfully started

📌  NOTE: Please do not close this terminal as this process must stay alive for the tunnel to be accessible ...

🔗  Starting tunnel for service service-loadbalancer.

PS C:\Users\Muhammad Mutahar\Desktop\DevOps\minikube-assignment-04> kubectl get svc service-loadbalancer
NAME                   TYPE           CLUSTER-IP     EXTERNAL-IP   PORT(S)          AGE
service-loadbalancer   LoadBalancer   10.98.196.53   127.0.0.1     8080:31114/TCP   27m

