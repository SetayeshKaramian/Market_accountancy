import users
import goods

"""login"""
print("\n", "Welcome to Market!".center(170))
the_key = False
menu_login = None

while menu_login != 0:
    menu_login = int(input("0.quit, 1.log in, 2.sing in, 3.Admin menu, 4.customer menu: "))

    if menu_login == 1:
        username = input("Please enter your username: ")
        user = users.username_checker(username)
        "check if user is admin or customer. ask admin to enter password and show customer his/her choices."
        if user.role_type == "admin":
            the_key = users.password_checker(user)
        else:
            "options for customer user without entering password"
            customer_choice = None
            while customer_choice != 0:
                customer_choice = int(input("you have entered as a customer. 0.main menu, 1.see goods,"
                                            " 2.login to have full access to customer menu"))
                if customer_choice == 1:
                    goods.print_goods()
                elif customer_choice == 2:
                    the_key = users.password_checker(user)

    if menu_login == 2:
        users.add_user()
        print("user added")

        """Admin menu"""
    if menu_login == 3:
        try:
            assert the_key == "king key"
            print('\n\n', "Welcome to the administration of market!".center(170))
            "check for empty inventories"
            for i in goods.the_goods_lst:
                if i.inventory == 0:
                    print(f"{i.name} inventory is empty!")

            option = None
            while option != 0:
                option = int(input("\nPlease choose your command: 0.main menu, 1.add goods, 2.see bills: "))

                "get info for good and check for right info"
                if option == 1:
                    data = input("Please enter: name, brand, price, inventory, barcode: ")
                    if goods.check_numberof_orient_good(data) is True:
                        goods.add_good(data)
                        print("good has been added successfully")
                    else:
                        print("you didn't fill all the infos!\nPlease try again.")

                if option == 2:
                    goods.print_bills()

        except AssertionError:
            print("only Admin have access to this menu")

    """customer menu"""
    if menu_login == 4:
        try:
            assert the_key == True
            print("\n", "Welcome to the market!\n\n".center(170))
            option = None
            while option != 0:
                option = int(input("please choose your command: 0.main menu,"
                                   " 1.see the list of goods and add to cart: "))
                if option == 1:
                    goods.print_goods()
                    command = input("please choose your command: a.customer menu, b.shopping: ")

                    "shopping part"
                    if command == 'b':
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
                            price = goods.shopping(the_good)
                            if price is None:
                                total_price += price
                        """after finishing shopping add customer bill to total bill and save it,
                        show the customer the total price and also print customer bill"""
                        if the_good == 1:
                            goods.append_to_total_bills()
                            print(f"\ntotal price: {total_price}\n")
                            print("your bill:\n")
                            with open('customer_bill.txt') as bill:
                                print(bill.read())

        except AssertionError:
            print("You can enter this menu after log in as a customer")

"after all, rewrite the goods file to save changes in inventory or save new goods that admin adds"
if menu_login == 0:
    goods.rewrite_goods()
