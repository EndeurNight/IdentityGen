from asyncio.windows_events import NULL
import sqlite3

def connectToDatabase():
    try:
        conn = sqlite3.connect('data/database.db')
        return conn
    except:
        print('Error connecting to database')
    return None

def addInDatabase():
    conn = connectToDatabase()
    if conn is not None:
        c = conn.cursor()
        c.execute(f'delete from identite')
        metier = open('data/metier.txt', 'r', encoding='utf-8').readlines()
        with open('data/names.txt', "r+",encoding="utf-8") as f:
            i = 1
            for name in f:
                
                if i < len(metier): 
                    profession = metier[i].split("\n")[0]
                else:
                    profession = "NULL"
                c.execute(f'INSERT INTO identite VALUES ({i}, "","{name}", "{profession}")')
                i += 1
        conn.commit()
        conn.close()
    else:
        print('Connection to database failed')

addInDatabase()