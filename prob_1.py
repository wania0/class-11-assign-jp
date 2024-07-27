"""
Problem 1:

create class Item
add instance properties
  name, price, quantity
create method calcualte_total_price
create method apply_discount
create method all_items

all items have 20% discount by default

# use these items and store it in items.csv

"Phone", 100, 1
"Laptop", 1000, 3
"Cable", 10, 5
"Mouse", 50, 5
"Keyboard", 75, 5

# read items.csv and create objects for each item
# I should be able to print all the items """

# Solution :

class Item:
    items = []
    
    def __init__(self, name, price, quantity):
        
        self.name = name
        self.price = price
        self.quantity = quantity
        self.discount_rate = 0.20
        
    def calculate_total_price(self):
        
        total_price = self.price * self.quantity
        print("The total price is:", total_price) 
           
    def apply_discount(self):
        
        print("Actual price is:", self.price)
        discount_amount = self.price * self.discount_rate
        self.price = self.price - discount_amount
        print(self.discount_rate * 100, "percent discount is applied.New price is:", self.price)

    @classmethod
    def read_file(cls):
        f = open ("items.csv","r")
        data = f.readlines()
        for item in data:
            Item.items.append(item.strip())
        print("Items are:")
        for item in Item.items:
            print(item)
        
Item.read_file()
        
item_1 = Item("charger", 300, 1)

item_1.apply_discount()