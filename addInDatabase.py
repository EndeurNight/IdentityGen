import sqlite3

def connectToDatabase():
    try:
        conn = sqlite3.connect('database.db')
        return conn
    except:
        print('Error connecting to database')
    return None

def addInDatabase():
    conn = connectToDatabase()
    if conn is not None:
        c = conn.cursor()
        c.execute(f'delete from identite')
        metier = open('metier.txt', 'r', encoding='utf-8')
        with open('names.txt', "r+",encoding="utf-8") as f:
            i = 1
            for name in f:
                
                if i <= len(metier.readlines()): 
                    profession = metier.read(i-1) 
                else:
                    profession = ""
                c.execute(f'INSERT INTO identite VALUES ({i}, "","{name}", "{profession}")')
                i += 1
        metier.close()
        conn.commit()
        conn.close()
    else:
        print('Connection to database failed')

addInDatabase()