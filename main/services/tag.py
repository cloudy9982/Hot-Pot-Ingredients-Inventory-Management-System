from main.models._db import save, delete
from flask import jsonify
from main.models.tag import Tag
from main.schemas.tag import TagSchema


class TagService:
    def __init__(self):
        self.tag_schema = TagSchema()
        self.tags_schema = TagSchema(many=True)

    def get_all(self):
        tags = Tag.query.all()
        return jsonify(self.tags_schema.dump(tags))

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