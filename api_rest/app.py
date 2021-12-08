from flask import  Flask, jsonify, request


from products import products


app= Flask(__name__)


@app.route('/ping') #ruta
def ping():
    return jsonify(products)

#ruta

@app.route('/product')
def product():
    return jsonify({"products":products, "mensage": "Product's list"})
    

@app.route("/product/<string:product_name>")
def getproduct(product_name):
    productsFound=[producto for producto in products if producto['name'] == product_name ]         
    
    if (len(productsFound)>0):
        return jsonify({"product":productsFound[0]})
    return jsonify({"menssage": "No se encontro"})


@app.route('/product',methods=['POST'])
def addProduct():
    return jsonify(request.json)

@app.route('/products/<string:product_name>', methods=['PUT'])
def editProduct(product_name):
    productFound= [product for product in products if product['name']== product_name]
    if(len(productFound)>0):
        productFound[0]['name']= request.json['name']
        productFound[0]['price']= request.json['price']
        productFound[0]['quantity']= request.json['quantity']
        return jsonify({"message": "Product Updated", "product":productFound[0]})
    return jsonify({"message":"Product Not found"})



if __name__=='__main__':
    app.run(debug=True, port=5000)