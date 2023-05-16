from main.models.tag import Tag
from ._ma import ma


class TagSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Tag
