from ._db import db


class Item(db.Model):
    __tablename__ = 'item'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    unit = db.Column(db.String(5), nullable=False)
    tag_id = db.Column(db.String(20), db.ForeignKey(
        'tag.id'), nullable=False)

    def __init__(self, name, price, unit, tag_id):
        self.name = name
        self.price = price
        self.unit = unit
        self.tag_id = tag_id
