import sys
import sqlite3

active_customer = None

def get_active_customer():
    return active_customer

def create_customer(first_name, last_name, address, phone_number):
    with sqlite3.connect('../bangazon.db') as conn:
        c = conn.cursor()

        try:
            c.execute("insert into customer values (?, ?, ?, ?, ?)", (None, first_name, last_name, address, phone_number))
            conn.commit()
        except sqlite3.OperationalError as error:
            print(error)


def get_customer_id(first_name, last_name, address, phone_number):
    with sqlite3.connect('../bangazon.db') as conn:
        c = conn.cursor()

        try:
            c.execute("select customer_id from customer where first_name=? and last_name=? and address=? and phone_number=?",(first_name, last_name, address, phone_number))
            customer_id = c.fetchone()
            print("cutsomer_id", customer_id[0])
            return customer_id[0]
        except sqlite3.OperationalError as error:
            print(error)


def get_all_customers():
    with sqlite3.connect('../bangazon.db') as conn:
        c = conn.cursor()

        try:
            c.execute("select first_name, last_name from customer")
            all_customers = c.fetchall()
            print(all_customers)
            for index, row in enumerate(all_customers):
                print("{} {} {}".format(index+1, row[0], row[1]))
            return all_customers
        except sqlite3.OperationalError as error:
            print(error)


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

