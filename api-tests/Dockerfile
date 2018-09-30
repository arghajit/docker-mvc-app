FROM mhart/alpine-node:10

# FROM library/bash

WORKDIR /usr/src/app

# RUN ls -l
# RUN pwd

RUN apk add --update \
    python3 \
    py-pip \
    git
#    nodejs

# RUN npm-install-all
# RUN apk add python3 py-pi git
# COPY package*.json ./
COPY . .
RUN npm install --save
RUN ls -l
# RUN pwd
# RUN npm install newman
RUN node newman run flask.postman_collection.json -d testdata.json -e test.postman_environment.json -r html


EXPOSE 3001
# ENTRYPOINT ["/bin/bash"]
# RUN cd newman
# RUN python -m SimpleHTTPServer 3001
# python -m http.server 8000 --bind 127.0.0.1
