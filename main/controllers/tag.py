from flask import request
from flask_restful import Resource
from main.services.tag import TagService

service = TagService()


class GetAllTag(Resource):
    def get(self):
        return service.get_all()


class GetTag(Resource):
    def get(self, id):
        return service.get(tag_id=id)


class PostTag(Resource):
    def post(self):
        return service.create(data=request.json)


class UpdateTag(Resource):
    def put(self, id):
        return service.update(tag_id=id, data=request.json)


class DeleteTag(Resource):
    def delete(self, id):
        return service.delete(tag_id=id)
