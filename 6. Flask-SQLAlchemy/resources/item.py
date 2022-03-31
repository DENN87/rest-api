from flask_jwt_extended import jwt_required
from flask_restful import Resource, reqparse
from models.item import ItemModel

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type = float,
                        required = True,
                        help = "This field cannot be blank!"
                        )
    parser.add_argument('store_id',
                        type = int,
                        required = True,
                        help = "Provide store id for this item."
                        )

    @jwt_required
    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {'message': 'Item not found.'}, 404
    
    def post(self, name):
        if ItemModel.find_by_name(name):
            return {'message': f"An item with name '{name}' already exists."}, 400
        data = Item.parser.parse_args()
        item = ItemModel(name, data['price'], data['store_id'])  # (**data) unpacking data
        try:
            item.save_to_db()
        except:
            return {'message': 'An error occurred inserting the item.'}, 500  # internal server error
        return item.json(), 201
    
    def put(self, name):
        data = Item.parser.parse_args()
        item = ItemModel.find_by_name(name)
        if item is None:
            item = ItemModel(name, data['price'], data['store_id'])  # (**data) unpacking data
        else:
            item.price = data['price']
            item.store_id = data['store_id']
        item.save_to_db()
        return item.json()
    
    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
            return {'message': 'Item successfully deleted.'}, 200
        return {'message': 'Nothing to delete, item not found.'}, 404


class ItemList(Resource):
    def get(self):
        # or list Comprehension [x.json() for x in ItemModel.query.all()]
        return {'items': list(map(lambda x: x.json(), ItemModel.find_all()))}
