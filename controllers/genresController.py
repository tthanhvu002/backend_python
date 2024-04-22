from models.genres import get_all_genre, get_genre_by_id, get_genre_by_name, delete_genre_by_id, update_genre_by_id, create_genre

def get_all_genre_controller(mysql):
    return get_all_genre(mysql)
def get_genre_by_id_controller(mysql,id):
    return get_genre_by_id(mysql,id)
def get_genre_by_name_controller(mysql,name):
    return get_genre_by_name(mysql,name)
def delete_genre_by_id_controller(mysql,id):
    return delete_genre_by_id(mysql,id)
def update_genre_by_id_controller(mysql,id, name,icon):
    return update_genre_by_id(mysql,id, name,icon)
def create_genre_controller(mysql, name,icon):
    return create_genre(mysql, name,icon)
# Path: backend_python/views/genreRoutes.py