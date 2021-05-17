import users
from users import User
from users import Customer
from users import Admin
import products
from products import Product
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s: %(name)s: %(levelname)s: %(message)s ')

file_handler = logging.FileHandler('Market.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

"""home menu"""
print("\n", "Welcome to Market!".center(170))
menu_option = None
while menu_option != 0:
    try:
        menu_option = int(input("\n0.Exit\n1.login\n2.sing in\n"))
        assert menu_option in range(0, 3)
    except (AssertionError, ValueError):
        print("invalid input. please try again.")

    """login"""
    """variable user_menu will lead each user to it's menu"""
    if menu_option == 1:
        user_menu = 0

        """check useranme"""
        username = input("please enter your username: ")
        user = User.check_username(username)

        """check if user is admin or customer"""
        if user is not None:
            if user.role_type == "customer":
                user.check_block()
                user_menu = "customer"
                logger.info(f"customer {user.username} login")

            """if user is admin we should check password too"""
            if user.role_type == "admin":
                password = input("please enter your password: ")
                hash_password = User.hash_password(password)
                if str(user.password) == str(hash_password):
                    user_menu = "admin"
                    logger.info(f"admin {user.username} login")
                else:
                    print("your password is not correct")
                    logger.error(f"admin {user.username} entered password wrong")

        try:
            assert user_menu != 0
            print(f"welcome {username}! you have entered as {user.whoami()}")
        except (AttributeError, NameError, AssertionError):
            print("wrong info! please try again\n")
            logger.error(f"user entered username wrong.")

        """customer menu"""
        if user_menu == "customer":
            print("\n", "Welcome to Customer Menu!".center(170))
            customer_option = None
            bill_update = False

            while customer_option != 0:

                try:
                    customer_option = int(input(
                        "\n0.log out\n1.see products list\n2.shopping\n3.your bill\n4,delete account:"))
                    assert customer_option in range(0, 5)
                except(AssertionError, ValueError):
                    print("invalid input! please try again")

                """see products"""
                if customer_option == 1:
                    for name_product in products.lst_products:
                        print('\n', name_product)
                        logger.info(f"customer {user.username} saw products list")

                """shopping and enter password"""
                if customer_option == 2:
                    print("\nfor shopping you should enter your password")

                    """customer password"""
                    user.password_check_counter(user)
                    logger.info(f"customer {user.username} entered completely.")

                    "start to write a new bill for customer"
                    with open("customer_bill.txt", 'w') as bill:
                        bill.write(user.username)
                        bill.write('\n')

                    """get products infos to add to cart"""
                    name_product = None
                    total_price = 0

                    while name_product != "0":
                        print("\nwhen ever you finish shopping, you can enter 0 to quit or 1 to finish shopping")
                        name_product = input("please enter product name: ").strip()

                        """1 for finish shopping"""
                        if name_product == "1":
                            Product.rewrite_products()
                            bill_update = True

                            """add customer bill to total bill"""
                            with open("bills.txt", 'a') as total_bill, open("customer_bill.txt", 'r') as customer_bill:
                                for row in customer_bill:
                                    total_bill.write(row)

                            print("end of shopping.")
                            logger.info(f"customer {user.username} shopped.")
                            break

                        else:
                            """add product to cart"""
                            try:
                                product = Product.find_product(name_product)
                                assert product is not None
                            except AssertionError:
                                print("there is no such good. please try again")

                            product_number = int(input("please enter number of products: "))

                            "adding price of one product to total price"
                            price = Customer.shopping(product, product_number)
                            if price is not None:
                                total_price += price

                """show customer bill"""
                if customer_option == 3:
                    if bill_update is True:
                        with open('customer_bill.txt') as bill:
                            print(bill.read())

                        logger.info(f"customer {user.username} saw her/his bills.")
                        print(f"total price: {total_price}")

                        """if customer didn't shop this will handle it"""
                    else:
                        print("for see your bill you should shop first!")

            """delete customer account"""
            if customer_option == 4:
                logger.info(f"{user.username} delete account")
                User.delete_account(user)
                print("your account has been deleted! good bye!")
                customer_option = 0

            """log out"""
            if customer_option == 0:
                logger.info(f"log out {user.username}")

        """open admin menu"""
        if user_menu == "admin":
            print("\n", "Welcome to Admin Menu!".center(170))
            Admin.warning_empty_inventory()
            admin_option = None

            while admin_option != 0:

                try:
                    admin_option = int(input("\n0.log out\n1.add product\n2.update inventory"
                                             "\n3.unblock a customer\n4.see bills\n5.delete account:"))
                    assert admin_option in range(0, 6)
                except (AssertionError, ValueError):
                    print("invalid input! please try again")

                """add product"""
                if admin_option == 1:
                    str_product = input("\nplease enter product infos:\nname, brand, price, inventory, barcode: ")
                    product_name = Product.add_product(str_product)
                    Product.rewrite_products()
                    print(f"{product_name} added")
                    logger.info(f"product {product_name} added")

                """update inventory"""
                if admin_option == 2:
                    name_product = input("please enter name of product: ")
                    add_inventory = int(input(f"enter the number of {name_product} that you want to add:  "))

                    product = Product.find_product(name_product)
                    product.inventory += add_inventory
                    Product.update_inventory(product.inventory, product)
                    Product.rewrite_products()

                    print(f"inventory of {name_product} updated")
                    logger.info(f"{name_product} inventory updated")

                """unblock a customer"""
                if admin_option == 3:
                    customer_name = input("please enter customer name: ")
                    Admin.unblock_customer(customer_name)
                    User.rewrite()
                    print(f"{customer_name} unblocked")
                    logger.info(f"customer {customer_name} unblocked")

                """see bills"""
                if admin_option == 4:
                    Admin.print_bills()
                    logger.info(f"admin saw bills")

                """delete admin account"""
                if admin_option == 5:
                    User.delete_account(user)
                    print('\n', "account deleted. goodbye buddy :(".center(170))
                    admin_option = 0
                    logger.info("admin delete account")

                """log out"""
                if admin_option == 0:
                    logger.info(f"log out {user.username}")

    """register menu"""
    if menu_option == 2:

        while True:
            username = input("please enter a unique username: ")
            user = User.check_username(username)

            """check if username exists or not"""
            if user is not None:
                print("This username exists. please try again\n")
                logger.info("sing in unsuccessful")
            else:
                break

        password = input("please enter a password: ")
        hash_password = User.hash_password(password)

        """ask user if want to sing in as user or customer"""
        role = 0
        while role not in [1, 2]:
            try:
                role = int(input("do you want to sing as 1.customer, 2.admin: "))
                assert role in [1, 2]
            except (AssertionError, ValueError):
                print("invalid input! please try again")

        """add customer"""
        if role == 1:
            customer = Customer(username, hash_password)
            row_customer = [[customer.username, customer.password, customer.role_type, customer.flag]]
            User.save_user(customer, row_customer)
            print(f"Welcome {username}, you are a customer")
            logger.info(f"{username} sing in as a customer")

        """add admin"""
        if role == 2:
            admin_existence = Admin.admin_finder(users.lst_users)
            if admin_existence is True:
                print("sorry we already have an admin")
                logger.info(f"{username} tried to sing in as an admin. but we already had one!")
            else:
                admin = Admin(username, hash_password)
                row_admin = [[admin.username, admin.password, admin.role_type]]
                User.save_user(admin, row_admin)
                print(f"Welcome {username} you are an admin.")
                logger.info(f"admin {username} added")
