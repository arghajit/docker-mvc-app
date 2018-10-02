#!flask/bin/python
from flask import Flask,jsonify,make_response,Response,request,Response,json,send_from_directory
from model import Users
from json import JSONEncoder
import datetime

notfound = 404
invalid = 403
ok = 200
created = 201
accepted = 202

response_success = {'message':'success'}
response_failure = {'message':'failure'}


class MyEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


class ResponseJSON(Response):
    """Extend flask.Response with support for list/dict conversion to JSON."""
    def __init__(self, content=None, *args, **kargs):
        if isinstance(content, (list, dict)):
            kargs['mimetype'] = 'application/json'
            content = to_json(content)

        super(Response, self).__init__(content, *args, **kargs)

    @classmethod
    def force_type(cls, response, environ=None):
        """Override with support for list/dict."""
        if isinstance(response, (list, dict)):
            # print("type: list or dict")
            return cls(response)
        else:
            return super(Response, cls).force_type(response, environ)

def json_default(value):
    if isinstance(value, datetime.date):
        # return dict(year=value.year, month=value.month, day=value.day)
        return "{0}-{1}-{2}".format(value.year ,value.month ,value.day)
    else:
        return value.__dict__

def to_json(content):
    """Converts content to json while respecting config options."""
    indent = None
    separators = (',', ':')

    if (app.config['JSONIFY_PRETTYPRINT_REGULAR']
            and not request.is_xhr):
        indent = 2
        separators = (', ', ': ')

    return (json.dumps(content, indent=indent, separators=separators, cls=MyEncoder, default=json_default), '\n')


class FlaskJSON(Flask):
    """Extension of standard Flask app with custom response class."""
    response_class = ResponseJSON


app = FlaskJSON(__name__)

# app = Flask(__name__)

users=[]
"""
--------------------------------------------
REST ENDPOINTS ARE STARTING FROM HERE
--------------------------------------------
"""
#GENERIC ENDPOINT
@app.route('/')
def index():
    return jsonify({'message':'hello world'})

#===========POST===========
@app.route('/api/user/new', methods=['POST'])
def createUser():
    user = Users()
    Users.startengine()
    try:
        user.create(**request.json)
    except Exception as e:
        print(e)
        user.rollback()
        return response_failure, invalid
    return response_success, created

#===========GET===========
@app.route('/api/user', methods=['GET'])
def getAllUsers():
    user = Users()
    userlist = []
    for user1 in user.retrive():
        userlist.append(user1.__str__())
    return userlist, ok

#===========GET===========
@app.route('/api/user/<string:name>', methods = ['GET'])
def getUser(name):
    user = Users()
    for user1 in user.retrive():
        if name == user1.__repr__():
            return user1.__str__(), ok
    return response_failure, invalid

#===========UDPATE===========
@app.route('/api/user/<string:key>', methods = ['PUT'])
def updateUser(key):
    new = Users()
    data = request.json
    try:
        if new.updateDb(key,**data):
            return response_success, accepted
    except Exception as e:
        print(e)
    return response_failure, notfound

#===========DELETE===========
@app.route('/api/user/<string:pk>', methods = ['DELETE'])
def deleteUser(pk):
    new= Users()
    new.delete(pk)
    return response_success, accepted

#===========404===========
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': '404 Not found'}), 404)

"""
--------------------------------------------
STATIC FILES
--------------------------------------------
"""
@app.route('/static/<path:path>', methods = ['GET'])
def send_js(path):
    print(path, file=sys.stdout)
    return send_from_directory('./public', path)

@app.route('/static/<string:mime>/<string:name>')
def serve_static(mime, name):
    return send_file('./static/{0}/{1}'.format(mime,name))

"""
--------------------------------------------
APP MAIN
--------------------------------------------
"""
if __name__ == '__main__':
    app.run(port=8000, threaded=True, host=('0.0.0.0'), debug=False)
