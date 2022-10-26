#On initialise la fenêtre et tous ses composants
self.root = tkinter.Tk()
#Titre de la fenêtre
self.root.title("IdentiyGen (stable) public build 22621.674")
#Logo de la fenêtre
self.root.iconbitmap("logo_ico.ico")
#Taille de la fenêtre (non redimensionnable)
self.root.resizable(False, False)
self.root.geometry("800x432")
#Couleur de fond
self.root.configure(bg = "#1B2F47")    

#Dans l'ordre des composants de la fenêtre ig (on part du design, de haut en bas et de gauche à droite)):

#Prénom
self.firstname = tkinter.StringVar()
#Nom
self.name = tkinter.StringVar()
#Métier
self.job = tkinter.StringVar()
#Sexe
self.sex = tkinter.StringVar()
#Groupe sanguin
self.blood = tkinter.StringVar()
#Ville
self.city = tkinter.StringVar()
#Code postal
self.postal_code = tkinter.StringVar()
#Age
self.age = tkinter.StringVar()
#Date de naissance
self.birth_date = tkinter.StringVar()
#Email
self.email = tkinter.StringVar()
#Numéro de sécurité sociale
self.social_security_number = tkinter.StringVar()
#Numéro de téléphone fixe
self.phone_number = tkinter.StringVar()
#Numéro de téléphone portable
self.mobile_phone_number = tkinter.StringVar()
#Numéro de carte bancaire
self.bank_card_number = tkinter.StringVar()
#Date d'expiration de la carte bancaire
self.bank_card_expiration_date = tkinter.StringVar()
#Code de sécurité de la carte bancaire
self.bank_card_security_code = tkinter.StringVar()

#On initialise la base de données
self.database = BaseDeDonnees('data/database.db')