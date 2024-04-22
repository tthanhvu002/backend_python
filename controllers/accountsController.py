from models.accounts import find_account_by_email, get_account_by_id,update_account_by_id, delete_account_by_id,get_accounts

def find_account_by_email_controller(mysql,email):
    return find_account_by_email(mysql,email)
def find_account_by_id_controller(mysql,id):    
    return get_account_by_id(mysql,id)
def update_account_controller(mysql,id, email, password):
    return update_account_by_id(mysql,id, email, password)
def delete_account_controller(mysql,id):
    return delete_account_by_id(mysql,id)
def get_accounts_controller(mysql):
    return get_accounts(mysql)