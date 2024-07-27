# Problem 3:

# # extend the above application
# # There are extra attributes in laptop i.e gpu, port_count and also it has 30% discount

# # application folder structure
# 1. items.py
# 2. laptop.py
# 3. data/items.csv

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
        discount_amount = self.price * float(self.discount_rate)
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

class Laptop(Item):
    def __init__(self, name, price, quantity, gpu, port_count):
        super().__init__(name, price, quantity)
        self.gpu = gpu 
        self.port_count = port_count
        self.discount_rate = 0.30
        
Item.read_file()

laptop = Laptop("HP", 1000 , 4, "NVIDIA GTX 3080", 4)

laptop.apply_discount()

laptop.calculate_total_price()

item_1 = Item("charger", 300, 1)

item_1.apply_discount()