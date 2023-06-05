import unittest
from flask import Flask
from app import App
import json
from main.models.item import Item
from main.models.tag import Tag
from main.models._db import db
from main.schemas._ma import ma
import logging
import os
from tests.functional.item import testItem


class FlaskAppTestCase(unittest.TestCase):
    @classmethod
    def setUp(self):
        if os.path.exists("back_demo.db"):
            os.remove("back_demo.db")
        self.app = App().test_client()
        logging.getLogger("werkzeug").setLevel(logging.ERROR)
        self.app_context = App().app_context()
        self.app_context.push()
        db.create_all()

        # 加入假資料
        tag1 = Tag(name="蔬菜")
        tag2 = Tag(name="關東煮")
        item1 = Item(name="青椒", price=20, unit="顆", tag_id=1)
        item2 = Item(name="花生", price=20, unit="粒", tag_id=2)
        db.session.add(tag1)
        db.session.add(tag2)
        db.session.add(item1)
        db.session.add(item2)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_all_item(self):
        return testItem.all_Item(self)

    def test_get_item(self):
        return testItem.get(self)

    def test_create_item(self):
        return testItem.create(self)

    def test_update_item(self):
        return testItem.update(self)

    def test_delete_item(self):
        return testItem.delete(self)


def suite():
    suite = unittest.TestLoader().loadTestsFromTestCase(FlaskAppTestCase)
    return suite


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite())
