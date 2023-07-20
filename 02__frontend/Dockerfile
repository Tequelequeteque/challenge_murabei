FROM node:alpine

WORKDIR /app
COPY . .
WORKDIR /app/codes
RUN npm install
RUN npm run build

CMD ["npm", "start"]