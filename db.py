from main.models.item import Item
from main.models.tag import Tag
from main.models.order import Order, LineItem
from main.models._db import db
from app import App

app = App()

# 生成假資料
fake_items = [
    Item(name="青椒", price=20, unit="個", tag_id=1),
    Item(name="香菇", price=15, unit="個", tag_id=1),
    Item(name="杏鮑菇", price=15, unit="個", tag_id=1),
    Item(name="大根（白蘿蔔）", price=20, unit="個", tag_id=1),
    Item(name="玉米筍（4支）", price=20, unit="籃", tag_id=1),
    Item(name="娃娃菜", price=20, unit="把", tag_id=1),
    Item(name="高麗菜", price=30, unit="籃", tag_id=1),
    Item(name="手工黑輪", price=10, unit="個", tag_id=2),
    Item(name="米血", price=10, unit="個", tag_id=2),
    Item(name="貢丸", price=10, unit="顆", tag_id=2),
    Item(name="龍蝦沙拉丸", price=10, unit="顆", tag_id=2),
    Item(name="魚包蛋", price=15, unit="顆", tag_id=2),
    Item(name="北海貝", price=15, unit="個", tag_id=2),
    Item(name="魚豆腐（2個）", price=15, unit="籃", tag_id=2),
    Item(name="百頁豆腐", price=15, unit="個", tag_id=2),
    Item(name="油豆腐", price=20, unit="個", tag_id=2),
    Item(name="鳥蛋", price=20, unit="顆", tag_id=2),
    Item(name="手工高麗菜捲", price=20, unit="捲", tag_id=2),
    Item(name="豬肉片", price=20, unit="串", tag_id=2),
    Item(name="牛肉片", price=25, unit="串", tag_id=2),
    Item(name="石斑魚條", price=25, unit="串", tag_id=2),
    Item(name="王子麵", price=15, unit="包", tag_id=3),
    Item(name="意麵", price=15, unit="包", tag_id=3),
    Item(name="烏龍麵", price=20, unit="包", tag_id=3),
    Item(name="荷包蛋", price=20, unit="個", tag_id=3),
    Item(name="蔥蛋", price=25, unit="個", tag_id=3),
    Item(name="可口可樂", price=25, unit="瓶", tag_id=4),
    Item(name="雪碧", price=25, unit="瓶", tag_id=4),
    Item(name="蘋果汁", price=25, unit="罐", tag_id=4),
    Item(name="檸檬風味茶", price=25, unit="罐", tag_id=4)
]
fake_tags = [Tag(name="季節時蔬"), Tag(name="關東煮"),Tag(name="主食類/其他"),Tag(name="飲品")]

lineitem1 = [
    LineItem(amount=3, item_id=1, name="青椒", price=20, unit="個"),
    LineItem(amount=1, item_id=22, name="王子麵", price=20, unit="包"),
]
lineitem2 = [
    LineItem(amount=2, item_id=1, name="青椒", price=20, unit="個"),
    LineItem(amount=4, item_id=27, name="可口可樂", price=30, unit="瓶"),
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
