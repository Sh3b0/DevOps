# DevOps

DevOps training repository. Two web applications are used to practice:

- Web application development with Python and JavaScript.
- Application Containerization with Docker.
- CI/CD with Jenkins and GitHub Actions.
- Infrastructure as Code with Terraform.
- Configuration Management with Ansible.
- Container Orchestration with K8s on AWS.
- Monitoring with Prometheus.
- Visualization and analytics with Grafana.

## Applications

- [app_python](./app_python): sample flask app that shows current time.

- [app_nodejs](./app_nodejs): sample nodejs app for an online multiplayer pong game.

## Best Practices

General best practices learnt are listed here, language-specific tips are listed the respective app directory.

- For the flask webapp check [app_python/PYTHON.md](./app_python/PYTHON.md) and [app_python/DOCKER.md](./app_python/DOCKER.md)

- For the nodejs webapp check [app_nodejs/NODEJS.md](./app_nodejs/NODEJS.md) and [app_nodejs/DOCKER.md](./app_nodejs/DOCKER.md)

### **During Development**

- **Use a Version Control System like `git`**: this helps to keep track of change history and roll back changes when needed. It also allows collaboration on remote repositories and many other benefits.
  - Be sure to ignore private or environment-specific files, you can use a `.gitignore` template for the IDE and tech stack you use.
- **Use the debugging/development server** provided by the framework, which provides extensive debugging messages and tools as well as other features such as reloading server on code changes.
- **Follow recommended design patterns** for the coding language you use (when appropriate).
- **Work in an isolated environment:**never install project dependencies globally in your OS filesystem unless you need them for all your projects.
- **Follow a well-known style guide and use linters and IDE extensions to enforce it** for the programming/scripting/documentation languages you use. The most important thing is to stay consistent and use the same styles everywhere.
- **Use a well-known directory hierarchy and file/folder naming** for the frameworks used.
- **Use automated tests** when it makes sense to use them.
- **You may use a containerized environment** to avoid problems of type *“It works on my machine”* and to avoid installing large software like databases on your machine.

### For Production

- **Use a containerized environment**
- **Best practices when writing `Dockerfile`**:
  - **Use a Dockerfile linter** (e.g., `hadolint`) as it helps build best practice Docker images.
  - **Use a small base image** that does the job (e.g., alpine-based images) as it will make deployment faster while not taking much space.
  - Copy only the necessary files to the image to make it smaller and faster, use `.dockerignore` to ignore unnecessary files and directories.
  - Use `EXPOSE` documentation to make port-forwarding easier for other programmers reading your `Dockerfile`.
- **Use a production webserver** like `nginx`
  - For serving static pages, handling SSL, load balancing, DoS protection, enforcing access rules, and many other required functionalities.
  - Cloud solutions help you focus on application development rather than going through all of these issues from the start, however, it’s still beneficial to learn about webserver configuration.
- Depending on application size and needs, you **may use a container orchestrator.**
  - For small-sized deployments, it’s more than enough to use `docker-compose` to deploy everything with one command.
  - For larger deployments, k8s is used.
- For version control of app images and convenient deployment to the cloud, you may **push image to a container registry** like DockerHub or the cloud-dedicated container registry.
  - To easily understand which version of the code is currently in the registry, you can tag the image with it’s corresponding the commit id from git.
  - You can see the latest id with `git log -1 --pretty=format:%h`
