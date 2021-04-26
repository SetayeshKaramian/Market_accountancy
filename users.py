import csv


class Users:
    def __init__(self, username, password, role_type="customer", lock="Free"):
        """

        :param username: same
        :param password: same
        :param role_type: whether user is admin ar customer
        :param lock: whether user has been blocked or not
        """
        self.username = username
        self.password = password
        self.role_type = role_type
        self.lock = lock

    def __str__(self):
        return f"Welcome {self.username} you are a {self.role_type}"

    def user_stringer(self):
        user = [self.username, str(self.password), self.role_type, self.lock]
        user_str = (','.join(user))
        return user_str

    def adminer(self, admin_code):
        if admin_code == 1234:
            self.role_type = "admin"
        return self.role_type


def user_blocker(user):
    print('this def will block the user and add it to the csv')


def hash_password(password):
    print("this def will hash the password")


def duplication(username):
    print("this def will check is the username has been in log before")


def username_checker(username):
    with open("users.txt") as csv_users:
        users_reader = csv.reader(csv_users, delimiter=',')
        for row in users_reader:
            if row[0] == username:
                user = Users(row[0], row[1], row[2], row[3])
                if user.lock == "Blocked":
                    user_blocker(row)
                    raise Exception(f"Dear {user.username} you have been blocked!")
                return user


"check pass word and give permission based on whether is customer or admin"


def password_checker(user):
    counter = [1, 2, 3]
    for i in counter:
        password = input("Please enter your password: ").strip()
        print("in near future we will check the hashed pass word")
        # password = hash_password(password)
        if password == user.password and user.role_type == "customer":
            key = True
            print("you logged in successfully as customer\n")
            return key
            break
        elif password == user.password and user.role_type == "admin":
            key = "king key"
            print("you logged in successfully as admin\n")
            return key
            break
        elif i == 3:
            user_blocker(user)
            raise Exception("Sorry. you entered you password wrong for 3 times. we blocked you account!")
        else:
            quit_choice = int(input(f"sorry, the password is not correct."
                                    f" you have {3 - i} more times to try.\n 0.quit, 1.continue:"))
        if quit_choice == 0:
            break


def add_user():
    role = int(input("Do you want to sign in as: 1.customer, 2.admin:"))
    singin_data = input("Please enter username and password\n username,password: ").split(',')
    duplication(singin_data[0])
    print("check if there was a duplication in name")
    singin_data[1] = int(singin_data[1])
    user = Users(singin_data[0], singin_data[1])
    if role == 2:
        admin_code = int(input("Please enter the admin code: "))
        user.adminer(admin_code)

    with open('users.txt', 'a') as csv_users:
        csv_users.write(user.user_stringer())
        csv_users.write("\n")

    # with open('users.txt') as csv_users:
    #     users_reader = csv.reader(csv_users, delimiter=',')
    #     for row in users_reader:
    #         if row[0] == username:
    #             duplication = True

    # try:
    #     assert duplication is False
    #     password = input("Please enter a password: ")
    #     lst_user = [username, password]
    #     user = (','.join(lst_user))
    #     with open('users.txt', 'a') as csv_users:
    #         csv_users.write(user)
    #         csv_users.write("\n")
    #
    # except AssertionError:
    #     print("This username already exists. try another one.")
