FROM node:16-alpine
WORKDIR /app
COPY . .
ENV NODE_ENV="production"
RUN npm ci
RUN addgroup -S app && adduser -S app -G app
USER app
CMD ["npm", "run", "start"]
