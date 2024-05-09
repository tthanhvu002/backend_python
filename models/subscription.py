from flask import current_app as app
from flask import jsonify


def get_all_subscription(mysql):
    with app.app_context():
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM subscription")
        data = cursor.fetchall()
        return jsonify(data)


def get_subscription_by_id(mysql, id):
    with app.app_context():
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM subscription WHERE id = %s", (id,))
        data = cursor.fetchone()
        return jsonify(data)


def get_subscription_by_book_type(mysql, book_type):
    with app.app_context():
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM subscription WHERE book_type = %s", (book_type,))
        data = cursor.fetchone()
        return jsonify(data)


def get_subscription_by_price(mysql, price):
    with app.app_context():
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM subscription WHERE price = %s", (price,))
        data = cursor.fetchone()
        return jsonify(data)


def create_subscription(
    duration, price_per_month, type, limit_book_mark, book_type, subscription_history_id
):
    with app.app_context():
        cursor = mysql.connection.cursor()
        cursor.execute(
            "INSERT INTO subscription (duration, price_per_month, type, limit_book_mark, book_type, subscription_history_id) VALUES (%s, %s, %s, %s, %s, %s)",
            (
                duration,
                price_per_month,
                type,
                limit_book_mark,
                book_type,
                subscription_history_id,
            ),
        )
        mysql.connection.commit()
        return jsonify({"message": "Tạo thành công"})


def delete_subscription_by_id(mysql, id):
    with app.app_context():
        cursor = mysql.connection.cursor()
        cursor.execute("DELETE FROM subscription WHERE id = %s", (id,))
        mysql.connection.commit()
        return jsonify({"message": "Xóa thành công"})


def update_subscription_by_id(
    mysql,
    id,
    duration,
    price_per_month,
    type,
    limit_book_mark,
    book_type,
    subscription_history_id,
):
    with app.app_context():
        cursor = mysql.connection.cursor()
        cursor.execute(
            "UPDATE subscription SET duration = %s, price_per_month = %s, type = %s, limit_book_mark = %s, book_type = %s, subscription_history_id = %s WHERE id = %s",
            (
                duration,
                price_per_month,
                type,
                limit_book_mark,
                book_type,
                subscription_history_id,
                id,
            ),
        )
        mysql.connection.commit()
        return jsonify({"message": "Cập nhật thành công"})
