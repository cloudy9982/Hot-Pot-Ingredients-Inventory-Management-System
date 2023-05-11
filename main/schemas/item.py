from main.models.item import Item
from ._ma import ma


class ItemSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Item
