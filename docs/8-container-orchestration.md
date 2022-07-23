# Container Orchestration

## Table of Contents

1. [Overview](#1-Overview)

   1.1. [Kubernetes](#1.1.-Kubernetes)

   1.2. [Helm](#1.2.-Helm)

2. [Goal](#2-Goal)

3. [Steps](#3-Steps)

   3.1. [Deployment](#3.1.-Deployment)

   3.2. [Helm Chart](#3.2.-Helm-Chart)

   3.3. [Secret](#3.3.-Secret)

   3.4. [LimitRange](#3.4.-LimitRange)

   3.5. [ConfigMap](#3.5.-ConfigMap)

   3.6. [StatefulSet](#3.6.-StatefulSet)

4. [Best Practices](#4.-Best-Practices)

## 1. Overview

### 1.1. Kubernetes

- A system for automating software deployment, scaling, and management.

- A typical use case involves the deployment of different **[objects](https://kubernetes.io/docs/concepts/overview/working-with-objects/kubernetes-objects/)** (using YAML files describing their desired **spec**ification) on **nodes** (virtual or physical machines) inside the **cluster** that is **controlled** and **managed** by the **master node** which stores information about the cluster state in **etcd** database and exposes an **API** that can be interacted with from the command-line (using `kubectl`).

- Common object **kind**s (check `kubectl api-resources`)

  | Object                                                       | Overview                                                     |
  | ------------------------------------------------------------ | ------------------------------------------------------------ |
  | [**Pod**](https://kubernetes.io/docs/concepts/workloads/pods/) | Represents a logical host that typically runs one containerized application, but may run additional **[sidecar](https://kubernetes.io/docs/concepts/workloads/pods/#workload-resources-for-managing-pods)** containers. |
  | [**ReplicaSet**](https://kubernetes.io/docs/concepts/workloads/controllers/replicaset/) | Ensures that a specified number of pod replicas are running at one time. |
  | [**Deployment**](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/) | Represents an application running in the cluster, provides declarative updates for Pods and ReplicaSets. |
  | [**Service**](https://kubernetes.io/docs/concepts/services-networking/service/) | Represents a network service that makes a set of pods accessible using a single DNS name and can load-balance between them. |
  | [**ConfigMap**](https://kubernetes.io/docs/concepts/configuration/configmap/) | An API object used to store non-confidential  data as key-value pairs that are accessible by pods (e.g., as environment variables). |
  | [**Secret**](https://kubernetes.io/docs/concepts/configuration/secret/) | Similar to ConfigMaps, but are specifically intended to hold confidential data (e.g., passwords and tokens). |
  | [**Ingress**](https://kubernetes.io/docs/concepts/services-networking/ingress/) | An API object that manages external access to the services in a cluster, typically HTTP. |
  | **[StatefulSet](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/)** | A deployment for stateful applications; provides guarantees about the ordering and uniqueness of deployed Pods. |
  | **[DaemonSet](https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/)** | Every node in a DaemonSet runs a copy of a certain pod (e.g., for cluster storage, logs collecting, or node monitoring). For example, there can be a DaemonSet for Windows hosts and another one for Linux hosts. |
  | **[PersistentVolume](https://kubernetes.io/docs/concepts/storage/persistent-volumes/)** | Abstraction of a persistent storage that can use a local or remote (cloud) storage as a backend. For the data to actually persist, the storage should be available for all nodes and shouldn’t depend on pod lifecycle or cluster status. |
  | **[LimitRange](https://kubernetes.io/docs/concepts/policy/limit-range/)** | Enforces minimum and maximum resource usage limits per pod or container in a namespace. |

### 1.2. Helm

- **A package manager for k8s:** allows packaging and reusing an existing k8s architecture/manifest as a bundle of YAML files called an **Application Chart** and upload it to a public/private registry (e.g., [ArtifactHub](https://artifacthub.io/)).

  - **Library charts** on the other hand are not meant for deployment, they are typically included as dependencies to other charts to allow reusing snippets of code across charts and avoid duplication.

- **A templating engine:** the packaged YAML files can use the [Helm templating language](https://helm.sh/docs/chart_template_guide/) that can generate different k8s manifests from the same source file through [values files](https://helm.sh/docs/chart_template_guide/values_files/). 

- **Basic Directory structure of a helm chart:**

  ```bash
  mychart/
  	templates/   # YAML bundle (where .Values object is accissble)
  	charts/      # Chart dependencies
  	Chart.yaml   # Chart metadata: name, version, dependencies, etc.
  	values.yaml  # Default values for the template files
  ```

## 2. Goal

- Deploy an application in minikube using the command line and using a manifest.
- Create a helm chart from the previously-created manifest.
- Create a secret (e.g., for DB username and password) and inject it as an environment variable to the deployment pods. 
- Set LimitRanges for CPU and memory usage.
- Create a ConfigMap with some JSON data and inject it as a volume.
- Create a StatefulSet.

## 3. Steps

### 3.1. Deployment

- Install [kubectl](https://kubernetes.io/docs/tasks/tools/) and [minikube](https://minikube.sigs.k8s.io/docs/start/)

- Run `minikube start` to start a local k8s cluster and configure `kubectl` to interact with it.

- Create a deployment for the Python (or NodeJS) application.

  ```bash
  kubectl create deployment python-app --image=sh3b0/app_python
  ```

- Create an external service to make the app accessible from outside.

  ```
  kubectl expose deployment python-app --type=LoadBalancer --port=8080
  ```

- Show created objects

  ```bash
  $ kubectl get all # or kubectl get pod,svc to show only pods and services
  NAME                             READY   STATUS    RESTARTS   AGE
  pod/python-app-cc8f9dc84-rvkmb   1/1     Running   0          9m28s
  
  NAME                 TYPE           CLUSTER-IP     EXTERNAL-IP   PORT(S)          AGE
  service/kubernetes   ClusterIP      10.96.0.1      <none>        443/TCP          13d
  service/python-app   LoadBalancer   10.108.44.57   <pending>     8080:31302/TCP   6m29s
  
  NAME                         READY   UP-TO-DATE   AVAILABLE   AGE
  deployment.apps/python-app   1/1     1            1           9m28s
  
  NAME                                   DESIRED   CURRENT   READY   AGE
  replicaset.apps/python-app-cc8f9dc84   1         1         1       9m28s
  ```

- When deploying on cloud, an external IP for the service will be available. For testing with minikube, run the following command to get a URL for accessing the service. 

  ```bash
  minikube service python-app --url
  ```

- Remove created objects

  ```bash
  kubectl delete service/python-app
  kubectl delete deployment.apps/python-app
  ```

- Create `deployment.yml` and `service.yml` inside `k8s/minikube` directory to do the same from configuration files instead of stdin.

- Apply configuration and check results

  ```bash
  $ kubectl apply -f deployment.yaml -f service.yaml
  deployment.apps/app-deployment created
  service/app created
  
  $ kubectl get all
  NAME                                  READY   STATUS    RESTARTS   AGE
  pod/app-deployment-69cfdc7ff9-lkhpk   1/1     Running   0          9s
  pod/app-deployment-69cfdc7ff9-v287x   1/1     Running   0          9s
  pod/app-deployment-69cfdc7ff9-vshs6   1/1     Running   0          9s
  
  NAME                 TYPE           CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
  service/app          LoadBalancer   10.106.183.183   <pending>     8080:32442/TCP   12s
  service/kubernetes   ClusterIP      10.96.0.1        <none>        443/TCP          13d
  
  NAME                             READY   UP-TO-DATE   AVAILABLE   AGE
  deployment.apps/app-deployment   3/3     3            3           9s
  
  NAME                                        DESIRED   CURRENT   READY   AGE
  replicaset.apps/app-deployment-69cfdc7ff9   3         3         3       9s
  ```

### 3.2. Helm Chart

- Install [helm](https://helm.sh/docs/intro/install/) and navigate to `k8s/helm`

- Create chart files and directories manually or use `helm create app-python` to add some boilerplate.

- Copy the previously-created YAMLs to `templates` directory, parametrize them and put default values in `values.yaml` 

- **Example use case:** deploy nodejs app for the chart

  ```bash
  cd k8s/helm
  helm install --set image=sh3b0/app_nodejs:latest my-chart ./app-deployment
  
  helm list            # to see installed charts
  minikube dashboard   # opens a web UI for debugging
  ```

### 3.3. Secret

- To store secrets (e.g., database user and password) in k8s, create a secret object:

  ```bash
  # Create secret from files (should be ignored from the VCS).
  $ kubectl create secret generic db-user-pass \
    --from-file=username=./username.txt \
    --from-file=password=./password.txt
  secret/db-user-pass created
  
  # Verify secret exists
  $ kubectl get secrets
  NAME                  TYPE                                  DATA   AGE
  db-user-pass          Opaque                                2      3s
  default-token-dmksw   kubernetes.io/service-account-token   3      40h
  
  # Show secret (base64 encoded)
  $ kubectl get secret db-user-pass -o jsonpath='{.data.username}' | base64 -d
  admin
  ```

- Secrets can be mounted as volumes or exposed as environment variables to pods. 

- The same is done:

  - Using a manifest file at `k8s/minikube/secret.yaml`
  - Using a template file at `k8s/helm/secret.yaml`
    - The secret values are exposed as environment variables to the container using `container.env` list.
    - Since that configuration section can be used frequently, it is defined as a named template `DB.CREDS` in `k8s/helm/app_deployment/templates/_helpers.tpl` and included in `deployment.yaml` with the proper indentation length.
    - Verify the variables are accessible by pods.  
    
        ![k8s-secret](./images/k8s-secret.png)

### 3.4. LimitRange

- Create `k8s/minikube/limitrange.yaml` with request (min) and limit (max) cpu and memory usage for all containers.

- Apply configuration: `kubectl apply -f limitrange.yaml`

- Check configuration is being used:

  ```bash
  $ kubectl get pod/app-deployment-7d7c4b5bb6-vn72b -oyaml
  ...
  resources:
    limits:
      cpu: 500m
      memory: 128Mi
    requests:
      cpu: 500m
      memory: 128Mi
  ...
  ```

### 3.5. ConfigMap

- Create dummy configs for testing

  ```bash
  $ cd k8s/helm/app-deployment/
  $ mkdir config
  $ echo '{ "key": "value" }' > config/config.json
  ```

- Create `templates/configmap.yaml` ConfigMap resource with the data from the JSON file.

- Edit `templates/deployment.yaml` to mount `config/` directory as a volume in `/app` in the app container.

- Install the chart and verify config is available in the container.  

    ![k8s-cm](./images/k8s-cm.png)

### 3.6. StatefulSet





## 4. Best Practices

https://kubernetes.io/docs/setup/best-practices/

https://helm.sh/docs/chart_best_practices/
