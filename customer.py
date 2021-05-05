from goods import Goods


# def customer_bill(user):
#     with open("customer_bill.txt", 'w') as bill:
#         bill.write(user.username)
#         bill.write('\n')


def shopping(a_good):
    good = Goods.good_finder(a_good)
    try:
        assert good != None
        number = int(input("please enter number of goods that you want: "))
        try:
            assert good.inventory >= number
            good.inventory = good.inventory - number
            price = number * good.price
            bill = f"item:{good.name}       number:{number}       total price:{price}\n"
            with open("customer_bill.txt", "a") as csv_bill:
                csv_bill.write(bill)
            return price

        except AssertionError:
            print(f"we don't have enough number of goods in inventory. we only have {good.inventory} of this item.")

    except AssertionError:
        print("there is no such good in our inventory!")


"""append the customer bill to the total bills so admin can see it later."""


def append_to_total_bills():
    with open("bills.txt", 'a') as total_bill, open("customer_bill.txt", 'r') as customer_bill:
        for row in customer_bill:
            total_bill.write(row)
