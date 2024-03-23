# Stage 1: Build stage
FROM node:alpine3.16 AS build

# Set working directory
WORKDIR /app

# Copy package.json and package-lock.json
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application code
COPY . .

# Stage 2: Production stage
FROM node:alpine3.16 AS production

# Set working directory
WORKDIR /app

# Copy only necessary files from the build stage
COPY --from=build /app .

# Expose port (if your app is running on a specific port)
EXPOSE 3000

# Command to run the application
CMD ["node", "app.js"]

