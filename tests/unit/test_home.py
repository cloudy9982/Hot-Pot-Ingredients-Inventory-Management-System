import unittest
from flask import Flask
from app import App
import json


class FlaskAppTestCase(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.app = App().test_client()

    def tearDown(self):
        pass

    def test_home(self):
        response = self.app.get("/")
        self.assertEqual(response.status_code, 200)
        result = json.loads(response.data.decode("utf-8"))
        assert "hello" in result
        assert result["hello"] == "world"


def suite():
    suite = unittest.TestLoader().loadTestsFromTestCase(FlaskAppTestCase)
    return suite


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite())
