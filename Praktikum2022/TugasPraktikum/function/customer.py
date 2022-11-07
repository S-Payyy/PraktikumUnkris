# Nama pelanggan
# • Alamat
# • No Telp
# • Tanggal
# • Harga per barang
# • Harga total
harga_total = 0
jumlah_total = 0
from function.menu import menutab
import datetime
import os
from rich.console import Console
from rich.table import Table
import sqlite3

def res():
    global harga_total
    global jumlah_total
    harga_total = 0
    jumlah_total = 0
    new()

def new():
    ### Table ###
    con = sqlite3.connect('../Praktikum2022/TugasPraktikum/data/database.db')
    cur = con.cursor()
    os.system("cls")
    con = sqlite3.connect('../Praktikum2022/TugasPraktikum/data/database.db')
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

    ### Input Cust ###
    nama_p = input("Nama Pelanggan : ")
    alamat = input("Alamat Pelanggan : ")
    no_p = input("No Telp Pelanggan : ")
    tanggal = datetime.datetime.now()

    #### Checking ####
    def check():
        a = input("\nApakah ada lagi ? ")
        if a in ["ya","yes","y"] :
            buy()
        else:
            print(f"""
            ##############################
            Nama\t: {nama_p}
            Alamat\t: {alamat}
            No Telp\t: {no_p}
            Total Barang : {jumlah_total}
            Total Harga\t : {harga_total}
            Tanggal\t: {tanggal.strftime("%w %B %Y")}
            ##############################
            Terima kasih 
            """)
            b = input("Tambah Customer Baru? ")
            if b in ["ya","yes","y"] :
                res()
            else:
                os.system('cls')
                menutab()
    
    def buyadd(xxx,j):
        global harga_total
        global jumlah_total
        jumlah_total = jumlah_total + int(j)
        harga_total = harga_total + int(xxx*j)

    def buy():
        barang = input("Nama Barang : ")
        cur.execute(f"SELECT id from product WHERE name ='{barang}'")
        if not cur.fetchone():
            print("Barang tidak tersedia.\n")
            buy()
        else:
            jumlah = input("Jumlah : ")
            cur.execute(f"SELECT price from product WHERE name ='{barang}'")
            h = cur.fetchone()
            buyadd(h[0],int(jumlah))
            check()

    buy()

