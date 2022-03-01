FROM node
WORKDIR app
COPY ./backend/express_backend/package.json /app/
RUN npm install 
ADD ./backend/express_backend/ /app/
EXPOSE 4000
CMD ["node","app.js"]