FROM node:16-alpine
WORKDIR /app
COPY . .
ENV NODE_ENV="production"
RUN npm ci && addgroup -S app && adduser -S app -G app && chown -R app:app . 
USER app
CMD ["npm", "run", "start"]
