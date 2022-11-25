from time import sleep
from rich.console import Console
from rich.markdown import Markdown
from rich.progress import track
from rich.console import Console
from func import Menutab
import os
import sqlite3

if __name__ == "__main__":
    sistem_operasi = os.name

    match sistem_operasi:
        case "posix": os.system("clear")
        case "nt": os.system("cls")
        
    salah = 0
    while True:
        con = sqlite3.connect('database.db')
        cur = con.cursor()
        console = Console()
        LOGIN = "# Login"
        console.print(Markdown(LOGIN))

        username = input('Username : ')
        password = input('Password : ')

        cur.execute(f"SELECT Userid from user WHERE Userid ='{username}' AND Pass ='{password}'")
        if not cur.fetchone():
            print("\nLogin Failed")
            for i in track(range(1), description="Try again..."):
                sleep(1)
            os.system('cls')
            salah+=1
            if salah >=3:
                print('Anda telah salah sebanyak 3 kali.')
                print('Program dihentikan.')
                break
            else:
                continue
        else:
            print("\nLogin Sukses")
            for i in track(range(1), description="Processing..."):
                sleep(1)
            match sistem_operasi:
                case "posix": os.system("clear")
                case "nt": os.system("cls")
            Menutab()
