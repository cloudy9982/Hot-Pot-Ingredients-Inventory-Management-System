from main.models.item import Item
from main.models.tag import Tag
from main.models.order import Order
from main.models._db import db
from faker import Faker
from app import App

fake = Faker()

app = App()

# 生成假資料
fake_items = []
fake_tags = []
fake_orders = []

# item
item = Item(name="青椒", price="20", unit="個", tag_id='1')
fake_items.append(item)
item = Item(name='花生', price='20', unit='粒', tag_id='2')
fake_items.append(item)

# tag
tag = Tag(name='蔬菜')
fake_tags.append(tag)
tag = Tag(name='關東煮')
fake_tags.append(tag)

# order
amount = fake.random_int(min=1, max=6)
order = Order(amount=amount)  # 创建订单模型类的实例
fake_orders.append(order)  # 将订单实例添加到fake_orders列表中

with app.app_context():
    # 將假資料插入資料庫
    for item in fake_items:
        db.session.add(item)

    for tag in fake_tags:
        db.session.add(tag)

    for order in fake_orders:
        db.session.add(order)
    db.session.commit()
