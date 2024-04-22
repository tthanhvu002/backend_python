from flask import current_app as app
from flask import jsonify

def get_all_users(mysql):
    with app.app_context():
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM users")
        data = cursor.fetchall()
        return jsonify(data)
def get_user_by_name(mysql,name):
    with app.app_context():
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM users WHERE name = %s", (name,))
        data = cursor.fetchone()
        return jsonify(data)
def get_user_by_id(mysql,id):   
    with app.app_context():
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM users WHERE id = %s", (id,))
        data = cursor.fetchone()
        return jsonify(data)
def update_user_by_id(mysql,id, name, email, phone,address):
    query = """
    UPDATE users
    SET name = ?, email = ?, phone = ?, address = ?
    WHERE id = ?
    """
    params = (name, email, phone, address, id)
    cursor = mysql.connection.cursor()
    cursor.execute(query, params)
    mysql.connection.commit()
    return jsonify("User updated successfully")
def delete_user_by_id(mysql,id):
    query = "DELETE FROM users WHERE id = %s"
    params = (id,)
    cursor = mysql.connection.cursor()
    cursor.execute(query, params)
    mysql.connection.commit()
    return jsonify("User deleted successfully")


   