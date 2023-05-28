from main.models._db import save, delete
from flask import jsonify
from main.models.tag import Tag
from main.models.item import Item
from main.schemas.item import ItemSchema


class ItemService:
    def __init__(self):
        self.item_schema = ItemSchema()
        self.items_schema = ItemSchema(many=True)

    def get_all(self):  # ok
        items = Item.query.join(Tag).all()
        results = []
        for item in items:
            results.append({
                "id": item.id,
                "name": item.name,
                "price": item.price,
                "unit": item.unit,
                "tagId": item.tag_id
            })
        print(results)
        return jsonify(results)

    def get(self, item_id):
        item = Item.query.get(item_id)
        return self.item_schema.jsonify(item)

    def create(self, data):  # ok
        item = Item.query.filter_by(name=data['name']).first()
        if not item:
            new_item = Item(
                name=data['name'],
                price=data['price'],
                unit=data['unit'],
                tag_id=data['tag']
            )
            save(new_item)
            print(jsonify(new_item))
            return self.item_schema.jsonify(new_item)

    def update(self, item_id, data):
        # item = Item.query.join(Tag).get(item_id)
        item = Item.query.join(Tag).filter(Item.id == item_id).first()
        print(item)
        if item:
            item.name = data['name']
            item.price = data['price']
            item.unit = data['unit']
            item.tag_id = data['tag']
        save(item)
        return self.item_schema.jsonify(item)

    def delete(self, item_id):
        item = Item.query.get(item_id)
        if item:
            delete(item)
            return item_id
