from models.books import find_all_books, find_book_by_id, find_book_by_name, find_book_by_genre, find_book_by_genreid, find_book_by_authorid, delete_book_by_id, update_book_by_id, create_book

def get_all_books_controller(mysql):
    return find_all_books(mysql)
def get_book_by_id_controller(mysql,id):
    return find_book_by_id(mysql,id)
def get_book_by_name_controller(mysql,name):
    return find_book_by_name(mysql,name)
def get_book_by_genre_controller(mysql,genre):
    return find_book_by_genre(mysql,genre)
def get_book_by_genreid_controller(mysql,genreid):
    return find_book_by_genreid(mysql,genreid)
def get_book_by_authorid_controller(mysql,authorid):
    return find_book_by_authorid(mysql,authorid)
def delete_book_by_id_controller(mysql,id):
    return delete_book_by_id(mysql,id)
def update_book_by_id_controller(mysql,id, name, description,rating, progress, published_year, image, language, book_type, src_audio):
    return update_book_by_id(mysql,id, name, description,rating, progress, published_year, image, language, book_type, src_audio)
def create_book_controller(mysql, name, description,rating, progress, published_year, image, language, book_type, src_audio, authorid, genreid):
    return create_book(mysql, name, description,rating, progress, published_year, image, language, book_type, src_audio, authorid, genreid)
