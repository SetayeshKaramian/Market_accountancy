import goods
from goods import Goods

"""check if anf inventory is empty and warn the admin about empty ones."""


def warning_empty_inventory():
    for i in goods.the_goods_lst:
        if i.inventory == 0:
            print(f"{i.name} inventory is empty!")


def check_numberof_orient_good(a_good):
    orient_checker = a_good.strip().split(',')
    try:
        assert len(orient_checker) == 5
        return True
    except AssertionError:
        return False


"""get data for adding new good."""


def get_data_new_good():
    data = input("Please enter: name, brand, price, inventory, barcode: ")
    if check_numberof_orient_good(data) is True:
        Goods.add_good(data)
        print("good has been added successfully")
    else:
        print("you didn't fill all the infos!\nPlease try again.")


def print_bills():
    with open('bills.txt') as bills:
        for row in bills:
            print(row)
