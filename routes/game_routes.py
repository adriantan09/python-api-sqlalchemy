from flask import request, jsonify
from app import app
from services import game_service

@app.route("/games", methods=["GET"])
def get_games():
    return jsonify(game_service.get_games())

@app.route("/game/<id>", methods=["GET"])
def get_game_by_id(id):
    return jsonify(game_service.get_game_by_id(id))

@app.route("/game", methods=["POST"])
def insert_game():
    return jsonify(game_service.insert_game(request.get_json()))

@app.route("/game/<id>", methods=["PUT"])
def update_game(id):
    return jsonify(game_service.update_game(id, request.get_json()))

@app.route("/game/<id>", methods=["DELETE"])
def delete_game(id):
    return jsonify(game_service.delete_game(id))
