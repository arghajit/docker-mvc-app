#!/bin/bash
echo "Executing Newman tests"
# exec 'newman run flask.postman_collection.json -d testdata.json -e test.postman_environment.json -r html'
npm install newman
npm install newman -g
newman run flask.postman_collection.json -d testdata.json -e test.postman_environment.json -r html
ls -l
# exec 'ls -l'
# exec 'cd newman'
cd newman
pip install --upgrade pip
python -m http.server 3001 --bind 127.0.0.1
