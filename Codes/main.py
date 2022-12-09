from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.button import ButtonBehavior
from kivy.uix.image import Image

import time

import pandas as pd

from Aliment import Aliment
from Catalogue import Catalogue
from Recette import Recette
from Livre import Livre
from Rangement import Rangement

class Loading(Screen):
    pass
class Accueil(Screen):
    pass
class Placard(Screen):
    pass
class Frigo(Screen):
    pass
class Congelo(Screen):
    pass
class CatalogueA(Screen):
    pass
class CatalogueB(Screen):
    pass
class CatalogueC(Screen):
    pass
class CatalogueD(Screen):
    pass
class Fiche(Screen):
    pass
class Liste(Screen):
    pass

class ImageButton(ButtonBehavior, Image):
    pass

GUI = Builder.load_file("main.kv")

class MainApp(App):

    def build(self):
        self.catalogue = Catalogue()
        self.livre = Livre()
        self.placard = Rangement()
        self.frigo = Rangement()
        self.congelo = Rangement()
        self.selection_rangement = ""
        self.state = "accueil"
        return GUI

    def on_start(self, **kwargs):
        self.update_recettes_accueil()
        self.update_fiche(0)
        #time.sleep(3)
        self.change_screen("accueil_screen")

    def change_screen(self, screen_name):
        screen_manager = self.root.ids['screen_manager']
        screen_manager.current = screen_name

    def update_recettes_accueil(self):
        self.root.ids['accueil_screen'].ids['recette1_name'].text = list(self.livre.collection.items())[0][0].name
        self.root.ids['accueil_screen'].ids['recette1_a1'].text = list(self.livre.collection.items())[0][0].a1
        self.root.ids['accueil_screen'].ids['recette1_a2'].text = list(self.livre.collection.items())[0][0].a2
        self.root.ids['accueil_screen'].ids['recette1_a3'].text = list(self.livre.collection.items())[0][0].a3
        self.root.ids['accueil_screen'].ids['recette1_image'].source = "Images/CookStock/Recettes/" + list(self.livre.collection.items())[0][0].name + ".jpg"

        self.root.ids['accueil_screen'].ids['recette2_name'].text = list(self.livre.collection.items())[1][0].name
        self.root.ids['accueil_screen'].ids['recette2_a1'].text = list(self.livre.collection.items())[1][0].a1
        self.root.ids['accueil_screen'].ids['recette2_a2'].text = list(self.livre.collection.items())[1][0].a2
        self.root.ids['accueil_screen'].ids['recette2_a3'].text = list(self.livre.collection.items())[1][0].a3
        self.root.ids['accueil_screen'].ids['recette2_image'].source = "Images/CookStock/Recettes/" + list(self.livre.collection.items())[1][0].name + ".jpg"

        self.root.ids['accueil_screen'].ids['recette3_name'].text = list(self.livre.collection.items())[2][0].name
        self.root.ids['accueil_screen'].ids['recette3_a1'].text = list(self.livre.collection.items())[2][0].a1
        self.root.ids['accueil_screen'].ids['recette3_a2'].text = list(self.livre.collection.items())[2][0].a2
        self.root.ids['accueil_screen'].ids['recette3_a3'].text = list(self.livre.collection.items())[2][0].a3
        self.root.ids['accueil_screen'].ids['recette3_image'].source = "Images/CookStock/Recettes/" + list(self.livre.collection.items())[2][0].name + ".jpg"

    def classify_recettes(self):
        all_aliments = self.placard.places + self.frigo.places + self.congelo.places
        all_names = []

        for x in all_aliments:
            if(x.name not in all_names):
                all_names.append(x.name)

        for key, value in self.livre.collection.items():
            score = 0
            nb_aliments = 0
            nb_aliments_communs = 0

            if((key.a2 != "") and (key.a3 != "")):
                nb_aliments = 3
            if((key.a2 != "") and (key.a3 == "")):
                nb_aliments = 2
            if((key.a2 == "") and (key.a3 == "")):
                nb_aliments = 1

            if(key.a1 in all_names):
                nb_aliments_communs = nb_aliments_communs + 1
            if(key.a2 in all_names):
                nb_aliments_communs = nb_aliments_communs + 1
            if(key.a3 in all_names):
                nb_aliments_communs = nb_aliments_communs + 1

            if((nb_aliments_communs == 3) and (nb_aliments == 3)):
                score = 100
            if((nb_aliments_communs == 2) and (nb_aliments == 2)):
                score = 90
            if((nb_aliments_communs == 2) and (nb_aliments == 3)):
                score = 80
            if((nb_aliments_communs == 1) and (nb_aliments == 1)):
                score = 70
            if((nb_aliments_communs == 1) and (nb_aliments == 2)):
                score = 60
            if((nb_aliments_communs == 1) and (nb_aliments == 3)):
                score = 50
            if(nb_aliments_communs == 0):
                score = 0

            self.livre.collection[key] = score

        self.livre.collection = dict(sorted(self.livre.collection.items(), key = lambda item:item[1], reverse = True))

    def update_fiche(self, i):
        self.root.ids['fiche_screen'].ids['recette_name'].text = list(self.livre.collection.items())[i][0].name
        self.root.ids['fiche_screen'].ids['recette_sort'].text = list(self.livre.collection.items())[i][0].sort
        self.root.ids['fiche_screen'].ids['recette_a1'].text = list(self.livre.collection.items())[i][0].a1
        self.root.ids['fiche_screen'].ids['recette_a2'].text = list(self.livre.collection.items())[i][0].a2
        self.root.ids['fiche_screen'].ids['recette_a3'].text = list(self.livre.collection.items())[i][0].a3
        self.root.ids['fiche_screen'].ids['recette_link'].text = list(self.livre.collection.items())[i][0].link
        self.root.ids['fiche_screen'].ids['recette_image'].source = "Images/CookStock/Recettes/" + list(self.livre.collection.items())[i][0].name + ".jpg"

    def update_liste(self):
        self.root.ids['liste_screen'].ids['pa'].text = list(self.livre.collection.items())[0][0].name
        self.root.ids['liste_screen'].ids['pb'].text = list(self.livre.collection.items())[1][0].name
        self.root.ids['liste_screen'].ids['pc'].text = list(self.livre.collection.items())[2][0].name
        self.root.ids['liste_screen'].ids['pd'].text = list(self.livre.collection.items())[3][0].name
        self.root.ids['liste_screen'].ids['pe'].text = list(self.livre.collection.items())[4][0].name
        self.root.ids['liste_screen'].ids['pf'].text = list(self.livre.collection.items())[5][0].name
        self.root.ids['liste_screen'].ids['pg'].text = list(self.livre.collection.items())[6][0].name
        self.root.ids['liste_screen'].ids['ph'].text = list(self.livre.collection.items())[7][0].name
        self.root.ids['liste_screen'].ids['pi'].text = list(self.livre.collection.items())[8][0].name
        self.root.ids['liste_screen'].ids['pj'].text = list(self.livre.collection.items())[9][0].name
        self.root.ids['liste_screen'].ids['pk'].text = list(self.livre.collection.items())[10][0].name

    def get_back_from_catalogue(self):
        self.update_placard()
        self.update_frigo()
        self.update_congelo()
        if(self.selection_rangement == "placard"):
            self.change_screen("placard_screen")
        if (self.selection_rangement == "frigo"):
            self.change_screen("frigo_screen")
        if (self.selection_rangement == "congelo"):
            self.change_screen("congelo_screen")

    def get_back_from_fiche(self):
        if(self.state == "accueil"):
            self.change_screen("accueil_screen")
        if(self.state == "liste"):
            self.change_screen("liste_screen")

    def add_aliment(self, aliment):
        for x in self.catalogue.collection:
            if(x.name == aliment):
                if(self.selection_rangement == "placard"):
                    self.placard.places.append(x)
                if (self.selection_rangement == "frigo"):
                    self.frigo.places.append(x)
                if (self.selection_rangement == "congelo"):
                    self.congelo.places.append(x)

    def supp_aliment(self, i):
        if(self.selection_rangement == "placard"):
            if(len(self.placard.places) >= i):
                del self.placard.places[i]
                self.update_placard()
        if(self.selection_rangement == "frigo"):
            if (len(self.frigo.places) >= i):
                del self.frigo.places[i]
                self.update_frigo()
        if(self.selection_rangement == "congelo"):
            if (len(self.congelo.places) >= i):
                del self.congelo.places[i]
                self.update_congelo()

    def print_aliments(self, rangement):
        for x in rangement.places:
            print(x)

    def update_placard(self):
        if(len(self.placard.places) >= 1):
            self.root.ids['placard_screen'].ids["p1_image"].source = "Images/CookStock/Aliments/" + self.placard.places[0].name + ".jpg"
        else:
            self.root.ids['placard_screen'].ids["p1_image"].source = "Images/CookStock/white.png"
        if (len(self.placard.places) >= 2):
            self.root.ids['placard_screen'].ids["p2_image"].source = "Images/CookStock/Aliments/" + self.placard.places[1].name + ".jpg"
        else:
            self.root.ids['placard_screen'].ids["p2_image"].source = "Images/CookStock/white.png"
        if (len(self.placard.places) >= 3):
            self.root.ids['placard_screen'].ids["p3_image"].source = "Images/CookStock/Aliments/" + self.placard.places[2].name + ".jpg"
        else:
            self.root.ids['placard_screen'].ids["p3_image"].source = "Images/CookStock/white.png"
        if (len(self.placard.places) >= 4):
            self.root.ids['placard_screen'].ids["p4_image"].source = "Images/CookStock/Aliments/" + self.placard.places[3].name + ".jpg"
        else:
            self.root.ids['placard_screen'].ids["p4_image"].source = "Images/CookStock/white.png"
        if (len(self.placard.places) >= 5):
            self.root.ids['placard_screen'].ids["p5_image"].source = "Images/CookStock/Aliments/" + self.placard.places[4].name + ".jpg"
        else:
            self.root.ids['placard_screen'].ids["p5_image"].source = "Images/CookStock/white.png"
        if (len(self.placard.places) >= 6):
            self.root.ids['placard_screen'].ids["p6_image"].source = "Images/CookStock/Aliments/" + self.placard.places[5].name + ".jpg"
        else:
            self.root.ids['placard_screen'].ids["p6_image"].source = "Images/CookStock/white.png"
        if (len(self.placard.places) >= 7):
            self.root.ids['placard_screen'].ids["p7_image"].source = "Images/CookStock/Aliments/" + self.placard.places[6].name + ".jpg"
        else:
            self.root.ids['placard_screen'].ids["p7_image"].source = "Images/CookStock/white.png"
        if (len(self.placard.places) >= 8):
            self.root.ids['placard_screen'].ids["p8_image"].source = "Images/CookStock/Aliments/" + self.placard.places[7].name + ".jpg"
        else:
            self.root.ids['placard_screen'].ids["p8_image"].source = "Images/CookStock/white.png"
        if (len(self.placard.places) >= 9):
            self.root.ids['placard_screen'].ids["p9_image"].source = "Images/CookStock/Aliments/" + self.placard.places[8].name + ".jpg"
        else:
            self.root.ids['placard_screen'].ids["p9_image"].source = "Images/CookStock/white.png"
        if (len(self.placard.places) >= 10):
            self.root.ids['placard_screen'].ids["p10_image"].source = "Images/CookStock/Aliments/" + self.placard.places[9].name + ".jpg"
        else:
            self.root.ids['placard_screen'].ids["p10_image"].source = "Images/CookStock/white.png"
        if (len(self.placard.places) >= 11):
            self.root.ids['placard_screen'].ids["p11_image"].source = "Images/CookStock/Aliments/" + self.placard.places[10].name + ".jpg"
        else:
            self.root.ids['placard_screen'].ids["p11_image"].source = "Images/CookStock/white.png"
        if (len(self.placard.places) >= 12):
            self.root.ids['placard_screen'].ids["p12_image"].source = "Images/CookStock/Aliments/" + self.placard.places[11].name + ".jpg"
        else:
            self.root.ids['placard_screen'].ids["p12_image"].source = "Images/CookStock/white.png"
        if (len(self.placard.places) >= 13):
            self.root.ids['placard_screen'].ids["p13_image"].source = "Images/CookStock/Aliments/" + self.placard.places[12].name + ".jpg"
        else:
            self.root.ids['placard_screen'].ids["p13_image"].source = "Images/CookStock/white.png"
        if (len(self.placard.places) >= 14):
            self.root.ids['placard_screen'].ids["p14_image"].source = "Images/CookStock/Aliments/" + self.placard.places[13].name + ".jpg"
        else:
            self.root.ids['placard_screen'].ids["p14_image"].source = "Images/CookStock/white.png"
        if (len(self.placard.places) >= 15):
            self.root.ids['placard_screen'].ids["p15_image"].source = "Images/CookStock/Aliments/" + self.placard.places[14].name + ".jpg"
        else:
            self.root.ids['placard_screen'].ids["p15_image"].source = "Images/CookStock/white.png"
        if (len(self.placard.places) >= 16):
            self.root.ids['placard_screen'].ids["p16_image"].source = "Images/CookStock/Aliments/" + self.placard.places[15].name + ".jpg"
        else:
            self.root.ids['placard_screen'].ids["p16_image"].source = "Images/CookStock/white.png"
        if (len(self.placard.places) >= 17):
            self.root.ids['placard_screen'].ids["p17_image"].source = "Images/CookStock/Aliments/" + self.placard.places[16].name + ".jpg"
        else:
            self.root.ids['placard_screen'].ids["p17_image"].source = "Images/CookStock/white.png"
        if (len(self.placard.places) >= 18):
            self.root.ids['placard_screen'].ids["p18_image"].source = "Images/CookStock/Aliments/" + self.placard.places[17].name + ".jpg"
        else:
            self.root.ids['placard_screen'].ids["p18_image"].source = "Images/CookStock/white.png"
        if (len(self.placard.places) >= 19):
            self.root.ids['placard_screen'].ids["p19_image"].source = "Images/CookStock/Aliments/" + self.placard.places[18].name + ".jpg"
        else:
            self.root.ids['placard_screen'].ids["p19_image"].source = "Images/CookStock/white.png"
        if (len(self.placard.places) >= 20):
            self.root.ids['placard_screen'].ids["p20_image"].source = "Images/CookStock/Aliments/" + self.placard.places[19].name + ".jpg"
        else:
            self.root.ids['placard_screen'].ids["p20_image"].source = "Images/CookStock/white.png"
        if (len(self.placard.places) >= 21):
            self.root.ids['placard_screen'].ids["p21_image"].source = "Images/CookStock/Aliments/" + self.placard.places[20].name + ".jpg"
        else:
            self.root.ids['placard_screen'].ids["p21_image"].source = "Images/CookStock/white.png"
        if (len(self.placard.places) >= 22):
            self.root.ids['placard_screen'].ids["p22_image"].source = "Images/CookStock/Aliments/" + self.placard.places[21].name + ".jpg"
        else:
            self.root.ids['placard_screen'].ids["p22_image"].source = "Images/CookStock/white.png"
        if (len(self.placard.places) >= 23):
            self.root.ids['placard_screen'].ids["p23_image"].source = "Images/CookStock/Aliments/" + self.placard.places[22].name + ".jpg"
        else:
            self.root.ids['placard_screen'].ids["p23_image"].source = "Images/CookStock/white.png"
        if (len(self.placard.places) >= 24):
            self.root.ids['placard_screen'].ids["p24_image"].source = "Images/CookStock/Aliments/" + self.placard.places[23].name + ".jpg"
        else:
            self.root.ids['placard_screen'].ids["p24_image"].source = "Images/CookStock/white.png"

    def update_frigo(self):
        if(len(self.frigo.places) >= 1):
            self.root.ids['frigo_screen'].ids["p1_image"].source = "Images/CookStock/Aliments/" + self.frigo.places[0].name + ".jpg"
        else:
            self.root.ids['frigo_screen'].ids["p1_image"].source = "Images/CookStock/white.png"
        if (len(self.frigo.places) >= 2):
            self.root.ids['frigo_screen'].ids["p2_image"].source = "Images/CookStock/Aliments/" + self.frigo.places[1].name + ".jpg"
        else:
            self.root.ids['frigo_screen'].ids["p2_image"].source = "Images/CookStock/white.png"
        if (len(self.frigo.places) >= 3):
            self.root.ids['frigo_screen'].ids["p3_image"].source = "Images/CookStock/Aliments/" + self.frigo.places[2].name + ".jpg"
        else:
            self.root.ids['frigo_screen'].ids["p3_image"].source = "Images/CookStock/white.png"
        if (len(self.frigo.places) >= 4):
            self.root.ids['frigo_screen'].ids["p4_image"].source = "Images/CookStock/Aliments/" + self.frigo.places[3].name + ".jpg"
        else:
            self.root.ids['frigo_screen'].ids["p4_image"].source = "Images/CookStock/white.png"
        if (len(self.frigo.places) >= 5):
            self.root.ids['frigo_screen'].ids["p5_image"].source = "Images/CookStock/Aliments/" + self.frigo.places[4].name + ".jpg"
        else:
            self.root.ids['frigo_screen'].ids["p5_image"].source = "Images/CookStock/white.png"
        if (len(self.frigo.places) >= 6):
            self.root.ids['frigo_screen'].ids["p6_image"].source = "Images/CookStock/Aliments/" + self.frigo.places[5].name + ".jpg"
        else:
            self.root.ids['frigo_screen'].ids["p6_image"].source = "Images/CookStock/white.png"
        if (len(self.frigo.places) >= 7):
            self.root.ids['frigo_screen'].ids["p7_image"].source = "Images/CookStock/Aliments/" + self.frigo.places[6].name + ".jpg"
        else:
            self.root.ids['frigo_screen'].ids["p7_image"].source = "Images/CookStock/white.png"
        if (len(self.frigo.places) >= 8):
            self.root.ids['frigo_screen'].ids["p8_image"].source = "Images/CookStock/Aliments/" + self.frigo.places[7].name + ".jpg"
        else:
            self.root.ids['frigo_screen'].ids["p8_image"].source = "Images/CookStock/white.png"
        if (len(self.frigo.places) >= 9):
            self.root.ids['frigo_screen'].ids["p9_image"].source = "Images/CookStock/Aliments/" + self.frigo.places[8].name + ".jpg"
        else:
            self.root.ids['frigo_screen'].ids["p9_image"].source = "Images/CookStock/white.png"
        if (len(self.frigo.places) >= 10):
            self.root.ids['frigo_screen'].ids["p10_image"].source = "Images/CookStock/Aliments/" + self.frigo.places[9].name + ".jpg"
        else:
            self.root.ids['frigo_screen'].ids["p10_image"].source = "Images/CookStock/white.png"
        if (len(self.frigo.places) >= 11):
            self.root.ids['frigo_screen'].ids["p11_image"].source = "Images/CookStock/Aliments/" + self.frigo.places[10].name + ".jpg"
        else:
            self.root.ids['frigo_screen'].ids["p11_image"].source = "Images/CookStock/white.png"
        if (len(self.frigo.places) >= 12):
            self.root.ids['frigo_screen'].ids["p12_image"].source = "Images/CookStock/Aliments/" + self.frigo.places[11].name + ".jpg"
        else:
            self.root.ids['frigo_screen'].ids["p12_image"].source = "Images/CookStock/white.png"
        if (len(self.frigo.places) >= 13):
            self.root.ids['frigo_screen'].ids["p13_image"].source = "Images/CookStock/Aliments/" + self.frigo.places[12].name + ".jpg"
        else:
            self.root.ids['frigo_screen'].ids["p13_image"].source = "Images/CookStock/white.png"
        if (len(self.frigo.places) >= 14):
            self.root.ids['frigo_screen'].ids["p14_image"].source = "Images/CookStock/Aliments/" + self.frigo.places[13].name + ".jpg"
        else:
            self.root.ids['frigo_screen'].ids["p14_image"].source = "Images/CookStock/white.png"
        if (len(self.frigo.places) >= 15):
            self.root.ids['frigo_screen'].ids["p15_image"].source = "Images/CookStock/Aliments/" + self.frigo.places[14].name + ".jpg"
        else:
            self.root.ids['frigo_screen'].ids["p15_image"].source = "Images/CookStock/white.png"
        if (len(self.frigo.places) >= 16):
            self.root.ids['frigo_screen'].ids["p16_image"].source = "Images/CookStock/Aliments/" + self.frigo.places[15].name + ".jpg"
        else:
            self.root.ids['frigo_screen'].ids["p16_image"].source = "Images/CookStock/white.png"
        if (len(self.frigo.places) >= 17):
            self.root.ids['frigo_screen'].ids["p17_image"].source = "Images/CookStock/Aliments/" + self.frigo.places[16].name + ".jpg"
        else:
            self.root.ids['frigo_screen'].ids["p17_image"].source = "Images/CookStock/white.png"
        if (len(self.frigo.places) >= 18):
            self.root.ids['frigo_screen'].ids["p18_image"].source = "Images/CookStock/Aliments/" + self.frigo.places[17].name + ".jpg"
        else:
            self.root.ids['frigo_screen'].ids["p18_image"].source = "Images/CookStock/white.png"
        if (len(self.frigo.places) >= 19):
            self.root.ids['frigo_screen'].ids["p19_image"].source = "Images/CookStock/Aliments/" + self.frigo.places[18].name + ".jpg"
        else:
            self.root.ids['frigo_screen'].ids["p19_image"].source = "Images/CookStock/white.png"
        if (len(self.frigo.places) >= 20):
            self.root.ids['frigo_screen'].ids["p20_image"].source = "Images/CookStock/Aliments/" + self.frigo.places[19].name + ".jpg"
        else:
            self.root.ids['frigo_screen'].ids["p20_image"].source = "Images/CookStock/white.png"
        if (len(self.frigo.places) >= 21):
            self.root.ids['frigo_screen'].ids["p21_image"].source = "Images/CookStock/Aliments/" + self.frigo.places[20].name + ".jpg"
        else:
            self.root.ids['frigo_screen'].ids["p21_image"].source = "Images/CookStock/white.png"
        if (len(self.frigo.places) >= 22):
            self.root.ids['frigo_screen'].ids["p22_image"].source = "Images/CookStock/Aliments/" + self.frigo.places[21].name + ".jpg"
        else:
            self.root.ids['frigo_screen'].ids["p22_image"].source = "Images/CookStock/white.png"
        if (len(self.frigo.places) >= 23):
            self.root.ids['frigo_screen'].ids["p23_image"].source = "Images/CookStock/Aliments/" + self.frigo.places[22].name + ".jpg"
        else:
            self.root.ids['frigo_screen'].ids["p23_image"].source = "Images/CookStock/white.png"
        if (len(self.frigo.places) >= 24):
            self.root.ids['frigo_screen'].ids["p24_image"].source = "Images/CookStock/Aliments/" + self.frigo.places[23].name + ".jpg"
        else:
            self.root.ids['frigo_screen'].ids["p24_image"].source = "Images/CookStock/white.png"

    def update_congelo(self):
        if(len(self.congelo.places) >= 1):
            self.root.ids['congelo_screen'].ids["p1_image"].source = "Images/CookStock/Aliments/" + self.congelo.places[0].name + ".jpg"
        else:
            self.root.ids['congelo_screen'].ids["p1_image"].source = "Images/CookStock/white.png"
        if (len(self.congelo.places) >= 2):
            self.root.ids['congelo_screen'].ids["p2_image"].source = "Images/CookStock/Aliments/" + self.congelo.places[1].name + ".jpg"
        else:
            self.root.ids['congelo_screen'].ids["p2_image"].source = "Images/CookStock/white.png"
        if (len(self.congelo.places) >= 3):
            self.root.ids['congelo_screen'].ids["p3_image"].source = "Images/CookStock/Aliments/" + self.congelo.places[2].name + ".jpg"
        else:
            self.root.ids['congelo_screen'].ids["p3_image"].source = "Images/CookStock/white.png"
        if (len(self.congelo.places) >= 4):
            self.root.ids['congelo_screen'].ids["p4_image"].source = "Images/CookStock/Aliments/" + self.congelo.places[3].name + ".jpg"
        else:
            self.root.ids['congelo_screen'].ids["p4_image"].source = "Images/CookStock/white.png"
        if (len(self.congelo.places) >= 5):
            self.root.ids['congelo_screen'].ids["p5_image"].source = "Images/CookStock/Aliments/" + self.congelo.places[4].name + ".jpg"
        else:
            self.root.ids['congelo_screen'].ids["p5_image"].source = "Images/CookStock/white.png"
        if (len(self.congelo.places) >= 6):
            self.root.ids['congelo_screen'].ids["p6_image"].source = "Images/CookStock/Aliments/" + self.congelo.places[5].name + ".jpg"
        else:
            self.root.ids['congelo_screen'].ids["p6_image"].source = "Images/CookStock/white.png"
        if (len(self.congelo.places) >= 7):
            self.root.ids['congelo_screen'].ids["p7_image"].source = "Images/CookStock/Aliments/" + self.congelo.places[6].name + ".jpg"
        else:
            self.root.ids['congelo_screen'].ids["p7_image"].source = "Images/CookStock/white.png"
        if (len(self.congelo.places) >= 8):
            self.root.ids['congelo_screen'].ids["p8_image"].source = "Images/CookStock/Aliments/" + self.congelo.places[7].name + ".jpg"
        else:
            self.root.ids['congelo_screen'].ids["p8_image"].source = "Images/CookStock/white.png"
        if (len(self.congelo.places) >= 9):
            self.root.ids['congelo_screen'].ids["p9_image"].source = "Images/CookStock/Aliments/" + self.congelo.places[8].name + ".jpg"
        else:
            self.root.ids['congelo_screen'].ids["p9_image"].source = "Images/CookStock/white.png"
        if (len(self.congelo.places) >= 10):
            self.root.ids['congelo_screen'].ids["p10_image"].source = "Images/CookStock/Aliments/" + self.congelo.places[9].name + ".jpg"
        else:
            self.root.ids['congelo_screen'].ids["p10_image"].source = "Images/CookStock/white.png"
        if (len(self.congelo.places) >= 11):
            self.root.ids['congelo_screen'].ids["p11_image"].source = "Images/CookStock/Aliments/" + self.congelo.places[10].name + ".jpg"
        else:
            self.root.ids['congelo_screen'].ids["p11_image"].source = "Images/CookStock/white.png"
        if (len(self.congelo.places) >= 12):
            self.root.ids['congelo_screen'].ids["p12_image"].source = "Images/CookStock/Aliments/" + self.congelo.places[11].name + ".jpg"
        else:
            self.root.ids['congelo_screen'].ids["p12_image"].source = "Images/CookStock/white.png"
        if (len(self.congelo.places) >= 13):
            self.root.ids['congelo_screen'].ids["p13_image"].source = "Images/CookStock/Aliments/" + self.congelo.places[12].name + ".jpg"
        else:
            self.root.ids['congelo_screen'].ids["p13_image"].source = "Images/CookStock/white.png"
        if (len(self.congelo.places) >= 14):
            self.root.ids['congelo_screen'].ids["p14_image"].source = "Images/CookStock/Aliments/" + self.congelo.places[13].name + ".jpg"
        else:
            self.root.ids['congelo_screen'].ids["p14_image"].source = "Images/CookStock/white.png"
        if (len(self.congelo.places) >= 15):
            self.root.ids['congelo_screen'].ids["p15_image"].source = "Images/CookStock/Aliments/" + self.congelo.places[14].name + ".jpg"
        else:
            self.root.ids['congelo_screen'].ids["p15_image"].source = "Images/CookStock/white.png"
        if (len(self.congelo.places) >= 16):
            self.root.ids['congelo_screen'].ids["p16_image"].source = "Images/CookStock/Aliments/" + self.congelo.places[15].name + ".jpg"
        else:
            self.root.ids['congelo_screen'].ids["p16_image"].source = "Images/CookStock/white.png"
        if (len(self.congelo.places) >= 17):
            self.root.ids['congelo_screen'].ids["p17_image"].source = "Images/CookStock/Aliments/" + self.congelo.places[16].name + ".jpg"
        else:
            self.root.ids['congelo_screen'].ids["p17_image"].source = "Images/CookStock/white.png"
        if (len(self.congelo.places) >= 18):
            self.root.ids['congelo_screen'].ids["p18_image"].source = "Images/CookStock/Aliments/" + self.congelo.places[17].name + ".jpg"
        else:
            self.root.ids['congelo_screen'].ids["p18_image"].source = "Images/CookStock/white.png"
        if (len(self.congelo.places) >= 19):
            self.root.ids['congelo_screen'].ids["p19_image"].source = "Images/CookStock/Aliments/" + self.congelo.places[18].name + ".jpg"
        else:
            self.root.ids['congelo_screen'].ids["p19_image"].source = "Images/CookStock/white.png"
        if (len(self.congelo.places) >= 20):
            self.root.ids['congelo_screen'].ids["p20_image"].source = "Images/CookStock/Aliments/" + self.congelo.places[19].name + ".jpg"
        else:
            self.root.ids['congelo_screen'].ids["p20_image"].source = "Images/CookStock/white.png"
        if (len(self.congelo.places) >= 21):
            self.root.ids['congelo_screen'].ids["p21_image"].source = "Images/CookStock/Aliments/" + self.congelo.places[20].name + ".jpg"
        else:
            self.root.ids['congelo_screen'].ids["p21_image"].source = "Images/CookStock/white.png"
        if (len(self.congelo.places) >= 22):
            self.root.ids['congelo_screen'].ids["p22_image"].source = "Images/CookStock/Aliments/" + self.congelo.places[21].name + ".jpg"
        else:
            self.root.ids['congelo_screen'].ids["p22_image"].source = "Images/CookStock/white.png"
        if (len(self.congelo.places) >= 23):
            self.root.ids['congelo_screen'].ids["p23_image"].source = "Images/CookStock/Aliments/" + self.congelo.places[22].name + ".jpg"
        else:
            self.root.ids['congelo_screen'].ids["p23_image"].source = "Images/CookStock/white.png"
        if (len(self.congelo.places) >= 24):
            self.root.ids['congelo_screen'].ids["p24_image"].source = "Images/CookStock/Aliments/" + self.congelo.places[23].name + ".jpg"
        else:
            self.root.ids['congelo_screen'].ids["p24_image"].source = "Images/CookStock/white.png"

x = MainApp()
x.run()