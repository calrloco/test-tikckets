FROM node:20-alpine

WORKDIR /app

COPY package.json package-lock.json* ./

RUN npm ci || true

COPY . .

EXPOSE 3000

RUN npm run build

CMD ["npm", "run", "preview", "--", "--host", "0.0.0.0", "--port", "3000"]
