from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

def show_about_window() :
        #Affiche la fenêtre "A propos"
        
        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path("./assets_about")


        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)


        window = Tk()

        window.geometry("445x445")
        window.resizable(0, 0)
        window.configure(bg = "#1B2F47")
        window.title("À propos d'IdentityGen")

        #Normalement, ça centre la fenêtre au milieu de l'écran
        window.eval('tk::PlaceWindow . center')

        canvas = Canvas(
        window,
        bg = "#1B2F47",
        height = 445,
        width = 445,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
        )

        canvas.place(x = 0, y = 0)


        #Texte
        image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
        image_1 = canvas.create_image(
        222.0,
        372.0,
        image=image_image_1
        )

        #Bannière de texte
        image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
        image_2 = canvas.create_image(
        219.0,
        292.0,
        image=image_image_2
        )

        #Logo IG
        image_image_3 = PhotoImage(
        file=relative_to_assets("image_3.png"))
        image_3 = canvas.create_image(
        227.0,
        150.0,
        image=image_image_3
        )

        
        window.resizable(False, False)
        window.mainloop()

def test():
        print("test")

if __name__ == "__main__":
    test()
    show_about_window()

