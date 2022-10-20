from fpdf import FPDF

class Convert:
    def __init__(self, pdf):
        self.pdf = pdf
    

    def convert(self):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.set_fill_color(27,47,71)
        pdf.cell(200, 10, txt="Atchoum", ln=1, align='C')
        pdf.output(self.pdf)

Convert('test.pdf').convert()