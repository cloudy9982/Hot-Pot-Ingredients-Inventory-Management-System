from flask import request
from flask_restful import Resource
from main.services.order import OrderService

service = OrderService()


class GetAllOrder(Resource):
    def get(self):
        return service.get_all()


class GetOrder(Resource):
    def get(self, id):
        return service.get(order_id=id)


class PostOrder(Resource):
    def post(self):
        return service.create(data=request.json)


class UpdateOrder(Resource):
    def put(self, id):
        return service.update(order_id=id, data=request.json)


class DeleteOrder(Resource):
    def delete(self, id):
        return service.delete(order_id=id)
