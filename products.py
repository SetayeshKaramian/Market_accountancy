import csv


class Product:
    def __init__(self, name, brand, price, inventory, barcode):
        self.name = name
        self.brand = brand
        self.price = price
        self.inventory = inventory
        self.barcode = barcode

    def __str__(self):
        return f"name: {self.name}\nbrand: {self.brand}\nprice: {self.price}"

    """find product in product list"""

    @staticmethod
    def find_product(product):
        found_product = None
        for item in lst_products:
            if item.name == product:
                found_product = item
                break
        return found_product

    """rewrite products file"""

    @staticmethod
    def rewrite_products():
        with open('products.txt', 'w', newline='') as csv_file:
            for item in lst_products:
                row = [[item.name, item.brand, item.price, item.inventory, item.barcode]]
                csv_writer = csv.writer(csv_file)
                csv_writer.writerows(row)

    @staticmethod
    def update_inventory(new_inventory, product):
        for item in lst_products:
            if item == product:
                item.inventory = new_inventory

    """creat new product"""

    @staticmethod
    def add_product(str_product):
        product_info = str_product.split(',')
        product_info = [int(x) if x.strip().isdigit() else x.strip() for x in product_info]
        try:
            new_product = Product(product_info[0], product_info[1], product_info[2], product_info[3], product_info[4])
            try:
                for item in lst_products:
                    assert item.barcode != new_product.barcode

                lst_products.append(new_product)
                return new_product.name

            except AssertionError:
                print("this product already exist")

        except IndexError:
            print("info is not correct")


lst_products = []
with open("products.txt") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    for row in csv_reader:
        row = [int(x) if x.strip().isdigit() else x.strip() for x in row]
        product = Product(row[0], row[1], row[2], row[3], row[4])
        lst_products.append(product)
