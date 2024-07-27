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