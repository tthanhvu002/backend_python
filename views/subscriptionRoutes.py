from flask import Blueprint, request, jsonify
from flask import current_app as app
from controllers.subscriptionController import get_all_subscription_controller, get_subscription_by_id_controller, get_subscription_by_book_type_controller, get_subscription_by_price_controller, create_subscription_controller, delete_subscription_by_id_controller

subscription_bp = Blueprint('subscription', __name__)

def init_app(app):
    @app.route('/api/subscription', methods=['GET'])
    def get_subscription():
        mysql = app.config['mysql']  # Access mysql from the app's configuration
        return get_all_subscription_controller(mysql)
    @app.route('/api/subscription/<int:id>', methods=['GET'])
    def get_subscription_by_id(id):
        mysql = app.config['mysql']
        return get_subscription_by_id_controller(mysql,id)
    @app.route('/api/subscription/<book_type>', methods=['GET'])
    def get_subscription_by_book_type(book_type):
        mysql = app.config['mysql']
        return get_subscription_by_book_type_controller(mysql,book_type)
    @app.route('/api/subscription/<price>', methods=['GET'])
    def get_subscription_by_price(price):
        mysql = app.config['mysql']
        return get_subscription_by_price_controller(mysql,price)
    @app.route('/api/subscription', methods=['POST'])
    def create_subscription():
        mysql = app.config['mysql']
        duration = request.json['duration']
        price_per_month = request.json['price_per_month']
        type = request.json['type']
        limit_book_mark = request.json['limit_book_mark']
        book_type = request.json['book_type']
        subscription_history_id = request.json['subscription_history_id']
        return create_subscription_controller(mysql, duration, price_per_month, type, limit_book_mark, book_type, subscription_history_id)
    def delete_subscription_by_id(id):
        mysql = app.config['mysql']
        return delete_subscription_by_id_controller(mysql,id)
    def update_subscription_by_id(id):
        mysql = app.config['mysql']
        duration = request.json['duration']
        price_per_month = request.json['price_per_month']
        type = request.json['type']
        limit_book_mark = request.json['limit_book_mark']
        book_type = request.json['book_type']
        subscription_history_id = request.json['subscription_history_id']
        return update_subscription_by_id_controller(mysql,id, duration, price_per_month, type, limit_book_mark, book_type, subscription_history_id)