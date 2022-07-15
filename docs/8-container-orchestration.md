# Container Orchestration

## Table of Contents

1. [Overview](#1-Overview)

   1.1. [Kubernetes](#1.1.-Kubernetes)

   1.2. [Helm](#1.2.-Helm)

2. [Goal](#2-Goal)

3. [Steps](#3-Steps)

   3.1. Deploy an Application on Minikube

   3.2. Create a Helm Chart

4. [Best Practices](#4.-Best-Practices)



## 1. Overview

### 1.1. Kubernetes

- A system for automating software deployment, scaling, and management.

- A typical use-case involves the deployment of different **[objects](https://kubernetes.io/docs/concepts/overview/working-with-objects/kubernetes-objects/)** (YAML files describing the desired **spec**ification of API resources) on **nodes** (virtual or physical machine) inside the **cluster** that is **controlled** and **managed** by the **master node** which stores information about the cluster state in **etcd** database and exposes an **API** that can be interacted with from the command-line (`kubectl`).

- Common object **kind**s (check `kubectl api-resources`)

  | Object                                                       | Description                                                  |
  | ------------------------------------------------------------ | ------------------------------------------------------------ |
  | [**Pod**](https://kubernetes.io/docs/concepts/workloads/pods/) | Represents a logical host that typically runs one containerized application, but may run an additional **[sidecar](https://kubernetes.io/docs/concepts/workloads/pods/#workload-resources-for-managing-pods)** container. |
  | [**ReplicaSet**](https://kubernetes.io/docs/concepts/workloads/controllers/replicaset/) | Ensures that a specified number of pod replicas are running at one time. |
  | [**Deployment**](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/) | Represents an application running in the cluster, provides declarative updates for Pods and ReplicaSets. |
  | [**Service**](https://kubernetes.io/docs/concepts/services-networking/service/) | Represents a network service that makes a set of pods accessible using a single DNS name and can load-balance between them. |
  | [**ConfigMap**](https://kubernetes.io/docs/concepts/configuration/configmap/) | An API object used to store non-confidential data in key-value pairs that are accessible by pods (e.g., as environment variables). |
  | [**Secret**](https://kubernetes.io/docs/concepts/configuration/secret/) | Similar to ConfigMaps, but are specifically intended to hold confidential data (e.g., passwords and tokens). |
  | [**Ingress**](https://kubernetes.io/docs/concepts/services-networking/ingress/) | An API object that manages external access to the services in a cluster, typically HTTP. |
  | **[StatefulSet](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/)** | A deployment for stateful applications; provides guarantees about the ordering and uniqueness of deployed Pods. |
  | **[DaemonSet](https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/)** | Every node in a DaemonSet runs a copy of a certain pod (e.g., cluster storage, logs collector, node monitoring). For example, there can be a DaemonSet for Windows hosts and another one for Linux hosts. |
  | **[PersistentVolume](https://kubernetes.io/docs/concepts/storage/persistent-volumes/)** | Abstraction of a persistent storage that can use a local or remote (cloud) storage as a backend. For the data to actually persist, the storage should be available for all nodes and shouldn’t depend on pod lifecycle or cluster status. |

### 1.2. Helm

- **A package manager for k8s:** allows packaging and reusing an existing k8s setup/manifest as a bundle of YAML files called an **Application Chart** and upload it to a public/private registry (e.g., [ArtifactHub](https://artifacthub.io/)).

  - **Library charts** on the other hand are not meant for deployment, they are typically included as dependencies to other charts to allow reusing snippets of code across charts and avoid duplication.

- **A templating engine:** the YAML files use default **values** that can be overridden by chart users.

- **Basic Directory structure of a helm chart:**

  ```bash
  mychart/
  	templates/   # YAML bundle (where .Values object is accissble)
  	charts/      # Chart dependencies
  	Chart.yaml   # Chart metadata: name, version, dependencies, etc.
  	values.yaml  # Default values for the template files
  ```

  



## 2. Goal

- Deploy an application in (local) minikube cluster from command line and using a manifest.
- Create a helm chart from the previously-created manifest.

## 3. Steps

### 3.1. Deploy an Application on Minikube

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

- When deploying on cloud, an external IP for the service will be available, for testing with minikube, run the following command to get a URL for accessing the service. 

  ```bash
  minikube service python-app --url
  ```

- Remove created objects

  ```bash
  kubectl delete service/python-app
  kubectl delete deployment.apps/python-app
  ```

- Create `deployment.yml` and `service.yml` inside `k8s` directory to do the same from configuration files instead of stdin.

- Apply configuration and check results

  ```bash
  $ kubectl apply -f deployment.yaml
  deployment.apps/app-deployment created
  
  $ kubectl apply -f service.yaml   
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



### 3.2. Create Helm Chart

- Install [helm](https://helm.sh/docs/intro/install/).

- Create chart files and directories manually or use `helm create app-python` to add some boilerplate.

- Copy the previously-created YAMLs to `templates` directory, parametrize them and put default values in `values.yaml` 

- **Example usecase:** deploy nodejs app for the chart

  ```bash
  cd k8s/helm
  helm install -f my_values.yaml my-chart ./app-deployment
  
  helm list            # to see installed charts
  minikube dashboard   # opens a web UI for debugging
  ```

  

## 4. Best Practices

https://kubernetes.io/docs/setup/best-practices/

https://helm.sh/docs/chart_best_practices/
