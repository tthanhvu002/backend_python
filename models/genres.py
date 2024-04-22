from flask import current_app as app
from flask import jsonify
def get_all_genre(mysql):
    with app.app_context():
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM genre")
        data = cursor.fetchall()
        return jsonify(data)
    
def get_genre_by_id(mysql,id):
    with app.app_context():
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM genre WHERE id = %s", (id,))
        data = cursor.fetchone()
        return jsonify(data)
def get_genre_by_name(mysql,name):
    with app.app_context():
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM genre WHERE name = %s", (name,))
        data = cursor.fetchone()
        return jsonify(data)
def delete_genre_by_id(mysql,id):
    query = "DELETE FROM genre WHERE id = %s"
    params = (id,)
    cursor = mysql.connection.cursor()
    cursor.execute(query, params)
    mysql.connection.commit()
    return jsonify("Genre deleted successfully")
def update_genre_by_id(mysql,id, name,icon):
    query = """
    UPDATE genre
    SET name = %s, icon = %s
    WHERE id = %s
    """
    params = (name,icon,id)
    cursor = mysql.connection.cursor()
    cursor.execute(query, params)
    mysql.connection.commit()
    return jsonify("Genre updated successfully")
def create_genre(mysql, name,icon):
    query = "INSERT INTO genre (name, icon) VALUES (%s, %s)"
    params = (name,icon)
    cursor = mysql.connection.cursor()
    cursor.execute(query, params)
    mysql.connection.commit()
    return jsonify("Genre created successfully")
