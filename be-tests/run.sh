#!/bin/sh

echo "executing postman tests"
newman run flask.postman_collection.json -d testdata.json -e test.postman_environment.json -r html --reporter-html-export ./index.html
echo "publishing results"
python -m SimpleHTTPServer 3001 --bind 127.0.0.1
