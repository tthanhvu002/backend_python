from flask import Blueprint, request, jsonify
from flask import current_app as app
from controllers.authorsController import get_authors_controller, get_author_by_id_controller, get_author_by_bookID_controller, get_author_by_name_controller, create_author_controller, delete_author_by_id_controller, update_author_by_id_controller

author_bp = Blueprint('author', __name__) 
@author_bp.route('/api/authors', methods=['GET'])
def get_authors():
    mysql = app.config['mysql']  # Access mysql from the app's configuration
    
    return get_authors_controller(mysql)
@author_bp.route('/api/authors/<id>', methods=['GET'])
def get_author_by_id(id):
    mysql = app.config['mysql']  # Access mysql from the app's configuration
    return get_author_by_id_controller(mysql,id)
@author_bp.route('/api/authors/<bookID>', methods=['GET'])
def get_author_by_bookID(bookID):
    mysql = app.config['mysql']  # Access mysql from the app's configuration
    return get_author_by_bookID_controller(mysql,bookID)
@author_bp.route('/api/authors/<name>', methods=['GET'])
def get_author_by_name(name):
    mysql = app.config['mysql']  # Access mysql from the app's configuration
    return get_author_by_name_controller(mysql,name)
@author_bp.route('/api/authors', methods=['POST'])
def create_author():
    mysql = app.config['mysql']  # Access mysql from the app's configuration
    name = request.json['name']
    description = request.json['description']
    image = request.json['image']
    return create_author_controller(mysql,name, description, image)
@author_bp.route('/api/authors/<id>', methods=['DELETE'])
def delete_author_by_id(id):
    mysql = app.config['mysql']  # Access mysql from the app's configuration
    return delete_author_by_id_controller(mysql,id)

@author_bp.route('/api/authors/<id>', methods=['PUT'])
def update_author_by_id(id):
    mysql = app.config['mysql']  # Access mysql from the app's configuration
    name = request.json['name']
    description = request.json['description']
    image = request.json['image']
    return update_author_by_id_controller(mysql,id, name, description, image)