import unittest
import sys;sys.path.append('../src')
from CustomerManager import *
from ProductManager import *
from TestCustomerManager import *


sys.path.append('../src')
from ProductManager import *
from CustomerManager import *

    @classmethod
    def setUpClass(self):
        self.customer = {"first_name": "Meg", "last_name": "Ducharme", "address": "500 Interstate Blvd S", "phone_number": "4104561238"}

class TestProductManager(unittest.TestCase):
    def test_get_all_products(self):
        create_product("dog toy")

        all_products = get_all_products()
        self.assertTrue(len(all_products) > 0)

    def test_user_can_add_product_to_an_order(self):
        create_customer(self.customer["first_name"], self.customer["last_name"], self.customer["address"],
                        self.customer["phone_number"])
        all_customers = get_all_customers()
        self.assertTrue(len(all_customers) > 0)

        activate_customer(1)
        active_customer = get_active_customer()
        self.assertIsNotNone(active_customer)

        product_id = 1

        # check if there is an open order
        add_product_to_order(active_customer, product_id)

        # where payment_option = None
        active_order_id = get_active_order_id(active_customer)

    def test_user_can_complete_an_order(self):
        create_customer(self.customer["first_name"], self.customer["last_name"], self.customer["address"],
                        self.customer["phone_number"])
        all_customers = get_all_customers()
        self.assertTrue(len(all_customers) > 0)

        activate_customer(1)
        active_customer = get_active_customer()
        self.assertIsNotNone(active_customer)

        #function will get active order, and add payment type to it
        closed_order(1, 1)

        # function will get active order, and add payment type to it
        is_closed = closed_order(active_order_id, selected_payment_option)
        self.assertIsNotNone(is_closed[0][1])

