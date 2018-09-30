#!flask/bin/python
from flask import Flask,jsonify,make_response,Response,request,Response,json
from model import Users
from json import JSONEncoder
# import serialize
import datetime

notfound = 404
invalid = 403
ok = 200
created = 201
accepted = 202

response_success = {'message':'success'}
response_failure = {'message':'failure'}
# response_crea


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

#GENERIC ENDPOINT
@app.route('/')
def index():
    return jsonify({'message':'hello world'})

users=[]
"""
--------------------------------------------
REST ENDPOINTS ARE STARTING FROM HERE
--------------------------------------------
"""
#===========POST===========
@app.route('/api/user/new', methods=['POST'])
def createUser():
    user = Users()
    Users.startengine()
    try:
        user.create(**request.json)
    except Exception as e:
        # print("===========app.py/createUser===========")
        print(e)
        user.rollback()
        return response_failure, invalid
    return response_success, created

#===========GET===========
@app.route('/api/user/', methods=['GET'])
def getAllUsers():
    user = Users()
    # for user1 in user.retrive():
        # users.append(user1)
    # print("===========app.py/getAllusers===========")
    # print(users)
    # response = {}
    # response['users']=users
    # return users, ok;
    userlist = []
    for user1 in user.retrive():
        userlist.append(user1.__str__())
    return userlist, ok

#===========GET===========
@app.route('/api/user/<string:name>', methods = ['GET'])
def getUser(name):
    user = Users()
    # print("===========app.py/getUser===========")
    # print(user.retrive(name))
    # if name in user.retrive():

    # userlist=[]
    for user1 in user.retrive():
        # userlist.append(user1)
        if name == user1.__repr__():
            # print(user1)
            return user1.__str__(), ok
    # response1 = {}
    # response1['users']=users
    # return users, ok;
    # print(user.retrive())
    #
    #
    message={}
    message['message']='failure'
    return response_failure, invalid

#===========UDPATE===========
@app.route('/api/user/<string:key>', methods = ['PUT'])
def updateUser(key):
    # print("==========={0}".format(key))
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
    return make_response(jsonify({'error': 'Not found'}), 404)


"""
MAIN - ENTRY POINT
"""
if __name__ == '__main__':
    app.run(port=8000, threaded=True, host=('0.0.0.0'), debug=True)
