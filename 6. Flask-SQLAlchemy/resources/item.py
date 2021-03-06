from flask_jwt_extended import get_jwt, get_jwt_identity, jwt_required
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

    @jwt_required()
    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {'message': 'Item not found.'}, 404

    @jwt_required(fresh = True)
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
    
    @jwt_required()
    def delete(self, name):
        claims = get_jwt()
        if not claims['is_admin']:
            return {'message': 'Admin privilege required.'}, 401
        
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
            return {'message': 'Item successfully deleted.'}, 200
        return {'message': 'Nothing to delete, item not found.'}, 404


class ItemList(Resource):
    @jwt_required(optional=True)
    def get(self):
        user_id = get_jwt_identity()
        # or list Comprehension [x.json() for x in ItemModel.query.all()]
        items = list(map(lambda item: item.json(), ItemModel.find_all()))
        if user_id:
            return {'items': items}, 200
        
        return {
            'items': [item['name'] for item in items],
            'message': 'More data available if you log in.'
            }, 200
