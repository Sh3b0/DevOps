# Infrastructure as Code

## Table of Contents

1. [Overview](#1-Overview)

   1.1. [Terraform](#11-Terraform)

   1.2. [Vagrant](#12-Vagrant)

2. [Goal](#2-Goal)

3. [Steps](#3-Steps)

   3.1. [Prerequisites](#31-Prerequisites)

   3.2. [Docker Provider](#32-Docker-Provider)

   3.3. [Vagrant Provider](#33-Vagrant-Provider)

   3.4. [GitHub Provider](#34-GitHub-Provider)

   3.5. [AWS Provider](#35-AWS-Provider)

4. [Best Practices](#4-Best-Practices)

## 1. Overview

### 1.1. Terraform

The core terraform workflow consists of 3 stages:

- **Write:** represent infrastructure as [HCL declarative code](https://www.terraform.io/language). The syntax is built around two constructs: **arguments** and **blocks** (i.e., line-separated arguments and blocks).
  - HCL supports common programming concepts such as **variables**, **types** (string, numeric), **functions** (built-in), and **expressions**.
  - An existing and supported infrastructure can be **import**ed into terraform to start managing it from code.
- **Plan:** terraform creates an execution plan describing actions (e.g., create, modify, or destroy resources) that will be taken based on existing infrastructure **state** (stored in the **backend**) and current **workspace** configuration.
- **Apply:** interact with the service/platform-specific API through their **providers** (published on [**registry**](https://registry.terraform.io/)) to execute the plan.
  - **Named values** are used for working with API keys or other configurations to allow re-usability and avoid hard-coding.
  - **Modules** are used to group resources that are used together as a reusable package.  

### 1.2. Vagrant

- `Vagrantfile` is used to describe an **environment** (of **VMs/containers** with networking) as **declarative ruby code** that can be used to set **up** the environment, test scripts or configuration management tools (e.g., Chef, Ansible, or Puppet), then **halt** and **destroy** the environment or recreate it on the cloud.
- A **box** (pulled from the **[cloud](https://vagrantcloud.com/boxes/search)**) is typically used as the starting point for running ready-to-use environments or as a template for creating custom ones.
- **Providers** allow writing `Vagrantfile`s for different types of virtualization systems. Support for **Virtualbox**, **Hyper-V**, and **Docker** works out-of-the-box. Other providers should be installed as **plugins**.

## 2. Goal

Getting familiar with terraform by:

- Experimenting with the [Docker provider](https://registry.terraform.io/providers/kreuzwerker/docker/latest/docs) following [this tutorial](https://learn.hashicorp.com/collections/terraform/docker-get-started).
- Using [Vagrant provider](https://registry.terraform.io/providers/bmatcuk/vagrant/latest/docs) to provision a test infrastructure (3 VMs serving the application with an NGINX load-balancer in front of them).
- Using [GitHub provider](https://registry.terraform.io/providers/integrations/github/latest/docs) to manage an existing GitHub repository from code.
- Using [AWS provider](https://registry.terraform.io/providers/hashicorp/aws/latest/docs) to provision an EC2 instance.

## 3. Steps

### 3.1. Prerequisites

- Install [VirtualBox](https://www.virtualbox.org/wiki/Downloads), [Terraform CLI](https://www.terraform.io/downloads), and [Vagrant CLI](https://www.vagrantup.com/downloads)
- Create `terraform` directory with 4 subdirectories (modules) for `vagrant`, `github`, `docker`, and `aws`.

### 3.2. Docker Provider

- Write `main.tf` that uses docker provider [kreuzwerker/docker](https://github.com/kreuzwerker/terraform-provider-docker) to create resources of types `docker_image` and a `docker_container`.

- Parametrize `container_name` in `variables.tf` and define outputs in `outputs.tf`

- Use terraform to run `sh3b0/app_python`

  ```bash
  docker pull sh3b0/app_python
  docker tag sh3b0/app_python app_python
  terraform init       # Prepare workspace and download providers
  terraform validate   # Check configuration for validity
  terraform fmt        # Format source file
  terraform plan       # Show execution plan
  ```

- Apply plan with the custom value: `terraform apply -var 'container_name=app_python'`

  ![tf-apply](./images/tf-apply.png)

- Show state

  ![tf-state](./images/tf-state.png)

### 3.3. Vagrant Provider

- Write `Vagrantfile` that uses [hashicorp/bionic64](https://app.vagrantup.com/hashicorp/boxes/bionic64) box to create 3 VMs for app and a fourth one for the load balancer.
  
  ```bash
  vagrant up       # Start and provision environment
  vagrant halt     # Stop the VMs
  vagrant destroy  # Destroy the environment.
  ```

- Write `main.tf` that uses vagrant provider and `outputs.tf` that shows forwarded ports.
  
  ```bash
  terraform init      # Prepare workspace and download providers
  terraform validate  # Check configuration for validity
  terraform fmt       # Format source file
  terraform plan      # Show execution plan
  terraform apply     # Execute the plan
  ```
  
- On success, 4 VMs should be visible in VirtualBox GUI.
  
  - **Default credentials for testing:** vagrant:vagrant
  - Private keys for connection are stored in `.vagrant` directory.
  
  ![vagrant](images/vagrant.png)

- Run `terraform destroy` to destroy the created infrastructure.

### 3.4. GitHub Provider

- Write `main.tf` that uses `integrations/github` provider.
- Configure `github` provider with `token` declared in `variables.tf` and assign the value from command line or `.tfvars` file.
- Declare resources of types `github_repository`, `github_branch`, `github_branch_default`, and `github_branch_protection_v3`  with the desired configurations.
- Import the remote repo to use the existing configuration
  
  ```bash
  terraform import github_repository.<resource_name> <repo_name>
  ```

- Use the same terraform commands as above to manage the repository configuration from terraform.

- **Test repository created manually**

  ![gh-1](images/gh-1.png)

- **Terraform configurations applied**

  ![gh-2](images/gh-2.png)

- **Description and default branch changed**

  ![gh-3](images/gh-3.png)

- **Branch protection rules applied**

  ![gh-4](images/gh-4.png)

### 3.5. AWS Provider

- Write `main.tf` that uses  `hashicorp/aws` provider to provision an EC2 instance by creating an `aws_instance` resource.

- Specify the OS to run using its corresponding AMI ([Ubuntu](https://cloud-images.ubuntu.com/locator/ec2/) examples).

- Run

  ```bash
  export AWS_ACCESS_KEY_ID=<iam_access_key>
  export AWS_SECRET_ACCESS_KEY=<iam_secret_key>
  terraform init
  terraform validate
  terraform fmt
  terraform plan
  terraform apply
  ```

- Verify instance was created

  ![tf-aws](./images/tf-aws.png)

- Destroy instance with `terraform destroy`

  ![tf-destroy](./images/tf-destroy.png)

## 4. Best Practices

- Use an IDE plugin to help with syntax highlighting and autocompletion ([official VSCode plugin](https://marketplace.visualstudio.com/items?itemName=HashiCorp.terraform)).
- Use built-in formatter and validator, check plan before applying changes.
- Sensitive information (state and secret variables) shouldn’t be pushed to the VCS; they can be stored locally and ignored by the VCS, or stored remotely and encrypted at rest ([.gitignore for terraform](https://github.com/github/gitignore/blob/main/Terraform.gitignore)).
- Recommended directory structure and file naming for a minimal module:

  ```bash
  .
  ├── README.md     # module description
  ├── main.tf       # entry point (resource definition)
  ├── variables.tf  # input variables and locals
  ├── outputs.tf    # output variables
  ```

- When using providers (for vagrant or terraform), be sure to pin their versions to ensure reproducibility.
