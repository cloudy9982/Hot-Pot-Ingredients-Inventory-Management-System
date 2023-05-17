from flask import request
from flask_restful import Resource
from main.services.item import ItemService

service = ItemService()


class GetAllItem(Resource):
    def get(self):
        return service.get_all()


class GetItem(Resource):
    def get(self, id):
        return service.get(item_id=id)


class PostItem(Resource):
    def post(self):
        return service.create(data=request.json)


class UpdateItem(Resource):
    def put(self, id):
        return service.update(item_id=id, data=request.json)


class DeleteItem(Resource):
    def delete(self, id):
        return service.delete(item_id=id)
