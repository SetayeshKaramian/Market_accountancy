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


the_goods_lst = []
with open('goods.txt') as csv_goods:
    goods_reader = csv.reader(csv_goods, delimiter=',')
    for row in goods_reader:
        row = [int(x) if x.strip().isdigit() else x.strip() for x in row]
        the_goods_lst.append(Goods(row[0], row[1], row[2], row[3], row[4]))


# def find_good(a_good):
#     with open('goods.txt') as csv_goods:
#         goods_reader = csv.reader(csv_goods, delimiter=',')
#         for row in goods_reader:
#             if row[0] == a_good:
#                 a_good = Goods(row[0], row[1], row[2], row[3], row[4])
#                 return a_good
#             break

def good_finder(a_good):
    print(a_good)
    for good in the_goods_lst:
        if good.name == a_good:
            return good


def add_good(a_good):
    with open('goods.txt', 'a') as csv_goods:
        csv_goods.write(a_good)
        csv_goods.write("\n")


def check_numberof_orient_good(a_good):
    orient_checker = a_good.strip().split(',')
    try:
        assert len(orient_checker) == 5
        return True
    except AssertionError:
        return False


def print_goods():
    for good in the_goods_lst:
        print(good, "\n")


def shopping(a_good):
    good = good_finder(a_good)
    try:
        assert good != None
        number = int(input("please enter number of goods that you want: "))
        try:
            assert good.inventory >= number
            good.inventory = good.inventory - number
            price = number * good.price
            bill = (f"item:{good.name}       number:{number}       total price:{price}\n")
            with open("customer_bill.txt", "a") as csv_bill:
                csv_bill.write(bill)
            return price

        except AssertionError:
            print(f"we don't have enough number of goods in inventory. we only have {good.inventory} of this item.")

    except AssertionError:
        print("there is no such good in our inventory!")


def print_bills():
    with open('bills.txt') as bills:
        for row in bills:
            print(row)


def append_to_total_bills():
    with open("bills.txt", 'a') as total_bill, open("customer_bill.txt", 'r') as customer_bill:
        for row in customer_bill:
            total_bill.write(row)


def rewrite_goods():
    update_time = "this will show time"
    with open("goods.txt", 'w') as file:
        file.write()
    for good in the_goods_lst:
        good_str = (f"{good.name},{good.brand},{good.price},{good.inventory},{good.barcode}\n")
        with open('goods.txt', 'a') as file:
            file.write(good_str)
