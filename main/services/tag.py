from main.models._db import save, delete
from flask import jsonify
from main.models.tag import Tag
from main.schemas.tag import TagSchema
from main.models.item import Item


class TagService:
    def __init__(self):
        self.tag_schema = TagSchema()
        self.tags_schema = TagSchema(many=True)

    # def get_all(self):
    #     tags = Tag.query.all()
    #     results = {}
    #     for tag in tags:
    #         results[tag.tag_id] = {
    #             "id": tag.tag_id,
    #             "name": tag.name,
    #             "items": []
    #         }
    #         items = Item.query.filter_by(tag_id=tag.tag_id).all()
    #         for item in items:
    #             item_data = {
    #                 "id": item.id,
    #                 "name": item.name,
    #                 "price": item.price,
    #                 "unit": item.unit,
    #                 "tagId": item.tag_id
    #             }
    #             results[tag.tag_id]["items"].append(item_data)
    #     return jsonify(list(results.values()))

    def get_all(self):
        try:
            tags = Tag.query.all()
            results = {}
            for tag in tags:
                results[tag.tag_id] = {"id": tag.tag_id, "name": tag.name, "items": []}
                items = Item.query.filter_by(tag_id=tag.tag_id).all()
                for item in items:
                    item_data = {
                        "id": item.id,
                        "name": item.name,
                        "price": item.price,
                        "unit": item.unit,
                        "tagId": item.tag_id,
                    }
                    results[tag.tag_id]["items"].append(item_data)
            return jsonify(list(results.values()))
        except Exception as e:
            error_message = str(e)  # 获取错误信息
            return jsonify({"error": error_message})

    def get(self, tag_id):
        tag = Tag.query.get(tag_id)
        return self.tag_schema.jsonify(tag)

    def create(self, data):
        tag = Tag.query.filter_by(name=data["name"]).first()
        if not tag:
            new_tag = Tag(name=data["name"])
            save(new_tag)
            return self.tag_schema.jsonify(new_tag)

    def update(self, tag_id, data):
        tag = Tag.query.get(tag_id)
        if tag:
            tag.name = data["name"]
        save(tag)
        return self.tag_schema.jsonify(tag)

    def delete(self, tag_id):
        tag = Tag.query.get(tag_id)
        if tag:
            delete(tag)
            return tag_id
