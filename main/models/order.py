from datetime import datetime
from ._db import db
import pytz

tz = pytz.timezone("Asia/Taipei")


class Order(db.Model):
    __tablename__ = "order"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    time = db.Column(db.DateTime, default=datetime.now(tz))
    username = db.Column(db.String(20), nullable=False)
    totalPrice = db.Column(db.Integer, default=0)
    # Define the relationship with LineItem
    lineitems = db.relationship(
        "LineItem", backref="order", cascade="all, delete-orphan"
    )

    def __init__(self, username, lineitems):
        self.username = username
        self.lineitems = lineitems
        self.totalPrice = self.calculate_total_price(lineitems)

    def calculate_total_price(self, lineitems):
        totalPrice = 0
        for lineitem in lineitems:
            totalPrice += lineitem.price * lineitem.amount
        return totalPrice


class LineItem(db.Model):
    __tablename__ = "lineitem"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    item_id = db.Column(db.Integer)
    name = db.Column(db.String(20), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    unit = db.Column(db.String(5), nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    totalPrice = db.Column(db.Integer, nullable=False)
    order_id = db.Column(db.Integer, db.ForeignKey("order.id"), nullable=False)

    def __init__(self, item_id, name, price, unit, amount):
        self.amount = amount
        self.item_id = item_id
        self.name = name
        self.price = price
        self.unit = unit
        self.totalPrice = self.amount * self.price
