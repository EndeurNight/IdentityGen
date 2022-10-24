import tkinter
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

from scripts.BaseDeDonnees import BaseDeDonnees
from scripts.Generator import Generator
from scripts.Convert import Convert
from pathlib import Path

"""figd_x7RI6RIJEAKFF75aS00IaDkivLUrvAl61IidC_Lx""" #unique figma token

"""figd_tfu8hIrJnOs2JiudjbuqX9k9Bp-VrHANXEhb7uLM""" #second

OUTPUT_PATH = Path(__file__).parent

ASSETS_PATH = OUTPUT_PATH / Path("./assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class main(BaseDeDonnees, Generator):
    
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title("IdentiyGen (stable) public build 22621.674")
        self.root.iconbitmap("logo_ico.ico")
        self.root.resizable(False, False)
        self.root.geometry("800x432")
        self.root.configure(bg = "#1B2F47")    



        self.firstname = tkinter.StringVar()
        self.job = tkinter.StringVar()
        self.age = tkinter.IntVar()
        self.ville = tkinter.StringVar()
        self.codePostal = tkinter.StringVar()

        self.database =BaseDeDonnees('data/database.db')


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

    def changeImage(self):
        self.getImage()
        self.image_image_2 = tkinter.PhotoImage(file=relative_to_assets("identityImage.png"))
        self.image_2 = self.canvas.create_image(
        717,
        81,
        image=self.image_image_2)

    def refresh_image(self):
        print("Rafraichissement de l'image...")
        try :
            self.changeImage()
        except :
            print("Erreur lors du rafraichissement de l'image")
        print("Image rafraichie !")
        

    def reGen(self):
        print("Rafraichissement des données...")
        try :
            self.changeImage()
            self.firstname.set(self.database.getRandomFirstName().split(";")[0])
            self.job.set(self.database.getRandomJob())
        except :
            print("Erreur lors du rafraichissement des données")
            self.firstname.set("Erreur")
            self.job.set("Erreur")
        print("Données rafraichies !")


    def convertToPdf(self):
        infos = {"prenom":self.firstname.get(), "job":self.job.get()}


        Convert("Identity_Gen_Card.pdf", infos).convert()
    
    def download_image(self) :
        print("Téléchargement de l'image...")
    
    def download_data(self) :
        print("Téléchargement des données...")

    
  





if __name__ == "__main__":
    main()
    