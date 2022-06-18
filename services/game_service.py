from models.game_model import Game
from app import db

# Helper function
def error(message):
    return { "error": message }

# Service functions
def get_games():
    return [obj.as_dict() for obj in Game.query.all()]

def get_game_by_id(id):
    game = Game.query.filter_by(id = id).first()
    if game is None:
        return error(f"Unable to locate game with id: {id}")

    return game.as_dict()

def insert_game(body):
    db.session.add(Game(
        name=body["name"],
        price=body["price"],
        publisher=body["publisher"]
    ))
    db.session.commit()

    return {}

def update_game(id, body):    
    game = get_game_by_id(id)
    if game.get("error"):
        return game
    
    game = Game.query.filter_by(id = id).one()
    game.name = body["name"]
    game.price = body["price"]
    game.publisher = body["publisher"]
    db.session.commit()

    return {}

def delete_game(id):
    game = get_game_by_id(id)
    if game.get("error"):
        return game

    Game.query.filter_by(id = id).delete()
    db.session.commit()

    return {}
