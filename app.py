from flask import Flask
from flask_restful import Api
from flask_migrate import Migrate
from flask_cors import CORS
from main.controllers.welcome import HelloWorld
from main.controllers.item import GetAllItem, GetItem, PostItem, UpdateItem, DeleteItem
from main.controllers.tag import GetAllTag, GetTag, PostTag, UpdateTag, DeleteTag
from main.models._db import db
from main.schemas._ma import ma


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./back_demo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

api = Api(app, prefix='/api')
db.init_app(app)
ma.init_app(app)
migrate = Migrate(app, db)

# api
api.add_resource(HelloWorld, '/')
# Item api
api.add_resource(GetAllItem, '/items')
api.add_resource(GetItem, '/items/<int:id>')
api.add_resource(PostItem, '/items')
api.add_resource(UpdateItem, '/items/<int:id>')
api.add_resource(DeleteItem, '/items/<int:id>')
# Tag api
api.add_resource(GetAllTag, '/tags')
api.add_resource(GetTag, '/tags/<int:id>')
api.add_resource(PostTag, '/tags')
api.add_resource(UpdateTag, '/tags/<int:id>')
api.add_resource(DeleteTag, '/tags/<int:id>')


with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
