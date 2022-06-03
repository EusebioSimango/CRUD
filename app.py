from flask import Flask , request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api, reqparse
# from flask_cors import CORS #install the package


app = Flask(__name__)
api = Api(app)
# CORS(app)

class Home(Resource):

	def get(self):
		return { 'api': "List of Pruducts" }

api.add_resource(Home, '/')

if __name__=='__main__':
	app.run(debug=True)
