from flask import Blueprint, request, jsonify
from flask import current_app as app
from controllers.accountsController import get_accounts_controller, find_account_by_id_controller, delete_account_controller, update_account_controller, find_account_by_email_controller

account_bp = Blueprint('account', __name__) 
def init_app(app):
    @app.route('/api/accounts', methods=['GET'])
    def get_accounts():
        mysql = app.config['mysql']  # Access mysql from the app's configuration
        return get_accounts_controller(mysql)
    @app.route('/api/accounts/<id>', methods=['GET'])
    def get_account_by_id(id):
        mysql = app.config['mysql']  # Access mysql from the app's configuration
        return find_account_by_id_controller(id,mysql)
    @app.route('/api/accounts/<id>', methods=['DELETE'])
    def delete_account_by_id(id):
        mysql = app.config['mysql']  # Access mysql from the app's configuration
        return delete_account_controller(id,mysql)
    @app.route('/api/accounts/<id>', methods=['PUT'])
    def update_account_by_id(id):  
        mysql = app.config['mysql']  # Access mysql from the app's configuration
        email = request.json['email']
        password = request.json['password']
        return update_account_controller(id, email, password,mysql)
    @app.route('/api/accounts/<email>', methods=['GET'])
    def find_account_by_email(email):   
        mysql = app.config['mysql']  # Access mysql from the app's configuration
        return find_account_by_email_controller(mysql,email)

