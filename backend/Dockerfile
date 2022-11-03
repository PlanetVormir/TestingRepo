FROM node:16-alpine
ENV NODE_ENV=production

WORKDIR /app/frontend

COPY . .
RUN npm install --production
RUN npm run build --prod

FROM python:3.10

RUN apt-get update && apt-get install -y --no-install-recommends postgresql-client \
    && rm -rf /var/lib/apt/lists/* \

WORKDIR /app
COPY --from=node /app/frontend .

WORKDIR /app/backend
COPY requirements.txt /app/backend
RUN pip install -r requirements.txt

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]