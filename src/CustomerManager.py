import sys
import sqlite3


active_customer = None


def get_active_customer():
    return active_customer

def create_customer(first_name, last_name, address, phone_number):
    with sqlite3.connect('bangazon.db') as conn:
        c = conn.cursor()

        try:
            c.execute("insert into Customer values (?, ?, ?, ?, ?)", (None, first_name, last_name, address, phone_number))
            conn.commit()

        except sqlite3.OperationalError as error:
            print(error)


def get_customer_id(first_name, last_name, address, phone_number):
    with sqlite3.connect('bangazon.db') as conn:
        c = conn.cursor()

        try:
            c.execute("select customer_id from customer where first_name=? and last_name=? and address=? and phone_number=?",(first_name, last_name, address, phone_number))
            customer_id = c.fetchone()
            print("cutsomer_id", customer_id[0])
            return customer_id[0]

        except sqlite3.OperationalError as error:
            print(error)


def get_all_customers():
    with sqlite3.connect('bangazon.db') as conn:
        c = conn.cursor()

        try:
            c.execute("select first_name, last_name from customer")
            all_customers = c.fetchall()
            return all_customers

        except sqlite3.OperationalError as error:
            print(error)


def display_customers():
    all_customers = get_all_customers()

    for index, row in enumerate(all_customers):
        print("{}. {} {}".format(index+1, row[0], row[1]))

    user_input = input("Choose Active Customer: ")

    chosen_active_customer = all_customers[int(user_input) - 1]

    activate_customer(chosen_active_customer)
    print("active customer", active_customer)


def activate_customer(customer_tuple):
    global active_customer

    with sqlite3.connect('bangazon.db') as conn:
        c = conn.cursor()

        try:
            c.execute("select customer_id, first_name, last_name from customer where first_name=? and last_name=?",(customer_tuple[0], customer_tuple[1]))
            active_customer = c.fetchone()
            print("active customer", active_customer)
            return active_customer

        except sqlite3.OperationalError as error:
            print(error)


def create_payment_option(name, account_number):
    print("active cutsomer create payment", active_customer)
    with sqlite3.connect('bangazon.db') as conn:
        c = conn.cursor()

        try:
            c.execute("insert into PaymentOption values (?, ?, ?, ?)", (None, name, account_number, active_customer[0]))
            conn.commit()

        except sqlite3.OperationalError as error:
            print(error)


def get_payment_option(name, account_number):
    with sqlite3.connect('bangazon.db') as conn:
        c = conn.cursor()

        try:
            c.execute("select name, account_number from paymentoption")
            all_payment_options = c.fetchall()
            for index, row in enumerate(all_payment_options):
                print("{} {} {}".format(index+1, row[0], row[1]))
            return all_payment_options
        except sqlite3.OperationalError as error:
            print(error)


def get_customer_payment_options():
    print("active get cus payment", active_customer[0])
    with sqlite3.connect('bangazon.db') as conn:
        c = conn.cursor()

        try:
            c.execute("select name, account_number from paymentoption where customer_id={}".format(active_customer[0]))
            customer_payment_options = c.fetchall()
            return customer_payment_options
        except sqlite3.OperationalError as error:
            print(error)


def set_payment_option():
    payment_options = get_customer_payment_options()

    for index, row in enumerate(payment_options):
        print("{}. {} {}".format(index+1, row[0], row[1]))

    payment_option_id = input("Choose payment option: ")
    return payment_option_id


