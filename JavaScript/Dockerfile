FROM node:18.15.0-bullseye-slim

WORKDIR /app

COPY package.json package-lock.json ./

RUN npm ci

COPY . .

EXPOSE 8080

CMD [ "node", "index.js" ]