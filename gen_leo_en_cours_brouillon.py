from random import randint, choices

class PyGen :
    def __init__(self) :
        pass
    def num_phone() :
        id_list = ["06", "07"]
        id_probas = [.70, .30]
        id = choices(id_list, id_probas)