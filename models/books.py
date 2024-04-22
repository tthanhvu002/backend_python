from flask import current_app as app
from flask import jsonify

def find_all_books(mysql):
    with app.app_context():
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM book")
        data = cursor.fetchall()
        return jsonify(data)
def find_book_by_id(mysql,id):   
    with app.app_context():
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM book WHERE id = %s", (id,))
        data = cursor.fetchone()
        return jsonify(data)
def find_book_by_name(mysql,name):
    with app.app_context():
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM book WHERE name = %s", (name,))
        data = cursor.fetchone()
        return jsonify(data)
def find_book_by_genre(mysql,genre):
    with app.app_context():
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM book WHERE genre = %s", (genre,))
        data = cursor.fetchall()
        return jsonify(data)
def find_book_by_genreid(mysql,genreid):
    with app.app_context():
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM book WHERE genreid = %s", (genreid,))
        data = cursor.fetchall()
        return jsonify(data)
    
def find_book_by_authorid(mysql,authorid):
    with app.app_context():
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM book WHERE authorid = %s", (authorid,))
        data = cursor.fetchall()
        return jsonify(data)
def delete_book_by_id(mysql,id):
    query = "DELETE FROM book WHERE id = %s"
    params = (id,)
    cursor = mysql.connection.cursor()
    cursor.execute(query, params)
    mysql.connection.commit()
    return jsonify("Book deleted successfully")
def update_book_by_id(mysql,id, name, description,rating, progress, published_year, image, language, book_type, src_audio):
    query = """
    UPDATE book
    SET name = ?, description = ?, rating = ?, progress = ?, published_year = ?, image = ?, language = ?, book_type = ?, src_audio = ?
    WHERE id = ?
    """
    params = (name, description, rating, progress, published_year, image, language, book_type, src_audio, id)
    cursor = mysql.connection.cursor()
    cursor.execute(query, params)
    mysql.connection.commit()
    return jsonify("Book updated successfully")

def create_book(mysql, name, description,rating, progress, published_year, image, language, book_type, src_audio, authorid, genreid):
    query = """
    INSERT INTO book (name, description,rating, progress, published_year, image, language, book_type, src_audio, authorid, genreid)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """
    params = (name, description,rating, progress, published_year, image, language, book_type, src_audio, authorid, genreid)
    cursor = mysql.connection.cursor()
    cursor.execute(query, params)
    mysql.connection.commit()
    return jsonify("Book created successfully")
