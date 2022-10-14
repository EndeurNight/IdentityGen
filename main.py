import tkinter
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

from matplotlib.pyplot import text
from BaseDeDonnees import BaseDeDonnees
from Generator import Generator
from pathlib import Path

"""figd_x7RI6RIJEAKFF75aS00IaDkivLUrvAl61IidC_Lx""" #unique figma token
OUTPUT_PATH = Path(__file__).parent

ASSETS_PATH = OUTPUT_PATH / Path("./data")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class main(BaseDeDonnees, Generator):
    
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title("Main")
        self.root.resizable(False, False)


        self.root.geometry("555x326")
        self.root.configure(bg = "#203349")


        self.firstname = tkinter.StringVar()
        self.job = tkinter.StringVar()
        self.age = tkinter.IntVar()
        self.ville = tkinter.StringVar()
        self.codePostal = tkinter.StringVar()

        self.database =BaseDeDonnees('data/database.db')


        self.canvas = Canvas(
            self.root,
            bg = "#203349",
            height = 326,
            width = 555,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        self.entry_image_1 = PhotoImage(
            file=relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(
            157.5,
            153.0,
            image=self.entry_image_1
        )
        self.entry_1 = Entry(
            bd=0,
            bg="#FFFFFF",
            highlightthickness=0,
            textvariable=self.job
        )
        self.entry_1.place(
            x=89.0,
            y=143.0,
            width=137.0,
            height=18.0
        )

        self.entry_image_2 = PhotoImage(
            file=relative_to_assets("entry_2.png"))
        self.entry_bg_2 = self.canvas.create_image(
            157.5,
            131.0,
            image=self.entry_image_2
        )
        self.entry_2 = Entry(
            bd=0,
            bg="#FFFFFF",
            highlightthickness=0,
            textvariable=self.firstname
        )
        self.entry_2.place(
            x=89.0,
            y=121.0,
            width=137.0,
            height=18.0
        )

        self.canvas.create_text(
            19.0,
            121.0,
            anchor="nw",
            text="Prénom :\n",
            fill="#FFFFFF",
            font=("Inter", 14 * -1)
        )

        self.canvas.create_text(
            19.0,
            143.0,
            anchor="nw",
            text="Métier :",
            fill="#FFFFFF",
            font=("Inter", 14 * -1)
        )

        self.image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(
            207.0,
            55.0,
            image=self.image_image_1
        )

        self.button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.reGen(None),
            relief="flat"
        )
        self.button_1.place(
            x=446.0,
            y=292.0,
            width=101.0,
            height=25.0
        )

        self.image_image_2 = PhotoImage(
            file=relative_to_assets("image_2.png"))
        self.image_2 = self.canvas.create_image(
            497.0,
            61.0,
            image=self.image_image_2
        )

        self.button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        self.button_2 = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.changeImage(),
            relief="flat"
        )
        self.button_2.place(
            x=534.0,
            y=121.0,
            width=10.833328247070312,
            height=11.818035125732422
        )
        self.root.mainloop()

    def changeImage(self):
        self.getImage()
        self.image_image_2 = tkinter.PhotoImage(file=relative_to_assets("identityImage.png"))
        self.image_2 = self.canvas.create_image(
        490.0,
        73.0,
        image=self.image_image_2)
        

    def reGen(self,e):
        self.changeImage()
        self.firstname.set(self.database.getRandomFirstName().split(";")[0])
        self.job.set(self.database.getRandomJob())

    
  





if __name__ == "__main__":
    main()
    