from random import randint, choices
import requests

class Generator :
    def __init__(self) :
        pass
    def num_phone(self) :
        id_list = ["06", "07"]
        id_probas = [.70, .30]
        id = choices(id_list, id_probas)


    def getImage(self):
        f = open("",'wb')
        f.write(requests.get('https://thispersondoesnotexist.com/image', headers={'User-Agent': 'My User Agent 1.0'}).content)
        f.close()
