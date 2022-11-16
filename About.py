from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Toplevel



class About:
        def __init__(self) -> None:
                self.OUTPUT_PATH = Path(__file__).parent
                self.ASSETS_PATH = self.OUTPUT_PATH / Path("./assets_about")



        def relative_to_assets(self, path: str) -> Path:
                return self.ASSETS_PATH / Path(path)

        def show_about_window(self, root) :
                #Affiche la fenêtre "A propos"              
                

                self.window = Toplevel(root)

                self.window.geometry("445x445")
                self.window.resizable(0, 0)
                self.window.configure(bg = "#1B2F47")
                self.window.title("À propos d'IdentityGen")

                # #Normalement, ça centre la fenêtre au milieu de l'écran
                # window.eval('tk::PlaceWindow . center')

                self.canvas = Canvas(
                self.window,
                bg = "#1B2F47",
                height = 445,
                width = 445,
                bd = 0,
                highlightthickness = 0,
                relief = "ridge"
                )

                self.canvas.place(x = 0, y = 0)


                #Texte
                image_image_1 = PhotoImage(
                file=("./assets_about/image_1.png"), master=root)

                image_1 = self.canvas.create_image(
                222.0,
                372.0,
                image=image_image_1
                )

                #Bannière de texte
                image_image_2 = PhotoImage(
                file=("./assets_about/image_2.png"), master=root)
                image_2 = self.canvas.create_image(
                219.0,
                292.0,
                image=image_image_2
                )

                #Logo IG
                image_image_3 = PhotoImage(
                file=("./assets_about/image_3.png"), master=root)
                image_3 = self.canvas.create_image(
                227.0,
                150.0,
                image=image_image_3
                )

                self.window.mainloop()


                