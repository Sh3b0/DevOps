# Continuous Deployment

## Table of Contents

1. [Overview](#1-Overview)

   1.1. [Ansible](#1.1.-Ansible)

2. [Goal](#2-Goal)

3. [Steps](#3-Steps)

   3.1. [Prerequisites](#3.1-Prerequisites)

   3.2. [Installing docker on VMs](#3.2.-Installing-Docker-on-VMs)

   3.3. [Deploying Apps](#3.3.-Deploying-Apps)

4. [Best Practices](#4.-Best-Practices)

## 1. Overview

### 1.1. Ansible

- A **playbook** (written in YAML) defines one or more **tasks/plays** (each expressed as list of **modules**) that will be executed on one or more remote machines (selected from **inventory**) through an SSH connection (no agent required).
- A **play** has a **name** (optional), target **hosts** (selected by **patterns**), and a **remote_user** (e.g., root).
- An **inventory** (YAML/INI file) contains [named groups of] IP addresses or hostnames of remote machines, it can also store **variables**.
- **Modules** (**[built-in](https://docs.ansible.com/ansible/2.9/modules/modules_by_category.html)** or [**3rd-party**](https://galaxy.ansible.com/)) are small units of code that Ansible executes against remote machines (default **strategy** is sequential).
- Ansible collects **return codes** from executed tasks, **facts** about remote machines and **magic variables** storing internal state.
- **Role:** the standard way to group related Ansible artifacts (vars, files, tasks, etc.) to share them so they can be loaded and reused.

## 2. Goal

- Getting familiar with Ansible by writing plays to automatically install docker and deploy one of the applications on the Vagrant VMs created during the previous phase. 

## 3. Steps

### 3.1. Prerequisites

- [Install Ansible CLI](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html)

- Apply terraform plan with vagrant provider from previous phase.

  ```bash
  cd terraform/vagrant
  terraform apply
  ```

- Forwarded SSH ports will be printed, note them down to use in Ansible config.

- Create inventory (`ansible/inventory.ini`) with configurations for connecting to VMs.

- Create project configuration (`ansible/ansible.cfg`) and override inventory file location to use the one just created.

  - You may also disable `host_key_checking` as it requires interactive input to add VMs to `~/.ssh/known_hosts`.

- Specify `ansible_ssh_private_key_file=<key_file>` in inventory.

  - Key files can be found in `.vagrant` directory which should be ignored from the VCS.

- Test connection with `ping` module

  ![ansible-1](images/ansible-1.png)

### 3.2. Installing docker on VMs 

- Create a playbook that installs docker (`ansible/install_docker.yml`)

- Execute the playbook: `ansible-playbook ansible/install_docker.yml`

  ![ansible-2](images/ansible-2.png)

- Verify that docker is installed

  ![ansible-3](images/ansible-3.png)

### 3.3. Deploying Apps

- Create and execute `config_nginx.yml` that will install and configure nginx on the loadbalancer VM.

- Install [community.docker collection](https://galaxy.ansible.com/community/docker)

  ```
  ansible-galaxy collection install community.docker
  ```

- Install `python3-pip` and [Docker SDK for Python](https://pypi.org/project/docker/).

- Create and execute `deploy_app.yml` that will pull and run latest app images from DockerHub on app VMs.

- If everything goes fine, application should be accessible at http://localhost:8080

- You may also schedule [Watchtower](https://github.com/containrrr/watchtower) to automatically update app images from DockerHub.

## 4. Best Practices

- A module should be responsible for one small simple task.

- Use `ansible-playbook --check` to check actions before taking them (not all modules support this).

  - Or try changes on staging environment first.

- Give tasks meaningful names, separate them with empty lines for readability, use comments for extra explanation.

- Use `ansible-lint` to lint playbooks.

- Use dynamic inventory when working with cloud hosts to avoid manual IP/hostname configurations.

- Use `state` to specify the desired module state so that modules won’t execute twice unless needed.

- Recommended directory structure:

  ```
  playbooks
  ├── playbook_name.yml
  └── roles
      └── role_name
          ├── defaults
          ├── files
          ├── handlers
          ├── library
          ├── mets
          ├── tasks
          ├── templates
          └── vars
  ```

  
