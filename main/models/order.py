from ._db import db


class Order(db.Model):
    __tablename__ = 'order'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # lineItemsName = db.Column(db.)
    amount = db.Column(db.String(5), nullable=False)

    def __init__(self, amount):
        self.amount = amount
