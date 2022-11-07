def add(userid,password):
    import sqlite3
    con = sqlite3.connect('../Praktikum2022/TugasPraktikum/data/database.db')
    cur = con.cursor()
    cur.execute(f'INSERT INTO user VALUES ("{userid}","{password}")')
    a = input("Tambahkan Product ? y/n ").lower()
    if a == 'y' :
        con.commit()
        con.close()
    elif a == 'n' :
        con.close()
    else :
        print('Invalid Input!!')
        con.close()
