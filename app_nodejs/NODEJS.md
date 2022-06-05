# Best Practices

> Used while developing a nodejs webapp.

## During Development

- Use **development server** (`webpack-dev-server` for frontend and `nodemon` for backend) to get useful logs in terminal and reload server on code changes.
- **Use devDependencies** for dependencies that are not required in production (they won’t get installed when NODE_ENV is production).
- **Use TypeScript** to write more reliable code.
- **Use ESLint with** recommended typescript rules.
- **Follow common directory structure and directory/file naming**
  - **For NodeJS apps:**
    - Use `src` directory for source code
    - `public` or `static` directory for static files with subdirectories for `css`, `js`, `images`, and any other needed static files 
    - `dist` directory for frontend bundles (and maybe for `js` files compiled with `tsc`).