# This is a simple Node Application run by Docker Container

### Dockerfile Config

    FROM node:alpine3.16
    WORKDIR /usr/src/app
    COPY package*.json app.js ./
    RUN npm install
    EXPOSE 3000
    CMD ["node", "app.js"]
