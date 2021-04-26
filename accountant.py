import csv


class Goods:
    def __init__(self, name, brand, price, inventory, barcode):
        self.name = name
        self.brand = brand
        self.price = price
        self.inventory = inventory
        self.barcode = barcode

    def __str__(self):
        return f"name: {self.name}\nbrand: {self.brand}\nprice: {self.price}"

    def inventory_updater(self):
        """ update the inventory based on customers' purchases"""


class Users:
    def __init__(self, username, password, lock=False):
        self.username = username
        self.password = password
        self.__lock = lock

    def __str__(self):
        return f"Welcome{self.username}"

    @property
    def user_blocker(self):
        self.__lock = True
        return self.__lock


def check_username_pass():
    a_key = False
    username = input("Username: ")
    password = input("Password: ")
    with open('users.txt') as csv_users:
        users_reader = csv.reader(csv_users, delimiter=',')
        for row in users_reader:
            if username == row[0] and password == row[1]:
                print(f"Hi {username}!")
                a_key = True
                break
    if a_key == True and username == "Admin":
        a_key = "king key"
    return a_key


def add_user():
    duplication = False
    username = input("Please enter a unique username: ")
    with open('users.txt') as csv_users:
        users_reader = csv.reader(csv_users, delimiter=',')
        for row in users_reader:
            if row[0] == username:
                duplication = True

    try:
        assert duplication is False
        password = input("Please enter a password: ")
        lst_user = [username, password]
        user = (','.join(lst_user))
        with open('users.txt', 'a') as csv_users:
            csv_users.write(user)
            csv_users.write("\n")

    except AssertionError:
        print("This username already exists. try another one.")


def shopping():
    cart = None
    counter = 1
    print("please choose your goods and number you needed in this format: good,number, if you want to quiet press 0:")
    while cart != 0:
        cart = input(f"good{counter}:")
        counter += 1
        "append to the"


the_goods_lst = []
with open('goods.txt') as csv_goods:
    goods_reader = csv.reader(csv_goods, delimiter=',')
    for row in goods_reader:
        the_goods_lst.append(Goods(row[0], row[1], row[2], row[3], row[4]))

"""login"""
print("\n", "Welcome to Market!".center(170))
key = False
menu_login = None

while menu_login != 0:
    menu_login = int(input("0.quite, 1.log in, 2.sing in, 3.Admin menu, 4.customer menu: "))

    if menu_login == 1:
        count = 1
        while key is False and count != 3:
            the_key = check_username_pass()
            if the_key is False:
                print(f"Sorry, that username or password isn't right. you can only try{3 - count} more times ")
                count += 1
        if key == False:
            pass

    if menu_login == 2:
        add_user()
        print("user added")
    if menu_login == 3:
        try:
            assert the_key == "king key"
            """Admin menu"""
            print('\n\n', "Welcome to the administration of market!".center(170))
            for i in the_goods_lst:
                if i.inventory == 0:
                    print(f"{i.name} inventory is empty!")
            option = None
            while option != 0:
                option = int(input("\nPlease choose your command: 0.quite, 1.add goods, 2.see bills: "))
                if option == 1:
                    data = input("Please enter: name, brand, price, inventory, barcode: ")
                    with open('goods.txt', 'a') as csv_goods:
                        csv_goods.write(data)
                        csv_goods.write("\n")

                if option == 2:
                    print("this will print bills.")

        except AssertionError:
            print("only Admin have access to this menu")

    if menu_login == 4:
        try:
            assert key == True
            """customer menu"""
            print("\n", "Welcome to the market!\n\n".center(170))
            option = None
            while option != 0:
                option = input("please choose your command: 0.quite, 1.see the list of goods and add to cart: ")
                if option == 1:
                    "print goods list"
                    "print:please choose your command: a.main menu, b.shopping"


        except AssertionError:
            print("You can enter this menu after log in")
