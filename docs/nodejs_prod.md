# For Production

- Used the lightweight alpine-based node images.
- Used `.dockerignore` to ignore unnecessary files and folders (e.g., `node_modules`, `Dockerfile`)
- Set environment variable `NODE_ENV` to `production` to configure ExpressJS with production settings.
- Used `npm ci` instead of `npm i` ([see why](https://docs.npmjs.com/cli/v8/commands/npm-ci)).

