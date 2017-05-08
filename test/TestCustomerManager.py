import unittest
import sys;sys.path.append('../src')
from CustomerManager import *

class TestCustomerManager(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.customer = {"first_name": "Meg", "last_name": "Ducharme", "address": "500 Interstate Blvd S", "phone_number": "4104561238"}



    def test_customer_is_saved_to_database(self):

        create_customer(self.customer.first_name, self.customer.last_name, self.customer.address, self.customer.phone_number)

        customer_id = get_customer_id(self.customer.first_name, self.customer.last_name, self.customer.address, self.customer.phone_number)

        self.assertIsNotNone(customer_id)


    def test_get_all_customers(self):

        create_customer(self.customer.first_name, self.customer.last_name, self.customer.address, self.customer.phone_number)

        all_customers = get_all_customers()

        self.assertTrue(len(all_customers) > 0)


    def test_choose_active_customer(self):

        create_customer(self.customer.first_name, self.customer.last_name, self.customer.address, self.customer.phone_number)

        all_customers = get_all_customers()

        self.assertTrue(len(all_customers) > 0)

        activate_customer("1")

        self.assertIsNotNone(active_customer)


    def test_add_payment_option(self):

        create_payment_option("Visa", "123456789")

        payment_id = get_payment_option("Visa", "123456789")

        self.assertNotNone(payment_id)


