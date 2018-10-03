# ROM mhart/alpine-node:10

FROM library/node:alpine

WORKDIR /usr/src/app

RUN apk add --update python
RUN npm config set package-lock false
RUN npm install -g newman newman-reporter-html

COPY . .

EXPOSE 3001, 8000
