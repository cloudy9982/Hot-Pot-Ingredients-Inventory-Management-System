from flask import Flask
from flask_restful import Api
from flask_migrate import Migrate
from flask_cors import CORS
from main.controllers.welcome import HelloWorld
from main.controllers.item import GetAllItem, GetItem, PostItem, UpdateItem, DeleteItem
from main.controllers.tag import GetAllTag, GetTag, PostTag, UpdateTag, DeleteTag
from main.models._db import db
from main.schemas._ma import ma


class App(Flask):
    def __init__(self):
        super().__init__(__name__)
        self.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./back_demo.db'
        self.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

        cors = CORS(self, resources={r"/*": {"origins": "*"}})

        api = Api(self)
        db.init_app(self)
        ma.init_app(self)
        migrate = Migrate(self, db)

        # api
        api.add_resource(HelloWorld, '/')
        # Item api
        api.add_resource(GetAllItem, '/item')
        api.add_resource(GetItem, '/item/<int:id>')
        api.add_resource(PostItem, '/item')
        api.add_resource(UpdateItem, '/item/<int:id>')
        api.add_resource(DeleteItem, '/item/<int:id>')
        # Tag api
        api.add_resource(GetAllTag, '/tag')
        api.add_resource(GetTag, '/tags/<int:id>')
        api.add_resource(PostTag, '/tags')
        api.add_resource(UpdateTag, '/tags/<int:id>')
        api.add_resource(DeleteTag, '/tags/<int:id>')

        with self.app_context():
            db.create_all()


if __name__ == '__main__':
    app = App()
    app.run(debug=True)
