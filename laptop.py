from item import Item

class Laptop(Item):
    def __init__(self, name, price, quantity, gpu, port_count):
        super().__init__(name, price, quantity)
        self.gpu = gpu 
        self.port_count = port_count
        self.discount_rate = 0.30
        
laptop = Laptop("HP", 1000 , 4, "NVIDIA GTX 3080", 4)

laptop.apply_discount()

laptop.calculate_total_price()

item_1 = Item("charger", 300, 1)

item_1.apply_discount()