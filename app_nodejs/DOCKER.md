# Best Practices

## In Production

- Used the lightweight `node-16:alpine` image.
- Used `.dockerignore` to ignore unnecessary files and folders (e.g., `node_modules`, `Dockerfile`, `*.md`).
- Set environment variable `NODE_ENV` to `production` to configure ExpressJS with production settings.
- Used `npm ci` instead of `npm i` ([see why](https://docs.npmjs.com/cli/v8/commands/npm-ci)).

