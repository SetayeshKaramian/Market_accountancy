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

    """find a good by it's name from the list of all goods"""

    @staticmethod
    def good_finder(a_good):
        for good in the_goods_lst:
            if good.name == a_good:
                return good

    """add a good to goods.txt file"""

    @staticmethod
    def add_good(a_good):
        with open('goods.txt', 'a') as csv_goods:
            csv_goods.write(a_good)
            csv_goods.write("\n")

    """print a good from goods list"""

    @staticmethod
    def print_goods():
        for good in the_goods_lst:
            print(good, "\n")


"""make a goods list from goods.txt file"""
the_goods_lst = []
with open('goods.txt') as csv_goods:
    goods_reader = csv.reader(csv_goods, delimiter=',')
    for row in goods_reader:
        row = [int(x) if x.strip().isdigit() else x.strip() for x in row]
        the_goods_lst.append(Goods(row[0], row[1], row[2], row[3], row[4]))

"""after running, rewrite goods.txt to update it. (add new goods and update inventory)"""


def rewrite_goods():
    update_time = "this will show time"
    with open("goods.txt", 'w') as file:
        file.write()
    for good in the_goods_lst:
        good_str = (f"{good.name},{good.brand},{good.price},{good.inventory},{good.barcode}\n")
        with open('goods.txt', 'a') as file:
            file.write(good_str)
