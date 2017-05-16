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

    if order_id == None:
        with sqlite3.connect('bangazon.db') as conn:
            c = conn.cursor()

            try:
                c.execute("insert into `Order` values (?, ?, ?)", (None, active_customer[0], None))
                conn.commit()


                order_id = get_active_order_id(active_customer[0])

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
    try:
        with sqlite3.connect('bangazon.db') as conn:
            c = conn.cursor()

            try:
                c.execute("select order_id from `order` where customer_id=? and payment_option_id is ?", (active_customer, None))
                order_id = c.fetchone()
                print("order id get active order", order_id)
                return order_id
            except sqlite3.OperationalError as error:
                print(error)
    except:
        return None


def close_order():
    active_customer = get_active_customer()
    order_id = get_active_order_id(active_customer[0])

    if order_id == None:
        print("")
        print("")
        print("******** You must add products to your cart first! ********")
        return

    else:
        total_price = get_total_price()

        print("Your order total is ${:.2f} Are you ready to purchase?".format(total_price[0]))

        user_input = input("(Y/N) > ")

        if user_input == "Y":

            payment_option_id = set_payment_option()

            with sqlite3.connect('bangazon.db') as conn:
                c = conn.cursor()

                try:
                    c.execute("update `Order` set payment_option_id={} where order_id={} and customer_id={}".format(payment_option_id, order_id[0], active_customer[0]))
                    conn.commit()

                except sqlite3.OperationalError as error:
                    print(error)

        else:
            return

def get_total_price():
    active_customer = get_active_customer()
    order_id = get_active_order_id(active_customer[0])

    with sqlite3.connect('bangazon.db') as conn:
        c = conn.cursor()

        try:
            query = "select sum(product.price) from `order` o join orderproduct op on op.order_id=o.order_id join product on op.product_id=product.product_id where o.order_id = {}".format(order_id[0])
            c.execute(query)
            total_cost = c.fetchone()
            return total_cost

        except sqlite3.OperationalError as error:
            print(error)

