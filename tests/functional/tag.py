import logging
import os
import unittest
import json
from main.models._db import save, delete
from flask import jsonify
from flask import Flask
from app import App
from main.models.tag import Tag
from main.models._db import db
from main.schemas._ma import ma
from flask import request
from flask_restful import Resource
from main.services.tag import TagService


class testTag:
    def all_Tag(self):
        response = self.app.get("/tag")
        self.assertEqual(response.status_code, 200)
        result = json.loads(response.data.decode("utf-8"))
        self.assertIsInstance(result, list)  # 是否為list
        self.assertGreater(len(result), 0)  # data長度超過0

    def get(self):
        tag_id = 1
        response = self.app.get(f"/tag/{tag_id}")
        self.assertEqual(response.status_code, 200)
        result = json.loads(response.data.decode("utf-8"))
        self.assertIsInstance(result, dict)  # 是否為dict
        self.assertGreater(len(result), 0)  # data長度超過0
        self.assertIn("name", result)  # 檢查字典是否包含 'name' 鍵
        self.assertEqual(result["name"], "蔬菜")  # 檢查 'name' 鍵對應的值是否為 '蔬菜'

    def create(self):
        data = {"name": "炸物"}
        response = self.app.post("/tag", json=data)
        self.assertEqual(response.status_code, 200)

        result = json.loads(response.data.decode("utf-8"))
        self.assertIsInstance(result, dict)  # 是否為 dict
        self.assertIn("tag_id", result)  # 檢查字典是否包含 'id' 鍵
        self.assertEqual(result["name"], "炸物")  # 檢查 'name' 鍵對應的值是否為 '炸物'

    def update(self):
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

    def delete(self):
        tag_id = 1
        response = self.app.delete(f"/tag/{tag_id}")
        self.assertEqual(response.status_code, 200)
