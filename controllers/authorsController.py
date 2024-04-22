from models.authors import get_authors, get_author_by_id, get_author_by_bookID, get_author_by_name, create_author, delete_author_by_id, update_author_by_id

def get_authors_controller(mysql):
    return get_authors(mysql)
def get_author_by_id_controller(mysql,id):
    return get_author_by_id(mysql,id)
def get_author_by_bookID_controller(mysql,bookID):
    return get_author_by_bookID(mysql,bookID)
def get_author_by_name_controller(mysql,name):
    return get_author_by_name(mysql,name)
def create_author_controller(mysql,name, description, image):
    return create_author(mysql,name, description, image)
def delete_author_by_id_controller(mysql,id):
    return delete_author_by_id(mysql,id)
def update_author_by_id_controller(mysql,id, name, description, image):
    return update_author_by_id(mysql,id, name, description, image)