active_customer = None

def get_active_customer():
    return active_customer

def create_customer(first_name, last_name, address, phone_number):
    pass


def get_customer_id(first_name, last_name, address, phone_number):
    return 1


def get_all_customers():
    return [(1, "Meg Ducharme")]


def activate_customer(customer_id):
    global active_customer
    active_customer = customer_id


def create_payment_option(name, account_number, active_customer):
    pass


def get_payment_option(name, account_number):
    return 1


def get_customer_payment_options(customer_id):
    return [("Visa", "123456789")]


def set_payment_option(payment_id):
    pass

