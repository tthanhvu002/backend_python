from flask import current_app as app
from flask import jsonify

def get_accounts(mysql):
    with app.app_context():
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM accounts")
        data = cursor.fetchall()
        return jsonify(data)
def get_account_by_id(mysql,id):
    with app.app_context():
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM accounts WHERE id = %s", (id,))
        data = cursor.fetchone()
        return jsonify(data)
def delete_account_by_id(mysql,id):
    with app.app_context():
        cursor = mysql.connection.cursor()
        cursor.execute("DELETE FROM accounts WHERE id = %s", (id,))
        mysql.connection.commit()
        return jsonify({'message': 'Xóa thành công'})
def update_account_by_id(mysql,id, account):
    with app.app_context():
        cursor = mysql.connection.cursor()
        cursor.execute("UPDATE accounts SET username = %s, password = %s WHERE id = %s", (account['username'], account['password'], id))
        mysql.connection.commit()
        return jsonify({'message': 'Cập nhật thành công'})
def find_account_by_email(mysql,email):
    with app.app_context():
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM accounts WHERE email = %s", (email,))
        data = cursor.fetchone()
        return jsonify(data)