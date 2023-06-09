import logging
import os
import unittest
import json
from flask import jsonify
from flask import Flask
from main.models._db import save, delete
from app import App
from main.models.tag import Tag
from main.models._db import db
from main.schemas._ma import ma
from main.models.item import Item
from main.schemas.item import ItemSchema


class testItem:
    def all_Item(self):
        response = self.app.get("/item")
        self.assertEqual(response.status_code, 200)
        result = json.loads(response.data.decode("utf-8"))
        self.assertIsInstance(result, list)  # 是否為list
        self.assertGreater(len(result), 0)  # data長度超過0

    def get(self):
        item_id = 1
        response = self.app.get(f"/item/{item_id}")
        self.assertEqual(response.status_code, 200)
        result = json.loads(response.data.decode("utf-8"))
        self.assertIsInstance(result, dict)  # 是否為dict
        self.assertGreater(len(result), 0)  # data長度超過0
        self.assertIn("name", result)  # 檢查字典是否包含 'name' 鍵
        self.assertEqual(result["name"], "青椒")  # 檢查 'name' 鍵對應的值是否為 '青椒'
        self.assertIn("price", result)  # 檢查字典是否包含 'price' 鍵
        self.assertEqual(result["price"], 20)  # 檢查 'price' 鍵對應的值是否為 '20'
        self.assertIn("unit", result)  # 檢查字典是否包含 'unit' 鍵
        self.assertEqual(result["unit"], "顆")  # 檢查 'unit' 鍵對應的值是否為 '顆'

    def create(self):
        data = {"name": "番茄", "price": 30, "unit": "顆", "tag": 1}
        response = self.app.post("/item", json=data)
        self.assertEqual(response.status_code, 200)

        result = json.loads(response.data.decode("utf-8"))
        self.assertIsInstance(result, dict)  # 是否為 dict
        self.assertIn("id", result)  # 檢查字典是否包含 'id' 鍵
        self.assertEqual(result["name"], "番茄")  # 檢查 'name' 鍵對應的值是否為 '番茄'
        self.assertEqual(result["price"], 30)  # 檢查 'price' 鍵對應的值是否為 '30'
        self.assertEqual(result["unit"], "顆")  # 檢查 'unit' 鍵對應的值是否為 '顆'

    def update(self):
        # 假設要更新的項目的 ID 為 1
        item_id = 1

        # 新的項目資料
        updated_data = {"name": "竹輪", "price": 20, "unit": "條", "tag": 2}

        # 發送 PUT 請求
        response = self.app.put(f"/item/{item_id}", json=updated_data)

        # 檢查回應的狀態碼是否為 200 OK
        self.assertEqual(response.status_code, 200)

        # 檢查項目是否被成功更新
        # 可以根據你的需求使用不同的方法來檢查更新後的結果
        # 例如可以發送 GET 請求，然後檢查回傳的資料是否符合更新後的內容
        updated_item_response = self.app.get(f"/item/{item_id}")
        self.assertEqual(updated_item_response.status_code, 200)
        updated_item = json.loads(updated_item_response.data.decode("utf-8"))
        self.assertEqual(updated_item["name"], updated_data["name"])
        self.assertEqual(updated_item["price"], int(updated_data["price"]))
        self.assertEqual(updated_item["unit"], updated_data["unit"])

    def delete(self):
        item_id = 1
        response = self.app.delete(f"/item/{item_id}")
        self.assertEqual(response.status_code, 200)

        # 檢查項目是否被成功刪除
        item_response = self.app.get(f"/item/{item_id}")
        self.assertEqual(item_response.get_data(as_text=True).strip(), "{}")
