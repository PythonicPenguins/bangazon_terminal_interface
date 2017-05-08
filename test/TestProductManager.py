import unittest
import sys;sys.path.append('../src')
from CustomerManager import *
from TestCustomerManager import *

class TestProductManager(unittest.TestCase):


    def test_get_all_products(self):
        create_product("dog toy")

        all_products = get_all_products()
        self.assertTrue(len(all_products) > 0)


    def test_customer_can_create_order(self):
        create_customer(self.customer["first_name"], self.customer["last_name"], self.customer["address"], self.customer["phone_number"])
        all_customers = get_all_customers()
        self.assertTrue(len(all_customers) > 0)

        activate_customer(1)
        self.assertIsNotNone(active_customer)

        product_id = 1

        create_new_order(active_customer, product_id)

        active_order = get_active_order_id(active_customer)
        #where payment_option = None

