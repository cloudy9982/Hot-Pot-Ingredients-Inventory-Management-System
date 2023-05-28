from main.models.item import Item
from main.models.tag import Tag
from main.models._db import db
from faker import Faker
from app import App

fake = Faker()

app = App()

# 生成假資料
fake_items = []
fake_tags = []

# item
for _ in range(6):
    name = fake.word()
    price = str(fake.random_int(min=1, max=6))
    unit = fake.word()
    tag_id = fake.random_int(min=1, max=6)
    item = Item(name=name, price=price, unit=unit, tag_id=tag_id)
    fake_items.append(item)

# tag
for _ in range(6):
    name = fake.word()
    tag = Tag(name=name)
    fake_tags.append(tag)

with app.app_context():
    # 將假資料插入資料庫
    for item in fake_items:
        db.session.add(item)

    for tag in fake_tags:
        db.session.add(tag)
    db.session.commit()
