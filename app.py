from flask import Flask, request, make_response
from flask_restful import Api
from flask_migrate import Migrate
from flask_cors import CORS
from main.controllers.welcome import HelloWorld
from main.controllers.item import GetAllItem, GetItem, PostItem, UpdateItem, DeleteItem
from main.controllers.tag import GetAllTag, GetTag, PostTag, UpdateTag, DeleteTag
from main.controllers.order import GetAllOrder, PostOrder
from main.models._db import db
from main.schemas._ma import ma
from flask_socketio import SocketIO


class App(Flask):
    def __init__(self):
        super().__init__(__name__)
        self.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///./back_demo.db"
        self.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

        cors = CORS(self, resources={r"/*": {"origins": "*"}})
        api = Api(self)
        db.init_app(self)
        ma.init_app(self)
        migrate = Migrate(self, db)

        # api
        api.add_resource(HelloWorld, "/")  # ok
        # Item api
        api.add_resource(GetAllItem, "/item")  # ok
        api.add_resource(GetItem, "/item/<int:id>")  # ok
        api.add_resource(PostItem, "/item")  # ok
        api.add_resource(UpdateItem, "/item/<int:id>")  # ok
        api.add_resource(DeleteItem, "/item/<int:id>")  # ok
        # Tag api
        api.add_resource(GetAllTag, "/tag")  # ok
        api.add_resource(GetTag, "/tag/<int:id>")  # ok
        api.add_resource(PostTag, "/tag")  # ok
        api.add_resource(UpdateTag, "/tag/<int:id>")  # ok
        api.add_resource(DeleteTag, "/tag/<int:id>")  # ok

        # Order api
        api.add_resource(GetAllOrder, "/order")  # ok
        api.add_resource(PostOrder, "/order")  # ok

        with self.app_context():
            db.create_all()


if __name__ == "__main__":
    app = App()
    CORS(app)
    socketio = SocketIO(app, cors_allowed_origins="*")
    app.run(debug=True, port=8081)
