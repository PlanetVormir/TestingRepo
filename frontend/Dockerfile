FROM node:16-alpine

WORKDIR /app/frontend

ENV PATH /app/node_modules/.bin:$PATH

COPY package.json .

RUN npm install

COPY . .
RUN npm run build

COPY build /app/frontend/