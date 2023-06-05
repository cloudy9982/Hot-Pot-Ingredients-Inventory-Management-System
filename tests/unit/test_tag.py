import unittest
from flask import Flask
from app import App
import json
from main.models.tag import Tag
from main.models._db import db
from main.schemas._ma import ma
import logging
import os
from tests.functional.tag import testTag


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
        db.session.add(tag1)
        db.session.add(tag2)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_all_tag(self):
        return testTag.all_Tag(self)

    def test_get_tag(self):
        return testTag.get(self)

    def test_create_tag(self):
        return testTag.create(self)

    def test_update_tag(self):
        return testTag.update(self)

    def test_delete_tag(self):
        return testTag.delete(self)


def suite():
    suite = unittest.TestLoader().loadTestsFromTestCase(FlaskAppTestCase)
    return suite


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite())
