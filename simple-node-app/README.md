# This is a simple Node Application run by Docker Container

### Dockerfile Config

    FROM node:alpine3.16
    WORKDIR /usr/src/app
    COPY package*.json app.js ./
    RUN npm install
    EXPOSE 3000
    CMD ["node", "app.js"]

### Content of my App.js file

    const express = require('express');
    const app = express();

    app.get('/', (req, res) => res.send("This is a simple node app running on a  Docker Container"))
    app.listen(3000, () => console.log("This server is running on port 3000"))
