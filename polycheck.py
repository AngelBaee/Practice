class mascara:
    def __init__(self,brand,price,cur):
        self.brand = brand
        self.price = price
        self.cur = cur

    def purchase(self):
        print("the price of",self.brand,"is",self.price,self.cur) 


class foundation:
    def __init__(self,brand,price,cur):
        self.brand = brand
        self.price = price
        self.cur = cur

    def purchase(self):
        print("the price of",self.brand,"is",self.price,self.cur) 


class lipstick:
    def __init__(self,brand,price,cur):
        self.brand = brand
        self.price = price
        self.cur = cur

    def purchase(self):
        print("the price of",self.brand,"is",self.price,self.cur)


masc = mascara("Rare beauty mascara",34,"$")
foun = foundation("Misha foundation",25,"$")
lips = lipstick("Dior lipstick",50,"$")

for x in (masc,foun,lips):
    x.purchase()