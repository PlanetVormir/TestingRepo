FROM node:16-alpine

WORKDIR /app/frontend

ENV PATH /app/node_modules/.bin:$PATH

COPY . .
RUN npm install
RUN npm run build