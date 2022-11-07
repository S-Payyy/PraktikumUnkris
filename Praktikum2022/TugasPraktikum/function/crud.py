import os
from rich.table import Table
from rich.console import Console
import sqlite3
from function.menu import menutab

def add(productid,name,price):
    con = sqlite3.connect('data/database.db')
    cur = con.cursor()
    cur.execute(f"INSERT INTO product VALUES ('{productid}','{name}','{price}')")
    a = input("Tambahkan Product ? y/n ").lower()
    if a == 'y' :
        con.commit()
        print("\n")
        b = input("Tambahkan Product lainnya ? y/n ").lower()
        if b == "y":
            add(input('Product ID : ') , input('Product Name : '), input('Price : '))
        else :
            os.system("cls")
            menutab()
    elif a == 'n' :
        os.system("cls")
        menutab()
    else :
        os.system("cls")
        print('Invalid Input!!')
        menutab()

def remove(productid):
    con = sqlite3.connect('data/database.db')
    cur = con.cursor()
    cur.execute(f'''
        DELETE FROM product WHERE id={productid}
    ''')
    a = input("Hapus Product ? y/n ").lower()
    if a == 'y' :
        con.commit()
        print("\n")
        b = input("Hapus Product lainnya ? y/n ").lower()
        if b == "y":
            remove(input('Product ID : '))
        else :
            os.system("cls")
            menutab()
    elif a == 'n' :
        os.system("cls")
        menutab()
    else :
        os.system("cls")
        print('Invalid Input!!')
        menutab()

def update(productid,productname,price):
    con = sqlite3.connect('data/database.db')
    cur = con.cursor()
    cur.execute(f"SELECT id from product WHERE id ='{productid}'")
    if not cur.fetchone():
        print("Id product tidak ditemukan")
        menutab()
    else:
        cur.execute(f"UPDATE product SET name = '{productname}' , price = '{price}' WHERE id = {productid}")
        a = input("Update Product ? y/n ").lower()
        if a == 'y' :
            con.commit()
            print("\n")
            b = input("Update Product lainnya ? y/n ").lower()
            if b in ["y","yes","ya"]:
                update(input('Product ID : ') , input('New Name : '), input('New Price : '))
            else :
                os.system("cls")
                menutab()
        elif a == 'n' :
            os.system("cls")
            menutab()
        else :
            os.system("cls")
            print('Invalid Input!!')
            menutab()

def read():
    os.system("cls")
    con = sqlite3.connect('data/database.db')
    cur = con.cursor()
    cur.execute("SELECT * from product ")
    dat_p = cur.fetchall()
    c = Console()
    tab = Table()
    col = ["ID","Name","Price"]
    for qq in col:
        tab.add_column(qq)
    for i in dat_p:
        tab.add_row(f"{i[0]}",f"{i[1]}",f"{i[2]}")
    c.print(tab)
    menutab()
    