
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("555x326")
window.configure(bg = "#203349")


canvas = Canvas(
    window,
    bg = "#203349",
    height = 326,
    width = 555,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    157.5,
    153.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0
)
entry_1.place(
    x=89.0,
    y=143.0,
    width=137.0,
    height=18.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    157.5,
    131.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0
)
entry_2.place(
    x=89.0,
    y=121.0,
    width=137.0,
    height=18.0
)

canvas.create_text(
    19.0,
    121.0,
    anchor="nw",
    text="Prénom :\n",
    fill="#FFFFFF",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    19.0,
    143.0,
    anchor="nw",
    text="Métier :",
    fill="#FFFFFF",
    font=("Inter", 14 * -1)
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    207.0,
    55.0,
    image=image_image_1
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=446.0,
    y=292.0,
    width=101.0,
    height=25.0
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    497.0,
    61.0,
    image=image_image_2
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=534.0,
    y=121.0,
    width=10.833328247070312,
    height=11.818035125732422
)
window.resizable(False, False)
window.mainloop()
