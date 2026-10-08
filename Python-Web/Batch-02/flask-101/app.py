from flask import Flask, render_template

app = Flask(__name__)

all_products = [
    {"id": 1, "name": "Laptop", "price": 1500.00, "color": 4281089616},
    {"id": 2, "name": "Smartphone", "price": 950.99, "color": 4281637083},
    {"id": 3, "name": "Tablet", "price": 599.99, "color": 4280193279},
    {"id": 4, "name": "Headphones", "price": 299.99, "color": 4293348412},
    {"id": 5, "name": "Smart Watch", "price": 399.99, "color": 4294928820},
]

@app.route('/')
def index():
    return "<h1>Hello world</h1>"

@app.route('/about')
def about():
    return '<h2>About Us</h2>'

@app.route('/products')
def products():
    return render_template("products.html", products=all_products)

if __name__ == '__main__':
    app.run()
