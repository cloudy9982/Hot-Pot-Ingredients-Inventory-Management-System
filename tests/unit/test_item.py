import unittest
from flask import Flask
from app import App
import json
from main.models.item import Item
from main.models.tag import Tag
from main.models._db import db
from main.schemas._ma import ma


class FlaskAppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = App().test_client()
        self.app_context = App().app_context()
        self.app_context.push()

        # 加入假資料
        tag1 = Tag(name='蔬菜')
        tag2 = Tag(name='關東煮')
        item1 = Item(name='青椒', price='20', unit='顆', tag_id='1')
        item2 = Item(name='花生', price='20', unit='粒', tag_id='2')
        db.session.add(tag1)
        db.session.add(tag2)
        db.session.add(item1)
        db.session.add(item2)
        db.session.commit()

    def tearDown(self):
        # db.session.remove()
        # db.drop_all()
        pass

    def test_home(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        result = json.loads(response.data.decode('utf-8'))
        assert 'hello' in result
        assert result['hello'] == 'world'

    def test_all_item(self):
        response = self.app.get('/item')
        self.assertEqual(response.status_code, 200)
        result = json.loads(response.data.decode('utf-8'))
        self.assertIsInstance(result, list)  # 是否為list
        self.assertGreater(len(result), 0)  # data長度超過0

    def test_get_item(self):
        response = self.app.get('/item/1')
        self.assertEqual(response.status_code, 200)
        result = json.loads(response.data.decode('utf-8'))
        self.assertIsInstance(result, dict)  # 是否為dict
        self.assertGreater(len(result), 0)  # data長度超過0

    # def test_post_item(self):
    #     # data = {
    #     #     'name': '西紅柿',
    #     #     'price': '20',
    #     #     'unit': '顆',
    #     #     'tag': '1'
    #     # }
    #     # response = self.app.post('/item', data=data)
    #     # self.assertEqual(response.status_code, 200)
    #     # print(response.data)
    #     # result = json.loads(response.data)
    #     # print(result)
    #     data = {'name': 'Alice'}
    #     response = self.app.post('/item', json=data)
    #     print(response.data)
    #     result = response.get_json()

    #     # 檢查回傳的結果
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(result['message'], 'Hello, Alice!')
    #     # self.assertIsInstance(result, dict)
    #     # item = Item.query.filter_by(name=data['name']).first()
    #     # self.assertIsNotNone(item)
    #     # self.assertEqual(item.name, data['name'])
    #     # self.assertEqual(result['name'], '西紅柿')
    #     # self.assertEqual(result['price'], '20')
    #     # self.assertEqual(result['unit'], '顆')
    #     # self.assertEqual(result['tag'], '1')


def suite():
    suite = unittest.TestLoader().loadTestsFromTestCase(FlaskAppTestCase)
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
