from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps

#db_connect = create_engine('sqlite:///chinook.db')
app = Flask(__name__)
api = Api(app)

class User(Resource):
    def get(self, mail, psw):
        response = {
            'status': 405,
            'msg': 'Ha ocurrido un error inesperado',
            'res': {}
        }
        response["res"] = {
            'mail': mail,
            'pass': psw
        }
        return jsonify(response)

api.add_resource(User, '/user/<mail>/<psw>') # Route_1

if __name__ == '__main__':
     app.run(port='5002')
