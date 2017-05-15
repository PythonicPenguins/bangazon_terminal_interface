import sys
import sqlite3


active_customer = None


def get_active_customer():
    return active_customer

def create_customer(first_name, last_name, address, phone_number):
    with sqlite3.connect('../bangazon.db') as conn:
        c = conn.cursor()

        try:
            c.execute("insert into Customer values (?, ?, ?, ?, ?)", (None, first_name, last_name, address, phone_number))
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
            display_customers(all_customers)

        except sqlite3.OperationalError as error:
            print(error)


def display_customers(all_customers):
    for index, row in enumerate(all_customers):
        print("{} {} {}".format(index+1, row[0], row[1]))

    chosen_active_customer = input("Choose Active Customer: ")
    activate_customer(chosen_active_customer)
    print(active_customer)


def activate_customer(customer_id):
    global active_customer

    with sqlite3.connect('../bangazon.db') as conn:
        c = conn.cursor()

        try:
            c.execute("select customer_id, first_name, last_name from customer where customer_id=?",(customer_id))
            active_customer = c.fetchone()
            print(activate_customer)
            return active_customer

        except sqlite3.OperationalError as error:
            print(error)


def create_payment_option(name, account_number):
    with sqlite3.connect('../bangazon.db') as conn:
        c = conn.cursor()

        try:
            c.execute("insert into PaymentOption values (?, ?, ?, ?)", (None, name, account_number, active_customer))
            conn.commit()

        except sqlite3.OperationalError as error:
            print(error)


def get_payment_option(name, account_number):
    with sqlite3.connect('../bangazon.db') as conn:
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
    with sqlite3.connect('../bangazon.db') as conn:
        c = conn.cursor()

        try:
            c.execute("select name, account_number from paymentoption where customer_id=?", (activate_customer))
            customer_payment_options = c.fetchall()
            return customer_payment_options
        except sqlite3.OperationalError as error:
            print(error)


def set_payment_option():
    payment_options = get_customer_payment_options()

    for index, row in enumerate(payment_options):
        print("{} {} {}".format(index+1, row[0], row[1]))

    payment_option_id = input("Choose payment option: ")

    return payment_option_id



