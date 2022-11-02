FROM node:16-alpine

WORKDIR /app/frontend

ENV PATH /app/node_modules/.bin:$PATH

COPY package.json .

RUN npm install --silent

COPY build build