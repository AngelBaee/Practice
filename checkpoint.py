class car:
    def __init__(self,brand,model,color):
        self.brand = brand
        self.model = model
        self.color = color

    def noideawhat(self):
        print(self.brand,self.model,self.color)  
        
class American(car):
    def __init__(lol,brand,model,color):
        car.__init__(lol,brand,model,color)


class German(car):
    def __init__(lol,brand,model,color):
        car.__init__(lol,brand,model,color)

class Japanese(car):
    def __init__(lol,brand,model,color):
        car.__init__(lol,brand,model,color)

info_americano = American("Ford Mustang","GT-500","black")
info_germano = German("BMW","M5","metalic")
info_japano = Japanese ("Toyota Supra","Blablabla","white")


info_americano.noideawhat()
info_germano.noideawhat()
info_japano.noideawhat()

#failed
#Fixed ыхыхыххыхыхыхыхыыхых