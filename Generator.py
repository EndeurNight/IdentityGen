from random import randint, choices
from PIL import Image;
import requests
from datetime import date



class Generator :
    

    def __init__(self) :
        pass
    def naissance(self) :
        "Fonction qui retourne une date de naissance aléatoire, sous forme : jour, mois, année de naissance, âge (en années) actuel"
        
        today = date.today()


        #on génère l'année de naissance en partant du principe que la personne est âgée de 18 à 90 ans
        annee_naissance = randint(today.year - 90, today.year - 18)

        #on prend l'année actuelle
        actual_year = today.year

        #on génère le mois de naissance
        mois_naissance = randint(1, 12)

        #on génère le jour de naissance
        if mois_naissance in [1, 3, 5, 7, 8, 10, 12] :
            jour_naissance = randint(1, 31)
        elif mois_naissance in [4, 6, 9, 11] :
            jour_naissance = randint(1, 30)
        else :
            jour_naissance = randint(1, 28)

        #on calcule l'âge de la personne
        age = today.year - annee_naissance - ((today.month, today.day) < (mois_naissance, jour_naissance))

        print("La personne est né(e) le " + str(jour_naissance) + "/" + str(mois_naissance) + "/" + str(annee_naissance) + " et a " + str(age) + " ans.")

        return jour_naissance, mois_naissance, annee_naissance, age

    def num_phone(self,mode) :
        if mode == "portable" :
            id_list = ["06", "07"]
            id_probas = [.60, .40]
        elif mode == "fixe" :
            id_list = ["01", "02", "03", "04", "05", "09"]
            id_probas = [.20, .20, .20, .10, .10, .20]
        else :
            print("Erreur : mode de numéro de téléphone incorrect")
            return None
        
        id = choices(id_list, id_probas)
        num = str(id[0])
        for i in range (0, 8) :
            num += str(randint(1, 9))
        return num

    def getImage(self):
        f = open("./data/identityImage.jfif",'wb')
        f.write(requests.get('https://thispersondoesnotexist.com/image', headers={'User-Agent': 'My User Agent 1.0'}).content)
        f.close()
        image = Image.open("./data/identityImage.jfif")
        image = image.convert("RGBA")
        image = image.resize((102, 102))
        image.save("./data/identityImage.png")

    def security_number(sexe, annee_naissance, mois):
        pass

#on teste la classe
gen = Generator()
print(gen.naissance())
print(gen.num_phone("portable"))
print(gen.num_phone("fixe"))
