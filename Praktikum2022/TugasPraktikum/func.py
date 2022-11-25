import sqlite3
import os
import datetime
from rich.panel import Panel
from rich.columns import Columns
from rich.console import Console
from rich.table import Table
con = sqlite3.connect('database.db')
cur = con.cursor()
console = Console()

class CRUD:
    def __init__(self,x,y = 'null',z = 0):
        self.x = x ## productid
        self.y = y ## product name
        self.z = z ## product price


    def add(self,x,y,z):
        try:
            cur.execute(f"INSERT INTO product VALUES ('{x}','{y}','{z}')")
            self.commit()
        except:
            return print('Data sudah ada.')

    def remove(self):
        try:
            cur.execute(f"DELETE FROM product WHERE id={self.x}")
            self.commit()
        except:
            return print('Data tidak ditemukan.')

    def update(self):
        try:
            cur.execute(f"SELECT id from product WHERE id ='{self.x}'")
            if not cur.fetchone():
                print("Id product tidak ditemukan")
                Menutab()
            else:
                productname = input("Mausukan Nama Produk\t: ")
                price = input("Masukan Harga Produk\t: ")
                cur.execute(f"UPDATE product SET name = '{productname}' , price = '{price}' WHERE id = {self.x}")
                self.commit()
        except:
            return print('Data tidak valid.')

    def read():
        try:
            os.system("cls")
            cur.execute("SELECT * from product ")
            dat_p = cur.fetchall()
            tab = Table()
            col = ["ID","Name","Price"]
            for qq in col:
                tab.add_column(qq)
            for i in dat_p:
                tab.add_row(f"{i[0]}",f"{i[1]}",f"{i[2]}")
            console.print(tab)
            Menutab()
        except:
            return print('Data tidak tersedia.')

    def commit():
        check = input("Apakah anda yakin? ")
        if check in ["y",'yes','ya','ye'] :
            print("Perubahan disimpan")
            con.commit()
        else:
            return print("Perubahan tidak disimpan.")

class USER:
    def __init__(self,x,y):
        self.x = x # userid
        self.y = y # userpass
    
    def add(x,y):
        try:
            cur.execute(f'INSERT INTO user VALUES ("{x}","{y}")')
            CRUD.commit()
            Menutab()
        except:
            return print("Data tidak valid")

    def remove(x,y):
        try:
            cur.execute(f"DELETE from user WHERE Userid ='{x}' AND Pass ='{y}'")
            CRUD.commit()
            Menutab()
        except:
            return print("Data tidak valid")

    def update(x,y):
        try:
            cur.execute(f"SELECT id from user WHERE Userid ='{x}'")
            if not cur.fetchone():
                print("User tidak ditemukan")
                Menutab.menu()
            else:
                name = input("Mausukan Nama Baru\t: ")
                psswd = input("Masukan Passsword Baru\t: ")
                cur.execute(f"UPDATE user SET name = '{name}' , price = '{psswd}' WHERE id = {x}")
                CRUD.commit()
                Menutab()
        except:
            return print('Data tidak valid.')

class CUSTOMER:
    def __init__(self):
        CUSTOMER.new(self)

    def read():
        try:
            os.system("cls")
            cur.execute("SELECT * from product ")
            dat_p = cur.fetchall()
            tab = Table()
            col = ["ID","Name","Price"]
            for qq in col:
                tab.add_column(qq)
            for i in dat_p:
                tab.add_row(f"{i[0]}",f"{i[1]}",f"{i[2]}")
            console.print(tab)
        except:
            return print('Data tidak tersedia.')

    def new():
        while True:
            global harga_total,jumlah_total
            harga_total = 0
            jumlah_total = 0
            CUSTOMER.read()
            try:
                nama_p = input("Nama Pelanggan : ")
                alamat = input("Alamat Pelanggan : ")
                no_p = input("No Telp Pelanggan : ")
            except:
                print("Data Yang dimaksukkan salah!")
                return CUSTOMER.new()
            tanggal = datetime.datetime.now()
            def check():
                a = input("\nApakah ada lagi ? ")
                if a in ["ya","yes","y"] :
                    buy()
                else:
                    bon = f"\n##################################\nNama\t\t: {nama_p}\nAlamat\t\t: {alamat}\nNo Telp\t\t: {no_p}\nTotal Barang\t: {jumlah_total}\nTotal Harga\t: {harga_total}\nTanggal\t\t: {tanggal.strftime('%w %B %Y')}\n##################################\n"
                    print(bon)
                    with open('struk.txt', 'a') as f:
                        f.write(bon)
                    b = input("Tambah Customer Baru? ")
                    if b in ["ya","yes","y"] :
                        pass
                    else:
                        os.system('cls')
                        Menutab()
            def buyadd(xxx,j):
                global harga_total
                global jumlah_total
                jumlah_total = jumlah_total + int(j)
                harga_total = harga_total + int(xxx*j)
                return jumlah_total, harga_total
            def buy():
                barang = input("Nama Barang : ")
                cur.execute(f"SELECT id from product WHERE name ='{barang}'")
                if not cur.fetchone():
                    print("Barang tidak tersedia.\n")
                    buy()
                else:
                    try:
                        jumlah = input("Jumlah : ")
                        cur.execute(f"SELECT price from product WHERE name ='{barang}'")
                        h = cur.fetchone()
                        buyadd(h[0],int(jumlah))
                        check()
                    except:
                        print("Data Yang dimaksukkan salah!")
                        buy()
            buy()

class Menutab(CRUD,USER,CUSTOMER):
    def __init__(self):
        print("Code Created by Muhamad Rifai Nim : 2270231011")
        menu_renderables = [(Panel("New Customer", expand=True, title="cus")),(Panel("Setting", expand=True, title="set")),(Panel("Product Update", expand=True, title="crud"))]
        console.print(Columns(menu_renderables))
        Menutab.menu()

    def cus_menu():
        CUSTOMER.new()
    
    def setting_menu():
        crud_menus= [(Panel("Add User", expand=True, title="new")),(Panel("Remove User", expand=True, title="del")),(Panel("Update User", expand=True, title="Up"))]
        console.print(Columns(crud_menus))
        
        cm = input('Settings Menu > ').lower()
        match cm:
            case "new": USER.add(x= input("Masukan Username Baru : ") , y=input("Masukan Password Baru : "))
            case "up": USER.update(x=input("Masukan Username : ") ,y= input("Masukan Password : "))
            case "del": USER.remove(x=input("Masukan Username : ") ,y= input("Masukan Password : "))
            case _: Menutab.crud_menu()

    def crud_menu():
        crud_menus= [(Panel("New Product", expand=True, title="new")),(Panel("Product List", expand=True, title="read")),(Panel("Update Product", expand=True, title="Up")),(Panel("Delete Product", expand=True, title="del"))]
        console.print(Columns(crud_menus))
            
        cm = input('CRUD Menu > ').lower()
        match cm:
            case "new": CRUD.add(input('Product ID : ') , input('Product Name : '), input('Price : '))
            case "read": CRUD.read()
            case "up": CRUD.update(input('Product ID : ') , input('New Name : '), input('New Price : '))
            case "del": CRUD.remove(input("Product ID : "))
            case _: Menutab.crud_menu()

    def menu():
        m = input('menu > ').lower()
        match m:
            case "cus": Menutab.cus_menu()
            case "set": Menutab.setting_menu()
            case "crud": Menutab.crud_menu()
            case _: Menutab.menu()

#### Testing ####
#CRUD(int(input("Masukan ID : "))).remove()
