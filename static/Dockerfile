FROM mhart/alpine-node:10
WORKDIR /usr/src/app
COPY package*.json ./
RUN ls -l
RUN cat package.json
RUN npm install
# RUN npm-install-all
RUN apk add python3 py-pi
COPY . .
RUN ls -l
RUN pwd
EXPOSE 3000
