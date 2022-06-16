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

- With npm (v16.14.0 was used)
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
