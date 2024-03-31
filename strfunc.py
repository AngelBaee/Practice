class gadgets:
    def __init__(self,brand,price,currency):
        self.brand = brand
        self.price = price
        self.currency = currency

    def __str__(self):
        return f'{self.brand}({self.price}{self.currency})'  

info = gadgets("Asus",1000,"$")

print(info)