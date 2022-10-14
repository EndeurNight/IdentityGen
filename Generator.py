from random import randint, choices
from PIL import Image;
import requests



class Generator :
    

    def __init__(self) :
        pass
    def naissance(self) :
        age = randint(20, 80)
        date = currentDateTime.date()
        year = date.strftime("%Y")


    def num_phone(self) :
        id_list = ["06", "07"]
        id_probas = [.70, .30]
        id = choices(id_list, id_probas)
    def getImage(self):
        f = open("./data/identityImage.jfif",'wb')
        f.write(requests.get('https://thispersondoesnotexist.com/image', headers={'User-Agent': 'My User Agent 1.0'}).content)
        f.close()
        image = Image.open("./data/identityImage.jfif")
        image = image.convert("RGBA")
        image = image.resize((102, 102))
        image.save("./data/identityImage.png")

    def security_number(sexe, annee_naissance, mois)
