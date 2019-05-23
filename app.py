from flask import Flask, jsonify, request

app = Flask(__name__)

pizzaDB = [
    {'name': 'tonno'},
    {'name': 'salami'},
    {'name': 'hawaii'},
    {'name': 'kebab'},
    {'name': 'vlees'},
    {'name': 'banaan'},
    {'name': 'appel'},
    {'name': 'kaas'}
]


@app.route("/", methods=['GET'])
def getPizza():
    return jsonify({'pizzaDB': pizzaDB})


@app.route("/getpizza/<string:name>", methods=['GET'])
def getOnePizza(name):
    resultPizza = []
    for pizza in pizzaDB:
        if pizza['name'] == name:
            resultPizza.append(pizza)
    return jsonify({'pizzaDB': resultPizza})


@app.route("/addpizza/", methods=['POST'])
def addOnePizza():
    pizza = {'name': request.json['name']}
    pizzaDB.append(pizza)
    return jsonify({'pizzaDB': pizzaDB})


@app.route("/changepizza/<string:name>", methods=['PUT'])
def putPizza(name):
    resultPizza = []
    for pizza in pizzaDB:
        if pizza['name'] == name:
            resultPizza.append(pizza)
    resultPizza[0]['name'] = request.json['name']
    return jsonify({'pizzaDB': pizzaDB})


@app.route("/deletepizza/<string:name>", methods=['DELETE'])
def delPizza(name):
    resultPizza = []
    for pizza in pizzaDB:
        if pizza['name'] == name:
            resultPizza.append(pizza)
    pizzaDB.remove(resultPizza[0])
    return jsonify({'pizzaDB': pizzaDB})


if __name__ == "__main__":
    app.run(debug=True, port=8080)
