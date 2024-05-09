from flask import current_app as app
from flask import jsonify


def get_all_subscription_history(mysql):
    with app.app_context():
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM subscription_history")
        data = cursor.fetchall()
        return jsonify(data)


def get_subscription_history_by_id(mysql, id):
    with app.app_context():
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM subscription_history WHERE id = %s", (id,))
        data = cursor.fetchone()
        return jsonify(data)

def get_subscription_history_by_start(mysql, start):
    with app.app_context():
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM subscription_history WHERE start = %s", (start,))
        data = cursor.fetchone()
        return jsonify(data)
def get_subscription_history_by_end(mysql,end):
    with app.app_context():
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM subscription_history WHERE end = %s", (end,))
        data = cursor.fetchone()
        return jsonify(data)
def get_subscription_history_by_price(mysql, price):
    with app.app_context():
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM subscription_history WHERE price = %s", (price,))
        data = cursor.fetchone()
        return jsonify(data)
def delete_subscription_history_by_id(mysql, id):
    with app.app_context():
        cursor = mysql.connection.cursor()
        cursor.execute("DELETE FROM subscription_history WHERE id = %s", (id,))
        mysql.connection.commit()
        return jsonify({"message": "Xóa thành công"})
    
