from flask import Flask, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_swagger_ui import get_swaggerui_blueprint
import os.path
import config

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = config.SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = config.SQLALCHEMY_TRACK_MODIFICATIONS

db = SQLAlchemy(app)

# essential to register other routes
from routes import game_routes

@app.before_request
def check_database():
    if not os.path.exists('games.db'):
        raise FileNotFoundError(f'Database: {config.DATABASE_NAME} is not present. Run \'python3 init_db.py\' to generate the database.')

@app.route("/static/<path:path>")
def send_static(path):
    return send_from_directory(path)

swaggerui_blueprint = get_swaggerui_blueprint(
    "/docs", # SWAGGER_URL
    "/static/swagger.json", # API_URL
    config={ 'app_name': "Test application" }
)
app.register_blueprint(swaggerui_blueprint)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
