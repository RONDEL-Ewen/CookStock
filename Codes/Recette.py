class Recette:
    
    def __init__(self, name, sort, link, a1, a2 = "", a3 = ""):
        
        self.name = name
        self.sort = sort
        self.link = link
        self.a1 = a1.lower()
        self.a2 = a2.lower()
        self.a3 = a3.lower()
    
    def __str__(self):
        
        return self.name + " | " + self.sort + " | " + self.a1 + " | " + str(self.a2) + " | " + str(self.a3)