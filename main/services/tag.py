from main.models._db import save, delete
from flask import jsonify
from main.models.tag import Tag
from main.schemas.tag import TagSchema
from main.models.item import Item


class TagService:
    def __init__(self):
        self.tag_schema = TagSchema()
        self.tags_schema = TagSchema(many=True)

    def get_all(self):  # ok
        items = Item.query.join(Tag).all()
        results = {}
        for item in items:
            if item.tag_id not in results:
                results[item.tag_id] = {
                    "id": item.tag_id,
                    "name": item.tag.name,
                    "items": []
                }

            results[item.tag_id]["items"].append({
                "id": item.id,
                "name": item.name,
                "price": item.price,
                "unit": item.unit,
                "tagId": item.tag_id
            })
        return jsonify(list(results.values()))

    def get(self, tag_id):
        tag = Tag.query.get(tag_id)
        return self.tag_schema.jsonify(tag)

    def create(self, data):
        tag = Tag.query.filter_by(name=data['name']).first()
        if not tag:
            new_tag = Tag(name=data['name'])
            save(new_tag)
            return self.tag_schema.jsonify(new_tag)

    def update(self, tag_id, data):
        tag = Tag.query.get(tag_id)
        if tag:
            tag.name = data['name']
            save(tag)
            return self.tag_schema.jsonify(tag)

    def delete(self, tag_id):
        tag = Tag.query.get(tag_id)
        if tag:
            delete(tag)
            return tag_id
