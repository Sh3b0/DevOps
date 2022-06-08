# During Development

- Use **development server** (e.g., `webpack-dev-server` for frontend and `nodemon` for backend) to get useful logs in terminal and reload server on code changes.
- **Use devDependencies** for dependencies that are not required in production (they won’t get installed when NODE_ENV is set to production).
- **Use TypeScript** to write more reliable and type-safe code.
- **Use ESLint with** recommended typescript rules.
- **Follow a common directory structure and directory/file naming**
  - **Example for NodeJS apps:**
    - Use `src` directory for source code
    - `public` or `static` directory for static files with subdirectories for `css`, `js`, `images`, and any other needed static files.
    - `dist` directory for frontend bundles (and maybe for `js` files compiled with `tsc`).