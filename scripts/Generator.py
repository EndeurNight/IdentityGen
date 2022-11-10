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

        if mois_naissance < 10 :
            temp = "0" + str(mois_naissance)
            mois_naissance = int(temp)

        #on génère le jour de naissance
        if mois_naissance in [1, 3, 5, 7, 8, 10, 12] :
            jour_naissance = randint(1, 31)
        elif mois_naissance in [4, 6, 9, 11] :
            jour_naissance = randint(1, 30)
        else :
            jour_naissance = randint(1, 28)

        #on calcule l'âge de la personne
        age = today.year - annee_naissance - ((today.month, today.day) < (mois_naissance, jour_naissance))

        #print("La personne est né(e) le " + str(jour_naissance) + "/" + str(mois_naissance) + "/" + str(annee_naissance) + " et a " + str(age) + " ans.")

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

        #on crée une version du numéro de téléphone avec des tirets
        num_tirets = num[0:2] + " " + num[2:4] + " " + num[4:6] + " " + num[6:8] + " " + num[8:10]
        #on crée une version avec l'identifiant du pays
        num_international = "+33" + num[1:10]
        #on crée une version avec l'identifiant du pays et des espaces
        num_international_espaces = "+33 " + num[1:2] + " " + num[2:4] + " " + num[4:6] + " " + num[6:8] + " " + num[8:10]
        return num, num_tirets, num_international, num_international_espaces

    def getImage(self):
        return self.getImageProcess()
        
    def getImageProcess(self):
        '''Fonction qui retourne une image aléatoire. J'ai du la séparer pour pouvoir utiliser les mesures de temps sur les threads'''
        f = open("./assets/identityImage.jfif",'wb')
        f.write(requests.get('https://thispersondoesnotexist.com/image', headers={'User-Agent': 'My User Agent 1.0'}).content)
        f.close()
        image = Image.open("./assets/identityImage.jfif")
        image = image.convert("RGBA")
        image = image.resize((150, 150))    
        image.save("./assets/identityImage.png")

    def security_number(self, sexe, annee_naissance, mois):
        """Pour l'instant, le numéro est généré de manière pseudo-aléatoire.
        Le modèle de génération est correct pour les 5 premiers chiffres mais est complété de manière aléatoire par Python, 
        car IdentityGen ne gère pas dans la version actuelle le lieu de naissance.
        La complétion automatique garde toutefois une certaine coordance ; les numéros sont possibles et ne prennent pas de valeurs inexistantes.
        1er chiffre = sexe ("H" = Homme, "F" = Femme)
        2 chiffres suivants = année de naissance
        2 chiffres suivants = mois de naissance
        2 chiffres suivants = département (GENERE)
        3 chiffres suivants = code commune INSEE (GENERE)
        3 chiffres suivants = numéro d'ordre de naissance
        2 chiffres suivants = Clé de contrôle
        Total = 1 + 2 + 2 + 2 + 3 + 3 + 2 = 15 chiffres
        """

        assert sexe in ["H", "F"], "Erreur : sexe incorrect"
        assert annee_naissance >= 1900 and annee_naissance <= date.today().year, "Erreur : année de naissance incorrecte"
        assert mois >= 1 and mois <= 12, "Erreur : mois de naissance incorrect" 

        #on génère le numéro de sécurité sociale
        num = ""

        #1er chiffre = sexe ("H" = Homme, "F" = Femme)
        if sexe == "H" :
            num += "1"
        elif sexe == "F" :
            num += "2"
        else :
            print("Erreur : sexe incorrect")
            return None
        
        #2 chiffres suivants = année de naissance
        annee_de_naissance = str(annee_naissance)
        num += str(annee_de_naissance[2])
        num += str(annee_de_naissance[3])

        #2 chiffres suivants = mois de naissance
        if mois < 10 :
            num += "0"
        num += str(mois)

        #2 chiffres suivants = département (GENERE)
        #Les départements vont de 01 à 99, mais 20, 96, 97 et 98 ne sont pas utilisés
        departement = randint(1, 99)
        if departement == 20 or departement == 96 or departement == 97 or departement == 98 :
            departement += 1
        if departement < 10 :
            num += "0"
        num += str(departement)

        #3 chiffres suivants = code commune INSEE (GENERE)
        #Les codes communes INSEE vont de 001 à 999
        code_commune = randint(1, 999)
        if code_commune < 10 :
            num += "00"
        elif code_commune < 100 :
            num += "0"
        num += str(code_commune)

        #3 chiffres suivants = numéro d'ordre de naissance
        #Les numéros d'ordre de naissance vont de 001 à 999
        num_ordre = randint(1, 999)
        if num_ordre < 10 :
            num += "00"
        elif num_ordre < 100 :
            num += "0"
        num += str(num_ordre)


        #2 chiffres suivants = Clé de contrôle
        #formule de Luhn
        cle = 97 - (int(num) % 97)
        if cle < 10 :
            num += "0"
        num += str(cle)

        num_avec_espaces = num[0:1] + " " + num[1:3] + " " + num[3:5] + " " + num[5:7] + " " + num[7:10] + " " + num[10:13] + " " + num[13:15]

        return num, num_avec_espaces
    
    def email(self, prenom, nom) :
        """Cette fonction génère un email aléatoire."""
        #liste des fournisseurs d'email les plus courants
        fournisseurs_tiers = ["online.de", "alice.it", "virgilio.it", "tin.it", "tim.it", "aol.com", "aol.fr", "me.com", "mac.com", "icloud.com", "arcor.de", "bluewin.ch", "blueyonder.co.uk", "bbox.fr", "btinternet.com", "comcast.net", "email.it", "facebook.com", "free.fr", "aliceadsl.fr", "infonie.fr", "libertysurf.fr", "online.fr", "freesbee.fr", "alicepro.fr", "worldonline.fr", "freenet.de", "gmx.de", "gmx.net", "gmx.at", "caramail.com", "gmx.fr", "gmail.com", "googlemail.com", "home.nl", "laposte.net", "libero.it", "blu.it", "giallo.it", "mail.ru", "bk.ru", "hotmail.com", "live.com", "msn.com", "outlook.com", "windowslive", "dbmail.com", "hotmail.fr", "live.fr", "msn.fr", "hotmail.be", "msn.be", "live.be", "hotmail.de", "hotmail.it", "hotmail.co.uk", "hotmail.es", "live.co.uk", "live.it", "live.nl", "live.se", "live.de", "hotmail.nl", "outlook.fr", "hotmail.se", "live.dk", "live.com.pt", "telefonica.es", "movistar.es", "numericable.fr", "noos.fr", "o2.pl", "orange.fr", "wanadoo.fr", "skynet.be", "rambler.ru", "lenta.ru", "autorambler.ru", "myrambler.ru", "ro.ru", "r0.ru", "sfr.fr", "neuf.fr", "9online.fr", "9business.fr", "cegetel.net", "club-internet.fr", "cario.fr", "guideo.fr", "mageos.com", "fnac.net", "waika9.com", "sky.com", "telenet.be", "tiscali.it", "tiscali.co.uk", "t-online.de", "verizon.net", "ono.com", "voila.fr", "web.de", "wp.pl", "yahoo.com", "ymail", "rocketmail", "yahoo.fr", "yahoo.co.uk", "yahoo.es", "yahoo.de", "yahoo.it", "ymail.com", "yahoo.com.tw", "rocketmail.com", "yahoo.se", "yandex.ru", "mail.com", "talktalk.net"]
        fournisseurs_classiques = ["gmail.com","outlook.fr","gmail.fr", "outlook.fr"]
        #on génère un mail aléatoire
        mode_aleatoire = randint(0, 1)
        #Si mode aléatoire = 0, alors on a le modèle prenom-nom
        #Sinon, nom-prenom (ça permet de donner un peu de variété)
        if mode_aleatoire == 0 :
            mail = ""
            mail += prenom.lower()
            separateur = ["", ".", "_", "-", ""]
            mail += separateur[randint(0, 4)]
            mail += nom.lower()
        else :
            mail = ""
            mail += nom.lower()
            separateur = ["", ".", "_", "-", ""]
            mail += separateur[randint(0, 4)]
            mail += prenom.lower()
        
        mail += "@"
        #on choisit un fournisseur d'email aléatoire entre les deux listes
        probabilites = [0.6, 0.4]
        choix = choices([0, 1], probabilites)[0]
        if choix == 0 :
            mail += fournisseurs_classiques[randint(0, len(fournisseurs_classiques) - 1)]
        else :
            mail += fournisseurs_tiers[randint(0, len(fournisseurs_tiers) - 1)]

        return mail

    def carte_bancaire(self) :
            """Cette fonction génère un numéro de carte bancaire aléatoire."""
            #on génère un numéro de carte bancaire aléatoire
            num = ""	
            #le premier chiffre est le numéro de la banque. En france, il y a 3 grands réseaux de cartes bancaires : Visa, Mastercard et American Express
            #on choisit un réseau aléatoirement
            reseau = ["3", "4", "5"]
            num += reseau[randint(0, 2)]
            #on génère ensuite les 5 chiffres de la banque de manière aléatoire (il faudrait vérifier que le numéro de banque existe, mais c'est trop compliqué)
            for i in range(5) :
                num += str(randint(0, 9))

            #puis on génère les 10 derniers chiffres de manière aléatoire (on obtient donc un numéro de carte bancaire aléatoire, qui ne respecte pas forcément les règles de Luhn car on ne le vérifie pas.
            for i in range(10) :
                num += str(randint(0, 9))

            cvv = randint(100, 999)
            date = str(randint(1, 12)) + "/" + str(randint(21, 30))

            num_avec_espaces = ""
            for i in range(len(num)) :
                if i % 4 == 0 and i != 0 :
                    num_avec_espaces += " "
                num_avec_espaces += num[i]

            return num, cvv, date, num_avec_espaces
    
    def groupe_sanguin(self) :
        """Génère un groupe sanguin aléatoire"""
        groupe = ["A", "B", "AB", "O"]
        rh = ["+", "-"]
        g = groupe[randint(0, 3)] + rh[randint(0, 1)]
        return str(g)

    def signe_astro(self) :
        """on triche un peu trois fois rien"""
        signes = ["Bélier", "Taureau", "Gémeaux", "Cancer", "Lion", "Vierge", "Balance", "Scorpion", "Sagittaire", "Capricorne", "Verseau", "Poissons"]
        return signes[randint(0, 11)]
    
# #on teste la classe
# gen = Generator()
# id = gen.naissance()
# print(id)
# print(gen.num_phone("portable"))
# print(gen.num_phone("fixe"))
# print(gen.security_number("H", int(id[2]), int(id[1])))
# print(gen.email("B","Q"))
# print(gen.carte_bancaire())
# print(gen.groupe_sanguin())
# print(gen.signe_astro())