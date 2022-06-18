from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = config.SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = config.SQLALCHEMY_TRACK_MODIFICATIONS

db = SQLAlchemy(app)

class Game(db.Model):
    __tablename__ = "games"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    publisher = db.Column(db.Text, nullable=False)

db.drop_all()
db.create_all()
db.session.add_all([
    Game(name='GTA V', price='99.9', publisher='Rockstar Games'),
    Game(name='Red Dead Redemption 2', price='76.6', publisher='Rockstar Games'),
    Game(name='Uncharted 3', price='65.2', publisher='Naughty Dog')
])
db.session.commit()
