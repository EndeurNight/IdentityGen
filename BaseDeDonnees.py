from operator import le
import sqlite3
from random import randint

class BaseDeDonnees:
    def __init__(self, databaseName):
        self.database = databaseName
        self.conn = None
        self.cursor = None

    def connectToDatabase(self):
        try:
            self.conn = sqlite3.connect(self.database)
            self.cursor = self.conn.cursor()
        except:
            print('Error connecting to database')

    def getFirstNames(self):
        if self.cursor == None:
            self.connectToDatabase()
        
        self.cursor.execute('SELECT prenom FROM identite')
        return self.cursor.fetchall()


    def getRandomFirstName(self):
        name = self.getFirstNames()
        return name[randint(0, len(name))][0].split("\n")[0]


    def getJobs(self):
        if self.cursor == None:
            self.connectToDatabase()
        
        self.cursor.execute('SELECT metier FROM identite WHERE metier != "NULL"')
        return self.cursor.fetchall()

    def getRandomJob(self):
        job = self.getJobs()
        return job[randint(0, len(job))][0].split("\n")[0]




