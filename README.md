# docker-mvc-app
### A sample project showcasing a multi containers application with REST backend running model-view and Responsive UI in front end running with api and ui level tests. All of these from a single docker-compose file.

### 1.1. About
Once started, multiple containers holding different docker images 
- serves a `user` model with RESTful APIs
- an `orm` associated with model stores data in db
- an REST endpoint serves static files for UI
- UI designed with purest form of CSS, JS and HTML which get served in UI and uses the aforementioned REST backend
- An test collection to test API endpoints run after db and backend boots up
- A simplest selenium framework testing UI with `BDD` style tests cases.

All of the contianers runs independently. All codes are added into docker contianers as `volume`. One can restart a single container independently to keepSo one can update the code directly and see it in effect. Dependeing upon tech stack, you may need to restart a single contianer to reflect the changes.

### 1.2. Run
Lorem ipsum dolor sit amet consectetur adipiscing elit, semper nam justo sapien cum duis penatibus, egestas cubilia senectus parturient pellentesque praesent. Quisque leo fusce aptent maecenas diam pulvinar litora, natoque montes vulputate sem cursus iaculis, tristique habitant ut ullamcorper taciti pharetra. Accumsan feugiat praesent class bibendum curae curabitur morbi lacinia convallis montes auctor velit, volutpat integer et gravida odio eget turpis tempor per fames vestibulum.
#### 1.2.1. Take a pull of this repository
```git
Arghajit@mac$ git clone https://github.com/arghajit/docker-mvc-app.git
```
#### 1.2.2. Build all of the containers
```docker
Arghajit@mac$ docker-compose build
```
#### 1.2.3. Run the containers. 
```sh
Arghajit@mac$ docker-compose up -d
```
In few seconds you start seeing all of the containers being up and running.
```
Arghajit@mac$ docker ps
xxxx
```
### 1.3. Structure
Structure is build with a `bottom-up` approch where modules are built one by one. All modules holds there required packages/modules inside it. 
#### 1.3.1. Database (`postgres`)
A simple `XXX` base image is being used with out any build step (`Dockerfile` is there; not in use). Currently the application uses the default `postgres@postgres` table schema and create model table there. This is entry point of our application which kicks off first.
```sh
port in use: 5432
````
#### 1.3.2. RESTful API (`flask`)
`flask` is minimal web framework build with `python`. It offers minimal setup to kick off a backend service. An mdoel `user` being served which is binding with a orm `SQLAlchemy`. Currently it points to `postgres` db hosted in the container. 
**Following are the endpoints of user service**
```sh
GET /api/user                       # produce JSON, SUCCESS CODE 200
GET /api/user/<string:name>         # produce JSON, SUCCESS CODE 200
POST /api/user/new                  # consume JSON, produce JSON, SUCCESS CODE 201
PUT /api/user/<string:name>         # consume JSON, produce JSON, SUCCESS CODE 202
DELETE /api/user/<string:name>      # produce JSON, SUCCESS CODE 202 
```
An **user** can be explained like this:
```json
{
   "name": "Justin S Weber",
   "birthday": "5/30/1990",
   "address": "3977 Court Street",
   "email": "justin@google.com"
 }
```
To keep things minimal currently no such `composite key` for this `user` model. Thus `name` was made unique and hence `<string:name>` uses *slug* value of the names.
```yml
    GET /api/user/Juntin_S_Weber
```
```yml
port in use: 8000
````
#### 1.3.3. Static (`pure css-html-js`)
Lorem ipsum dolor sit amet consectetur adipiscing elit, semper nam justo sapien cum duis penatibus, egestas cubilia senectus parturient pellentesque praesent. Quisque leo fusce aptent maecenas diam pulvinar litora, natoque montes vulputate sem cursus iaculis, tristique habitant ut ullamcorper taciti pharetra. Accumsan feugiat praesent class bibendum curae curabitur morbi lacinia convallis montes auctor velit, volutpat integer et gravida odio eget turpis tempor per fames vestibulum.
```yml
port in use: 8000
````
#### 1.3.4. API Testing (`newman-postman collection`)
Lorem ipsum dolor sit amet consectetur adipiscing elit, semper nam justo sapien cum duis penatibus, egestas cubilia senectus parturient pellentesque praesent. Quisque leo fusce aptent maecenas diam pulvinar litora, natoque montes vulputate sem cursus iaculis, tristique habitant ut ullamcorper taciti pharetra. Accumsan feugiat praesent class bibendum curae curabitur morbi lacinia convallis montes auctor velit, volutpat integer et gravida odio eget turpis tempor per fames vestibulum.
```
port in use: xxx
````
#### 1.3.5. UI Testing (`python-selenium-behave`)
Lorem ipsum dolor sit amet consectetur adipiscing elit, semper nam justo sapien cum duis penatibus, egestas cubilia senectus parturient pellentesque praesent. Quisque leo fusce aptent maecenas diam pulvinar litora, natoque montes vulputate sem cursus iaculis, tristique habitant ut ullamcorper taciti pharetra. Accumsan feugiat praesent class bibendum curae curabitur morbi lacinia convallis montes auctor velit, volutpat integer et gravida odio eget turpis tempor per fames vestibulum.
### 1.4. Flow
Lorem ipsum dolor sit amet consectetur adipiscing elit, semper nam justo sapien cum duis penatibus, egestas cubilia senectus parturient pellentesque praesent. Quisque leo fusce aptent maecenas diam pulvinar litora, natoque montes vulputate sem cursus iaculis, tristique habitant ut ullamcorper taciti pharetra. Accumsan feugiat praesent class bibendum curae curabitur morbi lacinia convallis montes auctor velit, volutpat integer et gravida odio eget turpis tempor per fames vestibulum.
### 1.5. Complete `Docker-compose.yml`
```yml
version: '3.6'

services:
  db1:
    container_name: db1
    restart: always
    image: "postgres:10.1-alpine"
    volumes:
      - ./db/postgres/log:/var/log/postgresql
      - ./db/postgres/backup:/backup
      - ./db/postgres/conf:/etc/postgresql/
    ports:
      - 5432:5432
    expose:
      - "5432"

  flask:
    container_name: flask
    restart: always
    build: './flask'
    command: 'python ./app.py'
    volumes:
      - ./flask:/code
    expose:
      - "8000"
    ports:
      - 8000:8000
    environment:
      - DB_HOST=db1
      - DB_NAME=postgres
      - DB_PORT=5432
      - DB_USER=postgres
      - DB_PASS=postgres
    depends_on:
      - db1

  api-tests:
    container_name: api-tests
    build: './api-tests'
    command: ./run.sh
    volumes:
      - ./api-tests:/usr/src/app
    ports:
      - 3001:3001
    depends_on:
      - db1
      - flask

  selenium:
    container_name: selenium
    build: './ui-tests'
    # command: 'behave'
    command: 'behave -f allure_behave.formatter:AllureFormatter -o . ./features'
    command: 'python -m SimpleHTTPServer 3002 --bind 127.0.0.1'
    volumes:
      - ./ui-tests:/code
    ports:
      - 4444:4444
      - 3002:3002
    depends_on:
      - flask
      - db1

```
### 1.6 Full Folder Structure
```sh
  .
  ├── README.md
  ├── api-tests
  │   ├── Dockerfile
  │   ├── flask.postman_collection.json
  │   ├── index.html
  │   ├── run.sh
  │   ├── test.postman_environment.json
  │   ├── testdata.json
  │   └── testdata2.json
  ├── db
  │   ├── Dockerfile
  │   ├── docker-entrypoint-initdb.d
  │   │   ├── init-postgres-db.sh
  │   │   └── run.sh
  │   ├── init.sql
  │   ├── postgres
  │   │   └── data
  │   │       └── postgresql.auto.conf
  │   └── run.sh
  ├── docker-compose.yml
  ├── flask
  │   ├── Dockerfile
  │   ├── app.py
  │   ├── favicon.ico
  │   ├── model.py
  │   ├── pip-selfcheck.json
  │   ├── public
  │   │   ├── css
  │   │   │   └── style.css
  │   │   ├── index.html
  │   │   └── js
  │   │       └── index.js
  │   └── requirements.txt
  ├── structure
  └── ui-tests
      ├── Dockerfile
      ├── environment.py
      ├── features
      │   └── user_service.feature
      ├── requirements.txt
      └── steps
          └── steps.py

  12 directories, 30 files

```
### 1.7 Work in progress
* UI Tests
  * Selenium test cases are written in feature files. But assiciated step definations are not written.
  * Fix docker env issues with selenium docker image. Chrome fails to kick off. Thinking to change the base image from `XXX` to `alpine linux` and use `xvfb` to run tests.
* Front End
  * Static files are being served by `flask` itself. CSS, HTML constructed. `index.js` being updated to tune with REST APIs.

