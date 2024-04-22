from flask import Blueprint, request, jsonify
from flask import current_app as app
from controllers.genresController import get_all_genre_controller, get_genre_by_id_controller, get_genre_by_name_controller, delete_genre_by_id_controller, update_genre_by_id_controller, create_genre_controller
genre_bp = Blueprint('genre', __name__)

def init_app(app):
    @app.route('/api/genre', methods=['GET'])
    def get_genre():
        mysql = app.config['mysql']  # Access mysql from the app's configuration
        return get_all_genre_controller(mysql)
    @app.route('/api/genre/<int:id>', methods=['GET'])
    def get_genre_by_id(id):
        mysql = app.config['mysql']  # Access mysql from the app's configuration
        return get_genre_by_id_controller(mysql,id)
    @app.route('/api/genre/<name>', methods=['GET'])
    def get_genre_by_name(name):
        mysql = app.config['mysql']  # Access mysql from the app's configuration
        return get_genre_by_name_controller(mysql,name)
    @app.route('/api/genre/<genreid>', methods=['DELETE'])
    def delete_genre_by_id(genreid):
        mysql = app.config['mysql']  # Access mysql from the app's configuration
        return delete_genre_by_id_controller(mysql,genreid)
    @app.route('/api/genre/<genreid>', methods=['PUT'])
    def update_genre_by_id(genreid):
        mysql = app.config['mysql']  # Access mysql from the app's configuration
        name = request.json['name']
        icon = request.json['icon']
        return update_genre_by_id_controller(mysql,genreid, name, icon)
    @app.route('/api/genre', methods=['POST'])
    def create_genre():
        mysql = app.config['mysql']  # Access mysql from the app's configuration
        name = request.json['name']
        icon = request.json['icon']
        return create_genre_controller(mysql, name, icon)