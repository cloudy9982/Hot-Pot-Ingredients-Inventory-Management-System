import unittest
from flask import Flask
from app import App
import logging
import os
from tests.functional.home import testHome


class FlaskAppTestCase(unittest.TestCase):
    @classmethod
    def setUp(self):
        if os.path.exists("back_demo.db"):
            os.remove("back_demo.db")
        self.app = App().test_client()
        logging.getLogger("werkzeug").setLevel(logging.ERROR)

    def tearDown(self):
        pass

    def test_home(self):
        return testHome()


def suite():
    suite = unittest.TestLoader().loadTestsFromTestCase(FlaskAppTestCase)
    return suite


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite())
