## PongMe

Online multiplayer pong game using socket.io.

![demo](./demo.gif)



## Used Technology

- **NodeJS**

  - **Dependencies:** TypeScript, ExpressJS, SocketIO, WebPack.
  - **DevDependencies:** typescript-eslint, nodemon, concurrently, webpack-dev-server.

- **HTML, CSS (Bootstrap)**

- **Docker**


## Running the application locally

- With npm (node v16.14.0 is used)
  ```bash
  nvm install
  nvm use
  npm install
  
  # To run webpack dev server
  npm run dev:frontend
  
  # To run nodemon with tsc
  npm run dev:backend
  ```

- With docker
  ```bash
  docker build -t pongme .
  docker run -p8080:8080 pongme
  ```

## Testing

```bash
# Local testing
npm run start # Wait until server starts
npm run test

# Testing in CI
npm run ci
```

## Release

```bash
export DOCKERHUB_ID=<YOUR_DOCKERHUB_ID>
export APP_NAME=app_nodejs

# To build app image
docker build -t $DOCKERHUB_ID/$APP_NAME .

# Testing the built image locally (http://localhost:8080)
docker run -p8080:8080 $DOCKERHUB_ID/$APP_NAME

# Tag image with last commit SHA (or use semantic versioning)
docker tag $DOCKERHUB_ID/$APP_NAME $DOCKERHUB_ID/$APP_NAME:$(git rev-parse --short HEAD)

# Login and push image to dockerhub
docker login -u $DOCKERHUB_ID # Enter password/token when prompted
docker push $DOCKERHUB_ID/$APP_NAME --all-tags
```
