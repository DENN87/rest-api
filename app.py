from flask import Flask, jsonify, request
from werkzeug.exceptions import abort

app = Flask(__name__)

stores = [
    {
        "name": "Mac Devices",
        "items": [
            {
                "name": "Macbook Air",
                "price": "699.99"
            },
            {
                "name": "Macbook Pro",
                "price": "1299.99"
            },
            {
                "name": "Mac Studio",
                "price": "1999.99"
            },
        ]
    },
    {
        "name": "Software",
        "items": [
            {
                "name": "Final Cut",
                "price": "299.99"
            },
            {
                "name": "Compressor",
                "price": "49.99"
            },
            {
                "name": "Motion",
                "price": "49.99"
            },
            {
                "name": "Logic Pro",
                "price": "199.99"
            },
        ]
    },
    {
        "name": "iPad",
        "items": [
            {
                "name": "iPad Air",
                "price": "599.99"
            },
            {
                "name": "iPad Pro",
                "price": "799.99"
            },
            {
                "name": "iPad",
                "price": "329.99"
            },
        ]
    },
]


# GET /store
@app.route('/store')
def get_stores():
    return jsonify({'stores': stores})


# GET /store/<string:name>
@app.route('/store/<string:name>')
def get_store_by_name(name):
    for s in stores:
        if s['name'] == name:
            return s
    else:
        abort(404, f'Store {name} not found.')


# POST /store data: {name:, items:}
@app.route('/store', methods=['POST'])
def create_store():
    data = request.get_json()
    new_store = {
        'name': data['name'],
        'items': data['items']
    }
    stores.append(new_store)
    return jsonify(new_store)


# GET /store/<string:name>/items
@app.route('/store/<string:name>/items')
def get_store_items(name):
    data = get_store_by_name(name)
    return jsonify(data['items'])


# POST /store/<string:name>/item {name:, price:}
@app.route('/store/<string:name>/item', methods=['POST'])
def create_store_item(name):
    data = request.get_json()
    store = get_store_by_name(name)
    store['items'].append(data)
    return jsonify(store)
    

if __name__ == __name__:
    app.run(port=3000)
