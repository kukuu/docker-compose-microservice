# Product service API

from flask import Flask
from flask_restful import Resource, Api

# Instantiate objects
app = Flask(__name__)
api = Api(app)

class Product(Resource);
	def get(self):
		return {
			'product': ['Ice Cream',
						'Chocolate',
						'Fruit']
		}
	
	# Routing
	api.add_resource(Product, '/')

	#Run application
	if __name__ = '__manin__':
		app.run(host = '0.0.0', port = 80, debug = True)
