class game:
    def __init__(self,name,edition):
        self.name = name
        self.edition = edition

    def __str__(self):
        return f"Welcome to {self.name} {self.edition}" 

info = game("The Sims",3)
print(info)    
