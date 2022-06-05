from flask import Flask , request, render_template, session, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS 
from flask_session import Session
import json

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
db  = SQLAlchemy(app)
CORS(app)

app.config['SESSION_PERMANENT'] = False
app.config['SESSION_TYPE'] = "filesystem"
Session(app)

global_products_list = []
class Product(db.Model):
	id          = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
	photo_url   = db.Column(db.String, unique=True)
	name        = db.Column(db.String(200), unique=True)
	price       = db.Column(db.Integer, unique=False)
	description = db.Column(db.String(200), unique=True)

	def _repr_(self):
		return {
			"success": "Product added successfully"
		}

class API(Resource):

	def get(self):
		products_list = []
		global_products_list
		products = Product.query.all()
		for product in products:
			_product = {
				'id': product.id,
				'name': product.name,
				'photo_url': product.photo_url,
				'price': product.price,
				'description': product.description
			}
			products_list.append(_product)
			global_products_list.append(_product)
		return  products_list

	def post(self):
		request_data = request.get_json()
		new_product = Product(
			photo_url=request_data['photo_url'],
			name=request_data['name'], 
			price=request_data['price'], 
			description=request_data['description']
		)
		db.session.add(new_product)
		return db.session.commit()


	

api.add_resource(API, '/api')

#Front-End Routes
@app.route("/")
def index():
	products_list = []
	products = Product.query.all()
	for product in products:
		_product = {
			'id': product.id,
			'photo_url': product.photo_url,
			'name': product.name,
			'price': product.price,
			'description': product.description
		}

		products_list.append(_product)
	return render_template("index.html", products=products_list)

@app.route("/edit")
def edit():
	id = request.args.get("id")
	product  = Product.query.get(id)
	print(str(product.description))
	return render_template("edit.html", product=product)

@app.route('/remove')
def delete():
	id = request.args.get('id')
	product =  Product.query.get(id)

@app.route('/admin/login', methods=["GET", "POST"])
def admin_login():
	if request.method == 'POST':
		session["admin"] == request.form.get("name")
		return redirect("/admin")

	return render_template("login.html")

@app.route('/admin')
def admin():
	if not session.get("admin"):
		return redirect("/admin/login")

	return render_template("admin.html")
if __name__=='__main__':
	app.run(debug=True)

