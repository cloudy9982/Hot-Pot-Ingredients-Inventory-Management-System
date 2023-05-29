from main.models._db import save, delete
from flask import jsonify
from main.models.order import Order
from main.schemas.order import OrderSchema


class OrderService:
    def __init__(self):
        self.order_schema = OrderSchema()
        self.orders_schema = OrderSchema(many=True)

    def get_all(self):
        orders = Order.query.all()
        results = []
        for order in orders:
            results.append({
                "id": order.id,
                "name": order.name,
                "price": order.price,
                "unit": order.unit,
                "tagId": order.tag_id
            })
        print(results)
        return jsonify(results)

    def get(self, order_id):
        order = order.query.get(order_id)
        return self.order_schema.jsonify(order)

    def create(self, data):  # ok
        order = order.query.filter_by(name=data['name']).first()
        if not order:
            new_order = order(
                name=data['name'],
                price=data['price'],
                unit=data['unit'],
                tag_id=data['tag']
            )
            save(new_order)
            print(jsonify(new_order))
            return self.order_schema.jsonify(new_order)
