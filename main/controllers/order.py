from flask import request
from flask_restful import Resource
from main.services.order import OrderService
from google.oauth2 import id_token
from google.auth.transport import requests
import json

service = OrderService()


class GetAllOrder(Resource):
    def get(self):
        return service.get_all()


class PostOrder(Resource):
    def post(self):
        return service.create(data=request.json)
