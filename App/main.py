import sys
sys.path.append(".")
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from json import dumps
from database import *

# Conectamos con la Base de Datos
conn = createConnection()
# creamos la tabla Usuarios
createTable(conn, sql_create_user_table)

#creamos la aplicacion
app = Flask(__name__)
# creamos la Api
api = Api(app)

class User(Resource):
    def get(self, mail, psw):
        response = {
            'status': 405,
            'msg': 'Ha ocurrido un error inesperado',
            'res': {}
        }
        return jsonify(response)

api.add_resource(User, '/user/<mail>/<psw>') # Route_1

if __name__ == '__main__':
     app.run(port='5002')
