from models.subscription import get_all_subscription, get_subscription_by_id, get_subscription_by_book_type, get_subscription_by_price, create_subscription, delete_subscription_by_id

def get_all_subscription_controller(mysql):
    return get_all_subscription(mysql)
def get_subscription_by_id_controller(mysql,id):
    return get_subscription_by_id(mysql,id)
def get_subscription_by_book_type_controller(mysql,book_type):
    return get_subscription_by_book_type(mysql,book_type)
def get_subscription_by_price_controller(mysql,price):
    return get_subscription_by_price(mysql,price)
def create_subscription_controller(mysql, duration, price_per_month, type, limit_book_mark, book_type, subscription_history_id):
    return create_subscription(duration, price_per_month, type, limit_book_mark, book_type, subscription_history_id)
def delete_subscription_by_id_controller(mysql,id):
    return delete_subscription_by_id(mysql,id)