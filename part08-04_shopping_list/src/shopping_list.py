# DO NOT CHANGE THE CODE OF THE CLASS
# ShoppingList. Write yous solution under it!
class ShoppingList:
    def __init__(self):
        self.products = []

    def number_of_items(self):
        return len(self.products)

    def add(self, product, number):
        self.products.append((product, number))

    def item(self, n):
        return self.products[n - 1][0]

    def amount(self, n):
        return self.products[n - 1][1]

# -------------------------
# Write your solution here:
# -------------------------

def total_units(list):
    total_items = 0
    for items in list.products:
        total_items += items[1]
    return total_items

if __name__ == "__main__":
    my_list = ShoppingList()
    my_list.add("bananas", 10)
    my_list.add("apples", 5)
    my_list.add("pineapple", 1)

    print(total_units(my_list))