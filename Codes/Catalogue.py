import pandas as pd
from Aliment import Aliment

class Catalogue:
    
    def __init__(self):
        
        self.collection = []
        
        fruits_legumes = pd.read_csv("Fruits_Legumes.csv", sep = ";")

        for i in range(fruits_legumes.shape[0]):
            
            a = Aliment(fruits_legumes.iloc[i]["Nom"],
                        fruits_legumes.iloc[i]["Score"],
                        fruits_legumes.iloc[i]["Valeur"],
                        fruits_legumes.iloc[i]["Image"])
            
            self.collection.append(a)
    
    def __str__(self):
        
        return str(len(self.collection))