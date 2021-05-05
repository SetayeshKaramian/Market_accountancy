import pandas as pd
import csv
import hashlib, binascii


class Users:
    def __init__(self, username, password, role_type="customer", flag="Free"):
        """

        :param username: same
        :param password: same
        :param role_type: whether user is admin ar customer
        :param flag: whether user has been blocked or not
        """
        self.username = username
        self.password = password
        self.role_type = role_type
        self.flag = flag

    def __str__(self):
        return f"Welcome {self.username} you are a {self.role_type}"

    """block the user and save it to log"""

    def user_blocker(self, lst_users):
        new_lst_users = []
        for item in lst_users:
            if item != self:
                new_lst_users.append(item)
        self.flag = "block"
        new_lst_users.append(self)
        with open('users.txt', "w", newline='') as csv_file:
            for user in new_lst_users:
                row_user = [[user.username, user.password, user.role_type, user.flag]]
                csv_writer = csv.writer(csv_file)
                csv_writer.writerows(row_user)
        return new_lst_users

    """if the user has the right code for becoming a admin, change their role to admin."""

    def adminer(self, admin_code):
        if admin_code == 1234:
            self.role_type = "admin"
            print("your now an admin!")
        return self.role_type

    """check if user is block or not"""

    def check_block(self):
        assert self.flag == "Free", f"Dear{self.username} you have been blocked"

    """hash passwords and save them as binascii numbers"""

    @staticmethod
    def hash_password():
        password = input("please enter your password: ")
        password = bytes(password, 'utf-8')
        hash_password = hashlib.pbkdf2_hmac('sha256', password, b"setzoka", 16)
        hash_password = binascii.hexlify(hash_password)
        return hash_password

    """register user and append to the log"""

    @staticmethod
    def register(lst_usernames):

        username = input("please enter your username: ")
        try:
            assert username not in lst_usernames
            hash_password = Users.hash_password()
            new_user = Users(username, hash_password)
            role = input("do you want to sing in as an admin?(y/n)")
            if role == "y":
                admin_code = int(input("please enter admin code: "))
                new_user.adminer(admin_code)
            row_user = [[new_user.username, new_user.password, new_user.role_type, new_user.flag]]
            with open('users.txt', 'a', newline='') as csv_file:
                csv_writer = csv.writer(csv_file)
                csv_writer.writerows(row_user)

        except AssertionError:
            print("this username is not valid")

    """when login, check username"""

    @staticmethod
    def check_username(lst_usernames):
        username = input("please enter you user name: ")
        if username in lst_usernames:
            for item in lst_users:
                if item.username == username:
                    user = item
                    break
            return user
        else:
            return print("user not found")

    """when login, check password"""

    @staticmethod
    def password_checker(user, lst_users):
        t = 0
        key = None
        while t != 3:
            password = Users.hash_password()
            if str(password) == user.password and user.role_type == "customer":
                key = True
                print("you logged in successfully as customer\n")
                break
            elif str(password) == user.password and user.role_type == "admin":
                key = "king key"
                print("you logged in successfully as admin\n")
                break
            elif t == 2:
                user.user_blocker(lst_users)
                raise Exception("Sorry. you entered you password wrong for 3 times. we blocked you account!")
            else:
                quit_choice = int(input(f"sorry, the password is not correct."
                                        f" you have {2 - t} more times to try.\n 0.quit, 1.continue: "))
            if quit_choice == 0:
                break
            t += 1
        return key


"""make a list of usernames"""
file_path = "users.txt"
df_accounts = pd.read_csv(file_path)
lst_usernames = list(df_accounts["username"])

"""make a list of objects of Users class from users.txt file."""
lst_users = []
with open('users.txt') as csv_users:
    csv_reader = csv.reader(csv_users, delimiter=',')
    for row in csv_reader:
        user = Users(row[0], row[1], row[2], row[3])
        lst_users.append(user)
