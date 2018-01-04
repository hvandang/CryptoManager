
from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


api.add_resource(HelloWorld, '/')

parser = reqparse.RequestParser()
parser.add_argument('username', type=str)
parser.add_argument('password', type=str)


class Authenticate(Resource):
	def post(self):
		args = parser.parse_args()
		un = str(args['username'])
		pw = str(args['password'])
		return check_auth(un,pw)
    		
def check_auth(username, password):
    return username == 'user' and password == '123'
    
api.add_resource(Authenticate, '/auth')

if __name__ == '__main__':
    app.run(debug=True)
    
    """
    
from flask import Flask
from flask import request
 
app = Flask(__name__)
 
@app.route('/get', methods = ['GET'])
def getHandler():
    return 'GET handler'
 
@app.route('/post', methods = ['POST'])
def postHandler():
    return 'POST handler'
 
@app.route('/getpost', methods = ['POST', 'GET'])
def postGetHandler():
    if request.method == 'POST':
        return 'request via POST'
    else:
        return 'request via GET'
 
app.run(host='0.0.0.0', port= 8090)"""