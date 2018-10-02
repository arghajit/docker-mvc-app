FROM mhart/alpine-node:10
# FROM library/alpine
# FROM library/node:alpine

WORKDIR /usr/src/app

# RUN apk add --no-cache mysql-client
# RUN rm -rf /usr/lib/node_modules
RUN apk add --update sudo nodejs nodejs-npm
# RUN npm install npm@latest -g
RUN npm config set package-lock false
RUN npm install -g nodemon --save-prod
# RUN npm install -g nodemon node-sass pug --unsafe-perm=true --allow-root



COPY . .

EXPOSE 3001
