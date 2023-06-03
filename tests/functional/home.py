from main.models._db import save, delete
from flask import jsonify


class testHome:
    def home(self):
        response = self.app.get("/")
        self.assertEqual(response.status_code, 200)
        result = json.loads(response.data.decode("utf-8"))
        assert "hello" in result
        assert result["hello"] == "world"
