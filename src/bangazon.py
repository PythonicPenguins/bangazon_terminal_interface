import sys
import sqlite3
import os
sys.path.append('src')
from CustomerManager import *
from ProductManager import *

class Bangazon():

    def build_menu(self):
        active_customer = get_active_customer()
        print("")

        if active_customer == None:
            print("Active Customer: None")

        else:
            print("Active Customer: {} {}".format(active_customer[1], active_customer[2]))
        print("")
        print("*********************************************************")
        print("**  Welcome to Bangazon! Command Line Ordering System  **")
        print("*********************************************************")
        print("1. Create a customer account")
        print("2. Choose active customer")
        print("3. Create a payment option")
        print("4. Add product to shopping cart")
        print("5. Complete an order")
        print("6. See product popularity")
        print("7. Leave Bangazon!")


    def main_menu(self):
        self.build_menu()
        choice = input("> ")

        if choice == "1":
            first_name = input("First Name: ")
            last_name = input("Last Name: ")
            address = input("Full Address: ")
            phone_number = input("Phone Number: ")

            create_customer(first_name, last_name, address, phone_number)

            os.system('cls' if os.name is 'nt' else 'clear')

        if choice == "2":
            display_customers()
            os.system('cls' if os.name is 'nt' else 'clear')
            self.main_menu()

        if choice == "3":
            if get_active_customer() == None:
                print("")
                print("YOU MUST CHOOSE AN ACTIVE CUSTOMER FIRST!")
                print("")
                self.main_menu()
            else:
                payment_type = input("What is the payment type?: ")
                account_number = input("Account Number: ")
                create_payment_option(payment_type, account_number)
                os.system('cls' if os.name is 'nt' else 'clear')

        if choice == "4":
            if get_active_customer() == None:
                print("")
                print("YOU MUST CHOOSE AN ACTIVE CUSTOMER FIRST!")
                print("")
                self.main_menu()
            else:
                get_all_products()
                os.system('cls' if os.name is 'nt' else 'clear')

        if choice == "5":
            if get_active_customer() == None:
                print("")
                print("YOU MUST CHOOSE AN ACTIVE CUSTOMER FIRST!")
                print("")
                os.system('cls' if os.name is 'nt' else 'clear')
                self.main_menu()
            else:
                close_order()
                os.system('cls' if os.name is 'nt' else 'clear')


        if choice != "7":
            self.main_menu()


if __name__ == "__main__":
    user = Bangazon()
    user.main_menu()
