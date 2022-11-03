FROM node:16-alpine
ENV NODE_ENV=production

WORKDIR /app/frontend

COPY . .
RUN npm install --production
RUN npm run build --prod