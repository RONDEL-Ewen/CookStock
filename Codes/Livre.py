import pandas as pd
from Recette import Recette

class Livre:
    
    def __init__(self):
        
        self.collection = {}
        
        recettes = pd.read_csv("Recettes.csv", sep = ";")
        recettes = recettes.fillna("")
        
        for i in range(recettes.shape[0]):
            
            r = Recette(recettes.iloc[i]["Nom"],
                        recettes.iloc[i]["Type"],
                        recettes.iloc[i]["Lien"],
                        recettes.iloc[i]["Ingredient 1"],
                        recettes.iloc[i]["Ingredient 2"],
                        recettes.iloc[i]["Ingredient 3"])
            
            self.collection[r] = 0

        self.collection = dict(sorted(self.collection.items(), key=lambda item: item[0].name, reverse=False))
            
    def __str__(self):

        result = ""
        for key, value in self.collection.items():
            result = result + key.name + " | " + str(value) + "\n"
        
        #return str(len(self.collection))
        return result