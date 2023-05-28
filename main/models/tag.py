from ._db import db


class Tag(db.Model):
    __tablename__ = 'tag'
    tag_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False)

    db_Tag_Item = db.relationship("Item", backref="tag")

    def __init__(self, name):
        self.name = name
