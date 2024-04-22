from flask import Blueprint, request, jsonify
from flask import current_app as app
from controllers.bookController import get_all_books_controller, get_book_by_id_controller, get_book_by_name_controller, get_book_by_genre_controller, get_book_by_genreid_controller, get_book_by_authorid_controller, delete_book_by_id_controller, update_book_by_id_controller, create_book_controller

book_bp = Blueprint('book', __name__)

def init_app(app):
    @app.route('/api/books', methods=['GET'])
    def get_books():
        mysql = app.config['mysql']  # Access mysql from the app's configuration
        return get_all_books_controller(mysql)
    @app.route('/api/books/<int:id>', methods=['GET'])
    def get_book_by_id(id):
        mysql = app.config['mysql']  # Access mysql from the app's configuration
        return get_book_by_id_controller(mysql,id)
    @app.route('/api/books/<name>', methods=['GET'])
    def get_book_by_name(name):
        mysql = app.config['mysql']  # Access mysql from the app's configuration
        return get_book_by_name_controller(mysql,name)
    @app.route('/api/books/genre/<genre>', methods=['GET'])
    def get_book_by_genre(genre):
        mysql = app.config['mysql']  # Access mysql from the app's configuration
        return get_book_by_genre_controller(mysql,genre)
    @app.route('/api/books/genreid/<genreid>', methods=['GET'])
    def get_book_by_genreid(genreid):
        mysql = app.config['mysql']  # Access mysql from the app's configuration
        return get_book_by_genreid_controller(mysql,genreid)
    @app.route('/api/books/authorid/<authorid>', methods=['GET'])
    def get_book_by_authorid(authorid):
        mysql = app.config['mysql']  # Access mysql from the app's configuration
        return get_book_by_authorid_controller(mysql,authorid)
    @app.route('/api/books/<bookid>', methods=['DELETE'])
    def delete_book_by_id(bookid):
        mysql = app.config['mysql']  # Access mysql from the app's configuration
        return delete_book_by_id_controller(mysql,bookid)
    @app.route('/api/books/<bookid>', methods=['PUT'])
    def update_book_by_id(bookid):
        mysql = app.config['mysql']  # Access mysql from the app's configuration
        name = request.json['name']
        description = request.json['description']
        rating = request.json['rating']
        progress = request.json['progress']
        published_year = request.json['published_year']
        image = request.json['image']
        language = request.json['language']
        book_type = request.json['book_type']
        src_audio = request.json['src_audio']
        return update_book_by_id_controller(mysql,bookid, name, description, rating, progress, published_year, image, language, book_type, src_audio)
    @app.route('/api/books', methods=['POST'])
    def create_book():
        mysql = app.config['mysql']  # Access mysql from the app's configuration
        name = request.json['name']
        description = request.json['description']
        rating = request.json['rating']
        progress = request.json['progress']
        published_year = request.json['published_year']
        image = request.json['image']
        language = request.json['language']
        book_type = request.json['book_type']
        src_audio = request.json['src_audio']
        authorid = request.json['authorid']
        genreid = request.json['genreid']
        return create_book_controller(mysql,name, description, rating, progress, published_year, image, language, book_type, src_audio, authorid, genreid)