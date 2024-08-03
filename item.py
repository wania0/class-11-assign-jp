class Item:
    items = []
    
    def __init__(self, name, price, quantity):
        
        self.name = name
        self.price = price
        self.quantity = quantity
        self.discount_rate = 0.20
        
    def calculate_total_price(self):
        
        total_price = self.price * self.quantity
        print(f"The total price of {self.name} is: {total_price}") 
           
    def apply_discount(self):
        
        print(f"Actual price of {self.name} is:", self.price)
        discount_amount = self.price * self.discount_rate
        self.price = self.price - discount_amount
        print(f"After {self.discount_rate * 100} percent discount on {self.name} new price is: {self.price}")

    @classmethod
    def read_file(cls):
        f = open ("data/items.csv","r")
        data = f.readlines()
        for item in data:
            item = Item(item[0], (item[1]),(item[2]))
            Item.items.append(item)
    
Item.read_file()
        
item_1 = Item("charger", 300, 10)
item_2 = Item("earbuds", 200, 12)

item_1.apply_discount()
item_2.apply_discount()

item_1.calculate_total_price()
item_2.calculate_total_price()