# Name: Quang Le
# Student ID: 1768324 

class ItemToPurchase:

    def __init__(self, item_name="none", item_price=0, item_quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

    def print_item_cost(self):
        cost = self.item_price * self.item_quantity
        print('{} {:.0f} @ ${:.0f} = ${:.0f}'.format(self.item_name, self.item_quantity, self.item_price, cost))
        return cost


print("Item 1")
name1 = input("Enter the item name:\n")
price1 = float(input("Enter the item price:\n"))
quant1 = float(input("Enter the item quantity:\n"))

print()
print("Item 2")
name2 = input("Enter the item name:\n")
price2 = float(input("Enter the item price:\n"))
quant2 = float(input("Enter the item quantity:\n"))

print()
print("TOTAL COST")
item1 = ItemToPurchase(name1, price1, quant1)
cost1 = item1.print_item_cost()
item2 = ItemToPurchase(name2, price2, quant2)
cost2 = item2.print_item_cost()
total = cost1+cost2
print()
print("Total: ${:.0f}".format(total))
