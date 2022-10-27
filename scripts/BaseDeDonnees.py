from operator import le
import sqlite3
from random import randint

class BaseDeDonnees:
    def __init__(self, databaseName):
        self.database = databaseName
        self.conn = None
        self.cursor = None

    def connectToDatabase(self):
        #On se connecte à la base de données
        try:
            self.conn = sqlite3.connect(self.database)
            self.cursor = self.conn.cursor()
        except:
            print('Error connecting to database')

    def getFirstNames(self):
        #On récupère tous les prénoms de la base de données
        if self.cursor == None:
            self.connectToDatabase()
        self.cursor.execute("SELECT prenom FROM identite WHERE prenom != 'NULL' AND prenom NOT LIKE '%=%'")
        return self.cursor.fetchall()

    def getRandomFirstName(self):
        #On récupère un prénom aléatoire, contient prenom et sexe
        name = self.getFirstNames()
        return name[randint(0, len(name))][0].split("\n")[0]

    def getJobs(self):
        #On récupère tous les métiers de la base de données
        if self.cursor == None:
            self.connectToDatabase()
        self.cursor.execute('SELECT metier FROM identite WHERE metier != "NULL" AND metier NOT LIKE "%=%"')
        return self.cursor.fetchall()

    def getRandomJob(self):
        job = self.getJobs()
        return job[randint(0, len(job))][0].split("\n")[0]
    
# test = BaseDeDonnees('data/database.db')
# print(test.getRandomFirstName())
# print(test.getRandomFirstName())




