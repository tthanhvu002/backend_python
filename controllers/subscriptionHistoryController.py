from models.subscription_history import get_all_subscription_history, get_subscription_history_by_id, get_subscription_history_by_start, get_subscription_history_by_end, get_subscription_history_by_price, delete_subscription_history_by_id

def get_all_subscription_history_controller(mysql):
    return get_all_subscription_history(mysql)
def get_subscription_history_by_id_controller(mysql,id):
    return get_subscription_history_by_id(mysql,id)
def get_subscription_history_by_start_controller(mysql,start):
    return get_subscription_history_by_start(mysql,start)
def get_subscription_history_by_end_controller(mysql,end):
    return get_subscription_history_by_end(mysql,end)
def get_subscription_history_by_price_controller(mysql,price):
    return get_subscription_history_by_price(mysql,price)
def delete_subscription_history_by_id_controller(mysql,id):
    return delete_subscription_history_by_id(mysql,id)
