import users
from users import Users
import goods
from goods import Goods
import administration
import customer

"""login"""
print("\n", "Welcome to Market!".center(170))
key = False
menu_option = None

while menu_option != 0:
    menu_option = int(input("0.quit, 1.log in, 2.sing in, 3.Admin menu, 4.customer menu: "))

    if menu_option == 1:
        "check if user exists"
        user = Users.check_username(users.lst_usernames)
        "check if user is ban or not"
        Users.check_block(user)
        "check if user is admin or costumer. if user was admin ask for password."
        if user.role_type == "admin":
            key = Users.password_checker(user, users.lst_users)
        else:
            print("\n\nWELCOME!\nyou have entered as a customer")
            key = "customer"

    if menu_option == 2:
        Users.register(users.lst_usernames)

        """Admin menu"""
    if menu_option == 3:
        try:
            assert key == "king key"
            print('\n\n', "Welcome to the administration of market!".center(170))
            "check for empty inventories"
            administration.warning_empty_inventory()

            option = None
            while option != 0:
                option = int(input("\nPlease choose your command: 0.main menu, 1.add goods, 2.see bills: "))

                "get info for good and check for right info"
                if option == 1:
                    administration.get_data_new_good()

                if option == 2:
                    administration.print_bills()

        except AssertionError:
            print("\nonly Admin have access to this menu\n")

    """customer menu"""
    if menu_option == 4:
        try:
            assert key == "customer"
            print("\n", "Welcome to customer menu!\n\n".center(170))
            option = None
            while option != 0:
                option = int(input("please choose your command: 0.main menu,"
                                   " 1.see the list of goods and add to cart: "))
                if option == 1:
                    Goods.print_goods()
                    command = input("please choose your command: a.customer menu, b.shopping: ")

                    "shopping part"
                    if command == 'b':
                        print("enter your password for access to shopping")
                        Users.password_checker(user, users.lst_users)
                        print("whenever you want, you can quit or go to finish"
                              " your shopping to see your bill and total price")
                        print("0.quit, 1.finish shopping\n")
                        the_good = None
                        total_price = 0

                        "start to write a new bill for customer"
                        with open("customer_bill.txt", 'w') as bill:
                            bill.write(user.username)
                            bill.write('\n')

                        while the_good != 0:
                            the_good = input("please enter name of good:").strip()
                            "check if customer want to finish her/his shopping"
                            if the_good.isdigit():
                                the_good = int(the_good)
                                break
                            "adding price of one ordered good to total price"
                            price = customer.shopping(the_good)
                            if price is None:
                                pass
                            else:
                                total_price += price

                        """after finishing shopping add customer bill to total bill and save it,
                        show the customer the total price and also print customer bill"""
                        if the_good == 1:
                            customer.append_to_total_bills()
                            print(f"\ntotal price: {total_price}\n")
                            print("your bill:\n")
                            with open('customer_bill.txt') as bill:
                                print(bill.read())

        except AssertionError:
            print("You can enter this menu after log in as a customer")

"after all, rewrite the goods file to save changes in inventory or save new goods that admin adds"
if menu_option == 0:
    goods.rewrite_goods()
