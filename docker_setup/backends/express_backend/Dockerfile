FROM node:17-alpine3.15
WORKDIR /app
COPY ./backend/express_backend/package.json /app/
RUN npm install 
ADD ./backend/express_backend/ /app/
EXPOSE 4000
USER node
CMD ["node","app.js"]