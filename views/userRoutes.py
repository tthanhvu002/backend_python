from flask import Blueprint, request, jsonify
from flask import current_app as app
from controllers.usersController import get_all_users_controller, get_user_by_id_controller, get_user_by_name_controller, delete_user_by_id_controller, update_user_by_id_controller

user_bp = Blueprint('user', __name__)
def init_app(app):
    @app.route('/api/users', methods=['GET'])
    def get_users():
        mysql = app.config['mysql']  # Access mysql from the app's configuration
        return get_all_users_controller(mysql)
    @app.route('/api/users/<id>', methods=['GET'])
    def get_users_by_id(id):
        mysql = app.config['mysql']  # Access mysql from the app's configuration    
        return get_user_by_id_controller(mysql,id)
    @app.route('/api/users/<name>', methods=['GET'])
    def get_users_by_name(name):
        mysql = app.config['mysql']  # Access mysql from the app's configuration
        return get_user_by_name_controller(mysql,name)
    @app.route('/api/users/<id>', methods=['DELETE'])
    def delete_users_by_id(id):
        mysql = app.config['mysql']  # Access mysql from the app's configuration
        return delete_user_by_id_controller(mysql,id)
    @app.route('/api/users/<id>', methods=['PUT'])
    def update_users_by_id(id):
        mysql = app.config['mysql']  # Access mysql from the app's configuration
        name = request.json['name']
        email = request.json['email']
        phone = request.json['phone']
        address = request.json['address']
        return update_user_by_id_controller(mysql,id, name, email, phone,address)