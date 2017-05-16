import sys
import sqlite3


def tear_down_db_data(first_name, last_name, address, phone_number):
    with sqlite3.connect('../bangazon.db') as conn:
        c = conn.cursor()

        try:
            c.execute("delete from customer where first_name=? and last_name=? and address=? and phone_number=?",(first_name, last_name, address, phone_number))

        except sqlite3.OperationalError as error:
            print(error)
