import flask

from flask import render_template

import databasejson

market = flask.Flask(__name__)

data = databasejson.load_database()

@market.route('/')
@market.route('/home')
def welcome():
    return render_template('market.html')

@market.route('/products')
def products():
    
    return render_template('products.html', products = data)
   

@market.route('/product/<product_id>')
def display_product(product_id):
    for product in data:
        if product_id == product['ProductId']:
            return render_template('product_info.html', product = product)


if __name__ == "__main__":
    market.run(debug=True)