from distutils import extension
from distutils.log import error
import tkinter
from pathlib import Path
from tkinter import Button, Canvas, Entry, PhotoImage, Text, Tk
from tkinter.filedialog import asksaveasfile
from scripts.BaseDeDonnees import BaseDeDonnees
from scripts.Convert import Convert
from scripts.Generator import Generator
from About import About
from rich.console import Console
from PIL import Image


"""figd_x7RI6RIJEAKFF75aS00IaDkivLUrvAl61IidC_Lx""" #unique figma token

"""figd_tfu8hIrJnOs2JiudjbuqX9k9Bp-VrHANXEhb7uLM""" #second

#Pas compris xD

OUTPUT_PATH = Path(__file__).parent

ASSETS_PATH = OUTPUT_PATH / Path("./assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

#on initialise la console (pour les print en couleurs)
console = Console()

class main(BaseDeDonnees, Generator):
    
    def __init__(self):

        #On initialise la fenêtre et tous ses composants
        self.root = tkinter.Tk()
        #Titre de la fenêtre
        self.root.title("IdentiyGen (stable) public build 2.16.4")
        #Logo de la fenêtre
        self.root.iconbitmap("logo_ico.ico")
        #Taille de la fenêtre (non redimensionnable)
        self.root.resizable(False, False)
        #self.root.geometry("800x432")
        self.root.geometry("800x445")
        #Couleur de fond
        self.root.configure(bg = "#1B2F47")

        #MENU 
        self.menu = tkinter.Menu(self.root)
        self.root.config(menu=self.menu)

        #about
        self.about = About()
        # self.about.test()
        # self.about.show_about_window()

        self.menuinfo = tkinter.Menu(self.menu, tearoff=0)
        self.menuinfo.add_command(label="Générer une nouvelle identité", command=self.reGen)
        self.menuinfo.add_command(label="Rafraichir l'image", command=self.refresh_image)
        #on ajoute un séparateur
        self.menuinfo.add_separator()
        self.menuinfo.add_command(label="Quitter", command=self.root.quit)
        self.menu.add_cascade(label="Application", menu=self.menuinfo)

        self.menu.add_cascade(label="À propos", command=self.about.test)


        


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
        


        self.canvas = Canvas(
            self.root,
            bg = "#1B2F47",
            height = 432,
            width = 800,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)

        entry_image_1 = PhotoImage(
            file=relative_to_assets("entry_1.png"))
        entry_bg_1 = self.canvas.create_image(
            449.0,
            238.5,
            image=entry_image_1
        )
        entry_1 = Entry(
            bd=0,
            bg="#FFFFFF",
            highlightthickness=0

        )
        entry_1.place(
            x=357.0,
            y=230.0,
            width=184.0,
            height=15.0
        )

        self.canvas.create_text(
            296.0,
            232.0,
            anchor="nw",
            text="Email :",
            fill="#FFFFFF",
            font=("Inter", 12 * -1)
        )

        entry_image_2 = PhotoImage(
            file=relative_to_assets("entry_2.png"))
        entry_bg_2 = self.canvas.create_image(
            418.5,
            208.5,
            image=entry_image_2
        )
        self.codepostal_entry = Entry(
            bd=0,
            bg="#FFFFFF",
            highlightthickness=0
        )
        self.codepostal_entry.place(
            x=395.0,
            y=200.0,
            width=47.0,
            height=15.0
        )

        self.canvas.create_text(
            296.0,
            202.0,
            anchor="nw",
            text="Code postal  :",
            fill="#FFFFFF",
            font=("Inter", 12 * -1)
        )

        entry_image_3 = PhotoImage(
            file=relative_to_assets("entry_3.png"))
        entry_bg_3 = self.canvas.create_image(
            203.5,
            238.5,
            image=entry_image_3
        )
        entry_3 = Entry(
            bd=0,
            bg="#FFFFFF",
            highlightthickness=0
        )
        entry_3.place(
            x=152.0,
            y=230.0,
            width=103.0,
            height=15.0
        )

        entry_image_4 = PhotoImage(
            file=relative_to_assets("entry_4.png"))
        entry_bg_4 = self.canvas.create_image(
            400.0,
            334.5,
            image=entry_image_4
        )
        entry_4 = Entry(
            bd=0,
            bg="#FFFFFF",
            highlightthickness=0
        )
        entry_4.place(
            x=358.0,
            y=326.0,
            width=84.0,
            height=15.0
        )

        self.canvas.create_text(
            17.0,
            232.0,
            anchor="nw",
            text="Date de naissance :",
            fill="#FFFFFF",
            font=("Inter", 12 * -1)
        )
        entry_image_5 = PhotoImage(
            file=relative_to_assets("entry_5.png"))
        entry_bg_5 = self.canvas.create_image(
            367.5,
            268.5,
            image=entry_image_5
        )
        entry_5 = Entry(
            bd=0,
            bg="#FFFFFF",
            highlightthickness=0
        )
        entry_5.place(
            x=194.0,
            y=260.0,
            width=347.0,
            height=15.0
        )

        self.canvas.create_text(
            17.0,
            262.0,
            anchor="nw",
            text="Numéro de sécurité sociale :",
            fill="#FFFFFF",
            font=("Inter", 12 * -1)
        )


        entry_image_6 = PhotoImage(
            file=relative_to_assets("entry_6.png"))
        entry_bg_6 = self.canvas.create_image(
            169.5,
            301.5,
            image=entry_image_6
        )
        entry_6 = Entry(
            bd=0,
            bg="#FFFFFF",
            highlightthickness=0
        )
        entry_6.place(
            x=84.0,
            y=293.0,
            width=171.0,
            height=15.0
        )

        image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        image_1 = self.canvas.create_image(
            36.0,
            299.0,
            image=image_image_1
        )
        entry_image_7 = PhotoImage(
            file=relative_to_assets("entry_7.png"))
        entry_bg_7 = self.canvas.create_image(
            186.5,
            333.5,
            image=entry_image_7
        )
        entry_7 = Entry(
            bd=0,
            bg="#FFFFFF",
            highlightthickness=0
        )
        entry_7.place(
            x=84.0,
            y=325.0,
            width=205.0,
            height=15.0
        )

        image_image_2 = PhotoImage(
            file=relative_to_assets("image_2.png"))
        image_2 = self.canvas.create_image(
            36.0,
            335.0,
            image=image_image_2
        )


        entry_image_8 = PhotoImage(
            file=relative_to_assets("entry_8.png"))
        entry_bg_8 = self.canvas.create_image(
            530.5,
            208.5,
            image=entry_image_8
        )
        entry_8 = Entry(
            bd=0,
            bg="#FFFFFF",
            highlightthickness=0
        )
        entry_8.place(
            x=520.0,
            y=200.0,
            width=21.0,
            height=15.0
        )

        self.canvas.create_text(
            467.0,
            202.0,
            anchor="nw",
            text="Âge :",
            fill="#FFFFFF",
            font=("Inter", 12 * -1)
        )

        entry_image_9 = PhotoImage(
            file=relative_to_assets("entry_9.png"))
        entry_bg_9 = self.canvas.create_image(
            526.5,
            333.5,
            image=entry_image_9
        )
        entry_9 = Entry(
            bd=0,
            bg="#FFFFFF",
            highlightthickness=0
        )
        entry_9.place(
            x=512.0,
            y=325.0,
            width=29.0,
            height=15.0
        )

        self.canvas.create_text(
            461.0,
            327.0,
            anchor="nw",
            text="CVV :",
            fill="#FFFFFF",
            font=("Inter", 12 * -1)
        )

        entry_image_10 = PhotoImage(
            file=relative_to_assets("entry_10.png"))
        entry_bg_10 = self.canvas.create_image(
            449.0,
            302.5,
            image=entry_image_10
        )
        entry_10 = Entry(
            bd=0,
            bg="#FFFFFF",
            highlightthickness=0
        )
        entry_10.place(
            x=356.0,
            y=294.0,
            width=186.0,
            height=15.0
        )

        entry_image_11 = PhotoImage(
            file=relative_to_assets("entry_11.png"))
        entry_bg_11 = self.canvas.create_image(
            449.0,
            302.5,
            image=entry_image_11
        )
        entry_11 = Entry(
            bd=0,
            bg="#FFFFFF",
            highlightthickness=0
        )
        entry_11.place(
            x=356.0,
            y=294.0,
            width=186.0,
            height=15.0
        )

        image_image_3 = PhotoImage(
            file=relative_to_assets("image_3.png"))
        image_3 = self.canvas.create_image(
            311.0,
            301.0,
            image=image_image_3
        )

        image_image_4 = PhotoImage(
            file=relative_to_assets("image_4.png"))
        image_4 = self.canvas.create_image(
            323.0,
            333.0,
            image=image_image_4
        )

        entry_image_12 = PhotoImage(
            file=relative_to_assets("entry_12.png"))
        entry_bg_12 = self.canvas.create_image(
            166.72222137451172,
            208.5,
            image=entry_image_12
        )
        entry_12 = Entry(
            bd=0,
            bg="#FFFFFF",
            highlightthickness=0
        )
        entry_12.place(
            x=78.44444274902344,
            y=200.0,
            width=176.55555725097656,
            height=15.0
        )

        self.canvas.create_text(
            17.0,
            202.0,
            anchor="nw",
            text="Ville :",
            fill="#FFFFFF",
            font=("Inter", 12 * -1)
        )

        entry_image_13 = PhotoImage(
            file=relative_to_assets("entry_13.png"))
        entry_bg_13 = self.canvas.create_image(
            529.0,
            180.5,
            image=entry_image_13
        )
        entry_13 = Entry(
            bd=0,
            bg="#FFFFFF",
            highlightthickness=0
        )
        entry_13.place(
            x=517.0,
            y=172.0,
            width=24.0,
            height=15.0
        )

        self.canvas.create_text(
            398.0,
            172.0,
            anchor="nw",
            text="Groupe sanguin :",
            fill="#FFFFFF",
            font=("Inter", 12 * -1)
        )

        entry_image_14 = PhotoImage(
            file=relative_to_assets("entry_14.png"))
        entry_bg_14 = self.canvas.create_image(
            362.5,
            180.5,
            image=entry_image_14
        )
        entry_14 = Entry(
            bd=0,
            bg="#FFFFFF",
            highlightthickness=0
        )
        entry_14.place(
            x=355.0,
            y=172.0,
            width=15.0,
            height=15.0
        )

        self.canvas.create_text(
            296.0,
            172.0,
            anchor="nw",
            text="Sexe :",
            fill="#FFFFFF",
            font=("Inter", 12 * -1)
        )

        entry_image_15 = PhotoImage(
            file=relative_to_assets("entry_15.png"))
        entry_bg_15 = self.canvas.create_image(
            169.5,
            180.5,
            image=entry_image_15
        )
        entry_15 = Entry(
            bd=0,
            bg="#FFFFFF",
            highlightthickness=0
        )
        entry_15.place(
            x=84.0,
            y=172.0,
            width=171.0,
            height=15.0
        )

        self.canvas.create_text(
            17.0,
            174.0,
            anchor="nw",
            text="Métier :",
            fill="#FFFFFF",
            font=("Inter", 12 * -1)
        )

        entry_image_16 = PhotoImage(
            file=relative_to_assets("entry_16.png"))
        entry_bg_16 = self.canvas.create_image(
            449.6389923095703,
            146.5,
            image=entry_image_16
        )
        entry_16 = Entry(
            bd=0,
            bg="#FFFFFF",
            highlightthickness=0
        )
        entry_16.place(
            x=358.2779846191406,
            y=138.0,
            width=182.72201538085938,
            height=15.0
        )

        self.canvas.create_text(
            296.0,
            140.0,
            anchor="nw",
            text="Nom :",
            fill="#FFFFFF",
            font=("Inter", 12 * -1)
        )

        entry_image_17 = PhotoImage(
            file=relative_to_assets("entry_17.png"))
        entry_bg_17 = self.canvas.create_image(
            174.49998474121094,
            148.5,
            image=entry_image_17
        )
        entry_17 = Entry(
            bd=0,
            bg="#FFFFFF",
            highlightthickness=0
        )
        entry_17.place(
            x=93.99999237060547,
            y=140.0,
            width=160.99998474121094,
            height=15.0
        )

        self.canvas.create_text(
            17.0,
            142.0,
            anchor="nw",
            text="Prénom :\n",
            fill="#FFFFFF",
            font=("Inter", 12 * -1)
        )

        image_image_5 = PhotoImage(
            file=relative_to_assets("image_5.png"))
        image_5 = self.canvas.create_image(
            270.0,
            63.0,
            image=image_image_5
        )

        image_image_6 = PhotoImage(
            file=relative_to_assets("image_6.png"))
        image_6 = self.canvas.create_image(
            718.0,
            82.0,
            image=image_image_6
        )

        ######################## Zone des boutons ########################

        button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.download_image(),
            relief="flat"
        )
        button_1.place(
            x=208.0,
            y=379.0,
            width=175.0,
            height=40.0
        )

        button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.download_data(),
            relief="flat"
        )
        button_2.place(
            x=17.0,
            y=379.0,
            width=175.0,
            height=40.0
        )

        button_image_3 = PhotoImage(
            file=relative_to_assets("button_3.png"))
        button_3 = Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.reGen(),
            relief="flat"
        )
        button_3.place(
            x=647.0,
            y=348.0,
            width=137.0,
            height=61.0
        )

        button_image_4 = PhotoImage(
            file=relative_to_assets("button_4.png"))
        button_4 = Button(
            image=button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.refresh_image(),
            relief="flat"
        )
        button_4.place(
            x=618.0,
            y=10.0,
            width=16.0,
            height=21.0
        )
        self.root.mainloop()

    ######################## Zone des fonctions ########################

    def changeImage(self):
        self.getImage()
        self.image_image_2 = tkinter.PhotoImage(file=relative_to_assets("identityImage.png"))
        self.image_2 = self.canvas.create_image(
        717,
        81,
        image=self.image_image_2)

    def refresh_image(self):
        console.print("Rafraichissement de l'image...", style="blue")
        try :
            self.changeImage()
            console.print("Image rafraichie !", style="green")
        except Exception as e:
            console.print("Erreur lors du rafraichissement de l'image", style="red")
            console.print(e, style="red")
        return
        

    def reGen(self):
        console.print("\nGénération des données...", style="bold purple")

        #On génère l'image
        console.print("Génération de l'image...", style="blue")
        try :
            self.changeImage()
            console.print("Image générée !", style="green")
        except Exception as e:
            console.print("Erreur lors du rafraichissement de l'image", style="red")
            console.print(e, style="red")

        #On génère le prénom
        console.print("Génération du prénom...", style="blue")
        try :
            console.print("Prénom : [u]" + str(self.database.getRandomFirstName().split(";")[0]) + "[/u]", style="green") 
            console.print("Prénom généré !", style="green")
        except Exception as e:
            console.print("Erreur lors de la génération du prénom", style="red")
            console.print(e, style="red")
        
        #On génère le métier
        console.print("Génération du métier...", style="blue")
        try :
            console.print("Métier : [u]" + str(self.database.getRandomJob().split(";")[0]) + "[/u]", style="green")
            console.print("Métier généré !", style="green")
        except Exception as e:
            console.print("Erreur lors de la génération du métier", style="red")
            console.print(e, style="red")

        console.print("Génération terminée.", style="bold green")

    def about(self):
        #on affiche la fenêtre à propos
        console.print("Ouverture de la fenêtre à propos...", style="blue")
        self.about()


    def convertToPdf(self):
        infos = {"prenom":self.firstname.get(), "job":self.job.get()}
        Convert("Identity_Gen_Card.pdf", infos).convert()
    
    def download_image(self) :

        console.print("Préparation de l'image...", style="blue")
        console.print("Recadrage et conversion de l'image...", style="blue")
        try :
            image = Image.open("./assets/identityImage.jfif")
            image_export = image.convert("RGBA")
            image_export.save("./assets/identityImageExport.png")
            console.print("Image convertie avec succès...", style="green")
        except Exception as e:
            console.print("Erreur lors de la conversion de l'image", style="red")
            console.print(e, style="red")
            return
        console.print("Téléchargement de l'image... \n {A CONTINUER}", style="yellow")

        # #on demande à l'utilisateur où il veut enregistrer l'image sur son ordinateur
        # extensions = [('Image PNG ', '*.png')]
        # #On demande à l'utilisateur où il veut enregistrer l'image identityImageExport.png
        # downloaded_image = asksaveasfile(filetypes = extension, defaultextension = extension)

        # f = open(downloaded_image,'wb')
        # f.write(self.image_image_2)
        # f.close()
        
    def download_data(self) :
        console.print("Téléchargement des données... \n {A CONTINUER}", style="yellow")

    
  





if __name__ == "__main__":
    console.print("Démarrage de l'application...\n\n", style="bold blue")
    main()
    