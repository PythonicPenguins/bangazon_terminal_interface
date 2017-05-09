import sys
import sqlite3
sys.path.append('src')
from CustomerManager import *
from ProductManager import *

class Bangazon():

    def build_menu(self):
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
            first_name = input("First Name ")

if __name__ == "__main__":
    user = Bangazon()
    user.main_menu()
