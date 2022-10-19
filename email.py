#a partir du fichier hebergeurs.txt, on construit une liste des hébergeurs
#on ouvre le fichier en lecture
hebergeurs = []
with open("hebergeurs.txt", "r") as f :
    for line in f :
        #on enlève les espaces et les sauts de ligne
        line = line.strip()
        #on ajoute l'hébergeur à la liste
        hebergeurs.append(line)

#on ouvre le fichier en écriture
with open("hebergeurs.txt", "w") as f :
    #on écrit les hébergeurs dans le fichier
    for hebergeur in hebergeurs :
        f.write("\"" + hebergeur + "\", ")

