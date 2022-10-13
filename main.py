import tkinter
from BaseDeDonnees import BaseDeDonnees
from Generator import Generator

"""figd_x7RI6RIJEAKFF75aS00IaDkivLUrvAl61IidC_Lx""" #unique figma token

class main(BaseDeDonnees, Generator):
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title("Main")
        self.root.geometry("300x300")
        self.root.resizable(False, False)
        self.root.mainloop()



    





if __name__ == "__main__":
    main()
    