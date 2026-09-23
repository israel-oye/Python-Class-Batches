from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

products = [
    {"id": 1, "name": "Laptop", "price": 1500.00, "color": 4281089616},
    {"id": 2, "name": "Smartphone", "price": 950.99, "color": 4281637083},
    {"id": 3, "name": "Tablet", "price": 599.99, "color": 4280193279},
    {"id": 4, "name": "Headphones", "price": 299.99, "color": 4293348412},
    {"id": 5, "name": "Smart Watch", "price": 399.99, "color": 4294928820},
]


@app.route("/")
def home():
    
    # print(render_template("index.html"))
    word = "<h3>Header </h3>"
    # return redirect(url_for('products_route'))
    return render_template("index.html", text=word)


@app.route("/example/<word>")
def example(word): # A view function
    return render_template('index.html', wrd=word)


# @app.route("/products")
# def products_route():
#     all_products = [
#         f"""
#         <a href={url_for('product_detail', id_=p['id'])}>
#         <li>
#             {p['name']}
#         </li>
#         </a>
#         """
#         for p in products
#     ]

#     all_products_html = ""
#     for li in all_products:
#         all_products_html += li

#     print(all_products_html)

#     return f"""
#     <h3>Products</h3>
#     <ol>
#     {all_products_html}
#     </ol>
#     """
@app.route("/products")
def products_route():
    return render_template("products.html", products=products)

@app.route('/products/<int:id_>')
def product_detail(id_: int):
    try:
        product = products[id_ - 1]
        color_hex = hex(product['color'])
        color_hex = color_hex[2:]
    except IndexError as e:
        return "<p>Error 404</p>"

    print(url_for('product_detail', id_=20))
    return f"""
        <h2>Products Page</h2>
        <h3 style="color: #{color_hex}">{product['name']}</h3>
        <br>
        <p>₦{product['price']}</p>
        <a href="{url_for('products_route')}"> All products </a>
    """

@app.route('/products', methods=['POST'])
def create_product():
    import random

    new_item = request.form['item']

    p = {
        'id': len(products) + 1,
        'name': new_item,
        'price': round((random.random() * 1000) + 100, 2),
        'color': 0
    }
    products.append(p)

    return redirect(url_for('products_route'))

if __name__ == "__main__":
    app.run(port=5000, debug=True)
