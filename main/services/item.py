from main.models._db import save, delete
from flask import jsonify
from main.models.item import Item
from main.schemas.item import ItemSchema


class ItemService:
    def __init__(self):
        self.item_schema = ItemSchema()
        self.items_schema = ItemSchema(many=True)

    def get_all(self):
        items = Item.query.all()
        return jsonify(self.items_schema.dump(items))

    def get(self, item_id):
        item = Item.query.get(item_id)
        return self.item_schema.jsonify(item)

    def create(self, data):
        item = Item.query.filter_by(name=data['name']).first()
        if not item:
            new_item = Item(
                name=data['name'],
                price=data['price'],
                unit=data['unit'],
                tag_id=data['tag_id']
            )
            save(new_item)
            return self.item_schema.jsonify(new_item)

    def update(self, item_id, data):
        item = Item.query.get(item_id)
        if item:
            item.name = data['name'],
            item.price = data['price'],
            item.unit = data['unit'],
            item.tag_id = data['tag_id']
            save(item)
            return self.item_schema.jsonify(item)

    def delete(self, item_id):
        item = Item.query.get(item_id)
        if item:
            delete(item)
            return item_id
