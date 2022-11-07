from time import sleep
from rich.console import Console
from rich.markdown import Markdown
from rich.progress import track
from function import menu
import os
import sqlite3

if __name__ == "__main__":
    sistem_operasi = os.name

    match sistem_operasi:
        case "posix": os.system("clear")
        case "nt": os.system("cls")

    def login():
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
            login()
        else:
            print("\nLogin Sukses")
            for i in track(range(1), description="Processing..."):
                sleep(1)
            os.system('cls')
            menu.menutab()

    login()
