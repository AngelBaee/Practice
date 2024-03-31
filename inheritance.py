class car:
    def __init__(lol,brand,model,color):
        lol.brand = brand
        lol.model = model
        lol.color = color

    def noideawhat(lol):
        print(lol.brand,lol.model,lol.color)

info = car("Ford Mustang","GT-500","black")
info.noideawhat()            
