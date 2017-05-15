import sys
import sqlite3
from CustomerManager import *


def get_all_products():
    with sqlite3.connect('bangazon.db') as conn:
        c = conn.cursor()

        try:
            c.execute("select name from product")
            all_customers = c.fetchall()
            for index, row in enumerate(all_customers):
                print("{} {}".format(index+1, row[0]))
            product_to_add = input("Product to add to cart: ")
            add_product_to_order(int(product_to_add))

        except sqlite3.OperationalError as error:
            print(error)


def create_product(product_name):
    with sqlite3.connect('bangazon.db') as conn:
        c = conn.cursor()

        try:
            c.execute("insert into Product values (?, ?, ?)", (None, name, price))
            conn.commit()

        except sqlite3.OperationalError as error:
            print(error)


def add_product_to_order(product_id):
    active_customer = get_active_customer()
    order_id = get_active_order_id(active_customer[0])
    print("order id add prod to order ", order_id)
    print("active customer add prod", active_customer[0])
    print("product id to add", product_id)

    if order_id == None:
        with sqlite3.connect('bangazon.db') as conn:
            c = conn.cursor()

            try:
                c.execute("insert into `Order` values (?, ?, ?)", (None, active_customer[0], None))
                conn.commit()


                order_id = get_active_order_id(active_customer[0])

                print(order_id, product_id)

                c.execute("insert into OrderProduct values (?, ?, ?)", (None, order_id[0], product_id))
                conn.commit()

            except sqlite3.OperationalError as error:
                print(error)

    else:
        with sqlite3.connect('bangazon.db') as conn:
            c = conn.cursor()

            try:
                c.execute("insert into OrderProduct values (?, ?, ?)", (None, order_id[0], product_id))
                conn.commit()

            except sqlite3.OperationalError as error:
                print(error)


def get_active_order_id(active_customer):
    print("active customer order id", active_customer)
    with sqlite3.connect('bangazon.db') as conn:
        c = conn.cursor()

        try:
            print(type(active_customer))
            c.execute("select order_id from `order` where customer_id=? and payment_option_id is ?", (active_customer, None))
            order_id = c.fetchone()
            print("oder id get active order", order_id)
            return order_id
        except sqlite3.OperationalError as error:
            print(error)


def close_order():
    active_customer = get_active_customer()
    print("active customer close order", active_customer)
    active_order_id = get_active_order_id(active_customer[0])

    payment_option_id = set_payment_option()

    with sqlite3.connect('bangazon.db') as conn:
            c = conn.cursor()

            try:
                c.execute("update OrderProduct set payment_option_id=? where order_id=? and customer_id=?)", (payment_option_id, order_id[0], active_customer[0]))
                conn.commit()

            except sqlite3.OperationalError as error:
                print(error)



