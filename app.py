from flask import Flask , request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api, reqparse
# from flask_cors import CORS #install the package
import json

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///priducts.db'
db  = SQLAlchemy(app)
# CORS(app)

class Product(db.Model):
	id          = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
	name        = db.Column(db.String(200), unique=True)
	price       = db.Column(db.Integer, unique=False)
	description = db.Column(db.String(200), unique=True)

	def _repr_(self):
		return {
			"success": "Product added successfully"
		}

class API(Resource):

	def get(self):
		products = Product.query.all()
		products_list = []
		for product in products:
			_product = {
				'id': product.id,
				'name': product.name,
				'price': product.price,
				'description': product.description
			}
			products_list.append(_product)
		return  products_list

	def post(self):
		request_data = request.get_json()
		new_product = Product(
			name=request_data['name'], 
			price=request_data['price'], 
			description=request_data['description']
		)
		db.session.add(new_product)
		return db.session.commit()


	

api.add_resource(API, '/api')


if __name__=='__main__':
	app.run(debug=True)
