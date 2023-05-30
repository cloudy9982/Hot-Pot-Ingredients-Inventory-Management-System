import unittest
from flask import Flask
from app import App
import json
from main.models.tag import Tag
from main.models._db import db
from main.schemas._ma import ma


class FlaskAppTestCase(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.app = App().test_client()
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
        response = self.app.get("/tag")
        self.assertEqual(response.status_code, 200)
        result = json.loads(response.data.decode("utf-8"))
        self.assertIsInstance(result, list)  # 是否為list
        self.assertGreater(len(result), 0)  # data長度超過0

    def test_get_tag(self):
        tag_id = 1
        response = self.app.get(f"/tag/{tag_id}")
        self.assertEqual(response.status_code, 200)
        result = json.loads(response.data.decode("utf-8"))
        self.assertIsInstance(result, dict)  # 是否為dict
        self.assertGreater(len(result), 0)  # data長度超過0
        self.assertIn("name", result)  # 檢查字典是否包含 'name' 鍵
        self.assertEqual(result["name"], "蔬菜")  # 檢查 'name' 鍵對應的值是否為 '蔬菜'

    def test_create_tag(self):
        data = {"name": "炸物"}
        response = self.app.post("/tag", json=data)
        self.assertEqual(response.status_code, 200)

        result = json.loads(response.data.decode("utf-8"))
        self.assertIsInstance(result, dict)  # 是否為 dict
        self.assertIn("tag_id", result)  # 檢查字典是否包含 'id' 鍵
        self.assertEqual(result["name"], "炸物")  # 檢查 'name' 鍵對應的值是否為 '炸物'

    def test_update_tag(self):
        # 假設要更新的項目的 ID 為 1
        tag_id = 1

        # 新的項目資料
        updated_data = {"name": "麵類"}

        # 發送 PUT 請求
        response = self.app.put(f"/tag/{tag_id}", json=updated_data)

        # 檢查回應的狀態碼是否為 200 OK
        self.assertEqual(response.status_code, 200)

        # 檢查項目是否被成功更新
        # 可以根據你的需求使用不同的方法來檢查更新後的結果
        # 例如可以發送 GET 請求，然後檢查回傳的資料是否符合更新後的內容
        updated_tag_response = self.app.get(f"/tag/{tag_id}")
        self.assertEqual(updated_tag_response.status_code, 200)
        updated_tag = json.loads(updated_tag_response.data.decode("utf-8"))
        self.assertEqual(updated_tag["name"], updated_data["name"])

    def test_delete_tag(self):
        tag_id = 1
        response = self.app.delete(f"/tag/{tag_id}")
        self.assertEqual(response.status_code, 200)

        # 檢查項目是否被成功刪除
        tag_response = self.app.get(f"/tag/{tag_id}")
        # self.assertEqual(tag_response, "null")


def suite():
    suite = unittest.TestLoader().loadTestsFromTestCase(FlaskAppTestCase)
    return suite


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite())
