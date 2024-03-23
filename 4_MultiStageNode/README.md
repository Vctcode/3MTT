# DOCKERFILE

    # Stage 1: Build stage
    FROM node:alpine3.16 AS build
    WORKDIR /app
    COPY package*.json ./
    RUN npm install
    COPY . .

    # Stage 2: Production stage
    FROM node:alpine3.16 AS production
    WORKDIR /app
    COPY --from=build /app .
    EXPOSE 3000
    CMD ["node", "app.js"]
