# CI/CD

> It’s about setting up an automated process for incorporating new code into existing infrastructure (CI) and automatically deploying/delivering it to the end-users (CD)

## GitHub Actions

> A **workflow** (described as a YAML file) defines actions that are triggered by some events (e.g., pushing to the remote repository), after which some **jobs** (each described by a sequence of **steps**) are **run on** dedicated GitHub servers (windows/ubuntu/macOS) in parallel.

- Add workflows in [`/.github/workflows/`](/.github/workflows/) and make sure they run only when there are relevant updates. 
- Keep actions minimal and don’t install unnecessary dependencies.
- Use GitHub secrets when working with credentials or tokens.
- With DockerHub, it’s more secure to use a generated-token with only the necessary permissions instead of using the password.

## Jenkins

> …

