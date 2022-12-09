class Aliment:
    
    def __init__(self, name, score, nutritional_value, image):
        
        self.name = name.lower()
        self.score = score
        self.nutritional_value = nutritional_value
        self.image = image
        
    def __str__(self):
        
        return self.name + " | " + str(self.score) + " | " + str(self.nutritional_value) + " | " + self.image