import tkinter
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


        self.canvas = tkinter.Canvas(
            self.root,
            bg = "#203349",
            height = 326,
            width = 555,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        self.entry_image_1 = tkinter.PhotoImage(
            file=relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(
            151.5,
            121.0,
            image=self.entry_image_1
        )
        self.entry_1 = tkinter.Entry(
            bd=0,
            bg="#FFFFFF",
            highlightthickness=0
        )
        self.entry_1.place(
            x=83.0,
            y=111.0,
            width=137.0,
            height=18.0
        )

        self.entry_image_2 = tkinter.PhotoImage(
            file=relative_to_assets("entry_2.png"))
        self.entry_bg_2 = self.canvas.create_image(
            151.5,
            99.0,
            image=self.entry_image_2
        )
        self.entry_2 = tkinter.Entry(
            bd=0,
            bg="#FFFFFF",
            highlightthickness=0
        )
        self.entry_2.place(
            x=83.0,
            y=89.0,
            width=137.0,
            height=18.0
        )

        self.canvas.create_text(
            13.0,
            89.0,
            anchor="nw",
            text="Prénom :\n",
            fill="#FFFFFF",
            font=("Inter", 14 * -1)
        )

        self.canvas.create_text(
            13.0,
            111.0,
            anchor="nw",
            text="Métier :",
            fill="#FFFFFF",
            font=("Inter", 14 * -1)
        )

        self.image_image_1 = tkinter.PhotoImage(
            file=relative_to_assets("image_1.png"))
        self.connimage_1 = self.canvas.create_image(
            152.0,
            31.0,
            image=self.image_image_1
        )

        self.button_image_1 = tkinter.PhotoImage(
            file=relative_to_assets("button_1.png"))
        self.button_1 = tkinter.Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.changeImage(None),
            relief="flat"
        )
        self.button_1.place(
            x=440.0,
            y=290.0,
            width=102.0,
            height=23.0
        )

        self.image_image_2 = tkinter.PhotoImage(
            file=relative_to_assets("image_2.png"))
        self.image_2 = self.canvas.create_image(
            490.0,
            73.0,
            image=self.image_image_2
        )
        self.root.mainloop()

    def changeImage(self, e):
        self.getImage()
        self.image_image_2 = tkinter.PhotoImage(file=relative_to_assets("identityImage.png"))
        self.image_2 = self.canvas.create_image(
        490.0,
        73.0,
        image=self.image_image_2)
  





if __name__ == "__main__":
    main()
    