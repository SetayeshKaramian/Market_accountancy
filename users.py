import logging
import csv
import binascii
import hashlib
import products

"""set logger"""
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s: %(name)s: %(levelname)s: %(message)s ')

file_handler = logging.FileHandler('Market.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

"""parent class"""
class User:
    def __init__(self, username, password, role_type):
        self.username = username
        self.password = password
        self.role_type = role_type

    """return name of class"""
    def whoami(self):
        return type(self).__name__

    @staticmethod
    def hash_password(password):
        password = bytes(password, 'utf-8')
        hash_password = hashlib.pbkdf2_hmac('sha256', password, b"setzoka", 16)
        hash_password = binascii.hexlify(hash_password)
        return hash_password

    @staticmethod
    def check_username(username):
        for user in lst_users:
            if user.username == username:
                return user

    @staticmethod
    def save_user(user, row_user):
        lst_users.append(user)
        with open("users.txt", 'a', newline="") as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerows(row_user)

    """rewrite users file"""
    @staticmethod
    def rewrite():
        with open('users.txt', "w", newline='') as csv_file:
            for user in lst_users:
                if user.whoami() == "Customer":
                    row_user = [[user.username, user.password, user.role_type, user.flag]]
                elif user.whoami() == "Admin":
                    row_user = [[user.username, user.password, user.role_type]]
                csv_writer = csv.writer(csv_file)
                csv_writer.writerows(row_user)


    @staticmethod
    def delete_account(user):
        for item in lst_users:
            if item == user:
                lst_users.remove(item)
        user.rewrite()


class Admin(User):
    def __init__(self, username, password, role_type="admin"):
        super(Admin, self).__init__(username, password, role_type)

    """check if there is any admin"""
    @staticmethod
    def admin_finder(lst_users):
        for user in lst_users:
            if user.role_type == "admin":
                return True

    """warn if inventory is empty"""
    @staticmethod
    def warning_empty_inventory():
        for i in products.lst_products:
            if i.inventory == 0:
                print(f"{i.name} inventory is empty!")


    @staticmethod
    def unblock_customer(customer_name):
        for user in lst_users:
            if user.role_type == "customer":
                if user.username == customer_name:
                    user.flag = "Free"
                    break

    @staticmethod
    def print_bills():
        with open('bills.txt') as bills:
            for row in bills:
                print(row)


class Customer(User):
    def __init__(self, username, password, role_type="customer", flag="Free"):
        super(Customer, self).__init__(username, password, role_type)
        self.flag = flag

    """check if customer is block and make an error if she/he is"""
    def check_block(self):
        logger.error(f"blocked user {self.username} tried to enter")
        assert self.flag == "Free", f"Dear {self.username} you have been blocked"

    """block a user"""
    def blocker(self):
        for user in lst_users:
            if user == self:
                self.flag = "block"
                user.rewrite()
                break

    """make sure customer can only enter his/her password 3 times wrong. and after that block customer"""
    def password_check_counter(self, user):
        t = 0
        while t != 3:
            password = User.hash_password(input("please enter your password: "))
            if str(password) == str(self.password):
                print("you have entered successfully. you can shop.")
                break
            elif t == 2:
                user.blocker()
                logger.error(f"user {self.username} blocked")
                raise Exception("Sorry your account have been blocked")
            else:
                print(f"wrong password you have {2 - t} more times to try")
                logger.info(f"user {self.username} entered password wrong")
            t += 1

    @staticmethod
    def shopping(product, number):
        try:
            assert product.inventory >= number
            product.inventory = product.inventory - number
            product.update_inventory(product.inventory, product)
            price = number * product.price
            bill = f"item:{product.name}       number:{number}       total price:{price}\n"
            with open("customer_bill.txt", "a") as csv_bill:
                csv_bill.write(bill)
            return price

        except AssertionError:
            print(f"we don't have enough number of goods in inventory. we only have {product.inventory} of this item.")

    """append the customer bill to the total bills so admin can see it later."""


"""make a list of users"""
admin = None
lst_users = []
with open("users.txt") as csv_customers:
    csv_reader = csv.reader(csv_customers, delimiter=',')
    for row in csv_reader:
        if row[2] == "customer":
            user = Customer(row[0], row[1], row[2], row[3])
        elif row[2] == "admin":
            user = Admin(row[0], row[1], row[2])
        lst_users.append(user)
