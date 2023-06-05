import unittest
from flask import Flask
from app import App
import json
from main.models.item import Item
from main.models.tag import Tag
from main.models.order import Order, LineItem
from main.models._db import db
from main.schemas._ma import ma
from main.schemas.order import OrderSchema
import logging
import os
from main.models._db import save


class FlaskAppTestCase(unittest.TestCase):
    @classmethod
    def setUp(self):
        if os.path.exists("../../instance/back_demo.db"):
            os.remove("back_demo.db")
        self.app = App().test_client()
        logging.getLogger("werkzeug").setLevel(logging.ERROR)
        self.app_context = App().app_context()
        self.app_context.push()
        db.create_all()

        fake_items = [
            Item(name="青椒", price=20, unit="顆", tag_id=1),
            Item(name="花生", price=30, unit="粒", tag_id=2),
        ]
        fake_tags = [Tag(name="蔬菜"), Tag(name="關東煮")]

        lineitem1 = [
            LineItem(amount=3, item_id=1, name="青椒", price=20, unit="個"),
            LineItem(amount=1, item_id=2, name="花生", price=30, unit="粒"),
        ]
        lineitem2 = [
            LineItem(amount=2, item_id=1, name="青椒", price=20, unit="個"),
            LineItem(amount=4, item_id=2, name="花生", price=30, unit="粒"),
        ]

        order1 = Order(username="cloudy", lineitems=lineitem1)
        order2 = Order(username="sunny", lineitems=lineitem2)
        order1.lineitems = lineitem1
        order2.lineitems = lineitem2

        fake_orders = [order1, order2]

        for item in fake_items:
            db.session.add(item)

        for tag in fake_tags:
            db.session.add(tag)

        for order in fake_orders:
            db.session.add(order)

        for lineitem in lineitem1 + lineitem2:
            db.session.add(lineitem)

        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_all_order(self):
        response = self.app.get("/order")
        self.assertEqual(response.status_code, 200)
        result = json.loads(response.data.decode("utf-8"))
        self.assertIsInstance(result, list)  # 是否為list
        self.assertGreater(len(result), 0)  # data長度超過0

    def test_create_order(self):
        lineitems_data = {"lineitems": [{"id": 2, "amount": 1}]}
        data = lineitems_data["lineitems"]
        lineitems = []
        for lineitem_data in data:
            item_id = lineitem_data["id"]
            amount = lineitem_data["amount"]
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
        lineitems_json = [lineitem.to_json() for lineitem in lineitems]
        order_json = {"username": "test", "lineitems": lineitems_json}
        response = self.app.post("/order", json=order_json)
        self.assertEqual(response.status_code, 200)

        result = json.loads(response.data.decode("utf-8"))
        self.assertIsInstance(result, dict)
        self.assertIn("id", result)
        self.assertEqual(result["username"], "test")
