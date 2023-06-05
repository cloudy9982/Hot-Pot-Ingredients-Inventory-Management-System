from main.models._db import save, delete
from flask import jsonify
from main.models.order import Order, LineItem
from main.models.item import Item
from main.schemas.order import OrderSchema
import pytz

tz = pytz.timezone("Asia/Taipei")


class OrderService:
    def __init__(self):
        self.order_schema = OrderSchema()
        self.orders_schema = OrderSchema(many=True)

    def get_all(self):
        orders = Order.query.all()
        results = []
        for order in orders:
            lineitems = LineItem.query.filter_by(order_id=order.id).all()
            lineitems_data = []
            for item in lineitems:
                lineitems_data.append(
                    {
                        "id": item.item_id,
                        "amount": item.amount,
                        "name": item.name,
                        "price": item.price,
                        "unit": item.unit,
                        "totalPrice": item.totalPrice,
                    }
                )
            results.append(
                {
                    "id": order.id,
                    "date": order.time.strftime("%Y-%m-%d %H:%M:%S"),
                    "username": order.username,
                    "totalPrice": order.totalPrice,
                    "lineitems": lineitems_data,
                }
            )
        return jsonify(results)

    def create(self, data):
        username = data["username"]
        lineitems_data = data["lineitems"]

        # 創建並關聯LineItem
        lineitems = []
        for lineitem_data in lineitems_data:
            item_id = lineitem_data["id"]
            amount = lineitem_data["amount"]

            # 根據item_id查詢對應的Item資料
            item = Item.query.get(item_id)

            if item:
                lineitem = LineItem(
                    item_id=item.id,
                    name=item.name,
                    price=item.price,
                    unit=item.unit,
                    amount=amount,
                )
                lineitems.append(lineitem)
        # 創建訂單
        order = Order(username=username, lineitems=lineitems)

        save(order)
        for lineitem in lineitems:
            save(lineitem)
        return self.order_schema.jsonify(order)
