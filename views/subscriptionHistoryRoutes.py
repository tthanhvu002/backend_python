from flask import Blueprint, request, jsonify
from flask import current_app as app
from controllers.subscriptionHistoryController import (
    get_all_subscription_history_controller,
    get_subscription_history_by_id_controller,
    get_subscription_history_by_end_controller,
    get_subscription_history_by_start_controller,
    get_subscription_history_by_price_controller,
    delete_subscription_history_by_id_controller,
)

subscription_history_bp = Blueprint("subscription_history", __name__)


def init_app(app):
    @app.route("/api/subscription_history", methods=["GET"])
    def get_subscription_history():
        mysql = app.config["mysql"]  # Access mysql from the app's configuration
        return get_all_subscription_history_controller(mysql)

    @app.route("/api/subscription_history/<int:id>", methods=["GET"])
    def get_subscription_history_by_id(id):
        mysql = app.config["mysql"]
        return get_subscription_history_by_id_controller(mysql, id)

 
    @app.route("/api/subscription_history/<start>", methods=["GET"])
    def get_subscription_history_by_start(start):
        mysql = app.config["mysql"]
        return get_subscription_history_by_start_controller(mysql, start)
    @app.route("/api/subscription_history/<end>", methods=["GET"])
    def get_subscription_history_by_end(end):
        mysql = app.config["mysql"]
        return get_subscription_history_by_end_controller(mysql, end)
    @app.route("/api/subscription_history/<price>", methods=["GET"])
    def get_subscription_history_by_price(price):
        mysql = app.config["mysql"]
        return get_subscription_history_by_price_controller(mysql, price)
    @app.route("/api/subscription_history", methods=["DELETE"])
    def delete_subscription_history_by_id():
        mysql = app.config["mysql"]
        id = request.json["id"]
        return delete_subscription_history_by_id_controller(mysql, id)
