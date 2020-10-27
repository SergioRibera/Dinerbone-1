from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps

#db_connect = create_engine('sqlite:///chinook.db')
app = Flask(__name__)
api = Api(app)

class User(Resource):
    def get(self):
        return jsonify({ 'name': 'Sergio Ribera' })

#class Employees(Resource):
#    def get(self):
        #conn = db_connect.connect() # connect to database
        #query = conn.execute("select * from employees") # This line performs query and returns json result
        #return {'employees': [i[0] for i in query.cursor.fetchall()]} # Fetches first column that is Employee ID

api.add_resource(User, '/user') # Route_1
#api.add_resource(Tracks, '/tracks') # Route_2
#api.add_resource(Employees_Name, '/employees/<employee_id>') # Route_3


if __name__ == '__main__':
     app.run(port='5002')
