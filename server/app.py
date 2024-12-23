from flask import  Flask, request
from flask_migrate import Migrate
from flask_cors import CORS
from utils import db
 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///chat.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

CORS(app)
migrate = Migrate(app,db)
db.init_app(app)