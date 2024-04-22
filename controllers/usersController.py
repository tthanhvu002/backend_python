from models.users import get_all_users, get_user_by_id, get_user_by_name, update_user_by_id, delete_user_by_id

def get_all_users_controller(mysql):
    return get_all_users(mysql)
def get_user_by_id_controller(mysql,id):
    return get_user_by_id(mysql,id)
def get_user_by_name_controller(mysql,name):
    return get_user_by_name(mysql,name)
def update_user_by_id_controller(mysql,id, name, email, phone,address):
    return update_user_by_id(mysql,id, name, email, phone,address)
def delete_user_by_id_controller(mysql,id):
    return delete_user_by_id(mysql,id)