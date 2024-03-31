class food:
    def __init__(self,name,colories,price):
        self.name = name 
        self.colories = colories
        self.price = price
        

    def lol(self):
        print(self.name,self.colories,self.price,self)


class fast_food(food):
    def __init__(self,name,colories,price,curr):
        super().__init__(name,colories,price,)
        self.curr = curr


    def inform(self):
        print("Here is your",self.name,"it's",self.price,self.curr,",need to mention that it's a little",self.colories,"hehe")

info = fast_food("Pizza Peperoni","fat",11,"$")
info.inform()
                