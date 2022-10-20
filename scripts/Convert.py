from fpdf import FPDF
from PIL import Image
import os


class Convert:
    def __init__(self, pdf, informations):
        self.pdf = pdf
        self.informations = informations


    def convert(self):
        pdf = FPDF('P','mm','A4')
        pdf.add_page()
        pdf.set_margins(0,0,0)
        pdf.set_font("Arial", size=12)
        img = Image.new("RGB",(211,300) ,(27,47,71))
        img.save("background.png")
        pdf.image("./background.png", 0, 0, pdf.w, pdf.h, type = '', link = '')

        pdf.cell(25,5, txt="Prénom : " + self.informations["prenom"], align="C", fill=False)
        pdf.ln(5)
        pdf.cell(30,5, txt="Job : " + self.informations["job"], align="C", fill=False)
        pdf.ln(5)
        pdf.image(self.informations["image"],150,150, 50, 50, type = '', link = '')

        




        pdf.output(self.pdf)

        
        

