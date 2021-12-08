FROM node:12.18-alpine
ENV NODE_ENV=production
ENV PORT=5000
WORKDIR /app
COPY . .
RUN npm install --silent
EXPOSE 5000
CMD ["npm", "start"]
