class game:
    def __init__ (self,name,edition):
        self.name = name
        self.edition = edition

    def greeting(self):
        print("Welcome to " +self.name,self.edition)
        

info = game("The Sims",3)
info.greeting()


#here we used greeting as a recursion function which helped us to call our function by accessing to the info