FROM node:12.18-alpine
ENV NODE_ENV=production
ENV PORT=3000
WORKDIR /app
COPY . .
RUN npm install --silent
EXPOSE 3000
CMD ["npm", "start"]
