from flask import current_app as app
from flask import jsonify
def get_authors(mysql):
    with app.app_context():
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM author")
        data = cursor.fetchall()
        return jsonify(data)
def get_author_by_id(mysql,id):
    with app.app_context():
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM author WHERE id = %s", (id,))
        data = cursor.fetchone()
        return jsonify(data)
def get_author_by_bookID(mysql,bookID):
    with app.app_context():
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT author.* FROM author INNER JOIN book ON author.id = book.author WHERE book.id = %s", (bookID,))
        data = cursor.fetchall()
        return jsonify(data)
def get_author_by_name(mysql,name):
    with app.app_context():
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM author WHERE name = %s", (name,))
        data = cursor.fetchone()
        return jsonify(data)   
def create_author(mysql,name, description, image):    
    query = """
    INSERT INTO authors (name, description, image)
    VALUES (?, ?, ?)
    """
    params = (name, description, image)
    result = execute_query(query, params)
    return result
def delete_author_by_id(mysql,id):
    query = "DELETE FROM authors WHERE id = ?"
    params = (id,)
    result = execute_query(query, params)
    return result
def update_author_by_id(mysql,id, name, description, image):
    query = """
    UPDATE authors
    SET name = ?, description = ?, image = ?
    WHERE id = ?
    """
    params = (name, description, image, id)
    result = execute_query(query, params)
    return result