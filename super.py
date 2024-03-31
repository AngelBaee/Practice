class food:
    def __init__(self,name,colories,price,curr):
        self.name = name 
        self.colories = colories
        self.price = price
        self.curr = curr

    def lol(self):
        print(self.name,self.colories,self.price,self.curr)


class fast_food(food):
    def __init__(self,name,colories,price,curr):
        super().__init__(name,colories,price,curr)

info = fast_food("Pizza Peperoni","fat",11,"$")
info.lol()                