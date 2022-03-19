from flask import Flask, request
from flask_restful import Resource, Api
from werkzeug.exceptions import abort

app = Flask(__name__)
api = Api(app)

items = []

class Item(Resource):
    def get(self, name):
        item = next(filter(lambda x: x['name'] == name, items), None)
        return item, 200 if item else 404
    
    def post(self, name):
        if next(filter(lambda x: x['name'] == name, items), None):
            return {f'message': "An item with name {name} already exists."}, 400
        else:
            item = request.get_json()
            items.append(item)
            return item, 201
    
        
class ItemList(Resource):
    def get(self):
        return items
        
    
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')


app.run(port=5000, debug=True)
