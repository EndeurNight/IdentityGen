
def changeImage(e):
    global image_image_2, image_2
    image = Image.open(relative_to_assets("il.png"))
    image.resize(320,32)
    image_image_2 = PhotoImage(image)
    image_2 = canvas.create_image(
    490.0,
    73.0,
    image=image_image_2)


