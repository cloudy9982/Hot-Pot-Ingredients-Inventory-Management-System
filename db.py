from main.models.item import Item
from main.models.tag import Tag
from main.models.order import Order, LineItem
from main.models._db import db
from faker import Faker
from app import App

fake = Faker()

app = App()

# 生成假資料
fake_items = [
    Item(name="青椒", price=20, unit="個", tag_id=1),
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

with app.app_context():
    for item in fake_items:
        db.session.add(item)

    for tag in fake_tags:
        db.session.add(tag)

    for order in fake_orders:
        db.session.add(order)

    for lineitem in lineitem1 + lineitem2:
        db.session.add(lineitem)

    db.session.commit()
