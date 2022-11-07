def menutab():
    from function.customer import new
    from function.crud import add,read,remove,update
    from rich.panel import Panel
    from rich.columns import Columns
    from rich.console import Console
    console = Console()
    print("Code Created by Muhamad Rifai Nim : 2270231011")

    menu_renderables = [(Panel("New Customer", expand=True, title="new")),(Panel("Setting", expand=True, title="set")),(Panel("Product Update", expand=True, title="crud"))]
    console.print(Columns(menu_renderables))

    def new_menu():
        new()
    
    def setting_menu():
        print("Maaf Menu ini blm tersedia.")
    
    def crud_menu():
        crud_menus= [(Panel("New Product", expand=True, title="new")),(Panel("Product List", expand=True, title="read")),(Panel("Update Product", expand=True, title="Up")),(Panel("Delete Product", expand=True, title="del"))]
        console.print(Columns(crud_menus))
        
        cm = input('CRUD Menu > ').lower()
        match cm:
            case "new": add(input('Product ID : ') , input('Product Name : '), input('Price : '))
            case "read": read()
            case "up": update(input('Product ID : ') , input('New Name : '), input('New Price : '))
            case "del": remove(input("Product ID : "))
            case _: crud_menu()

    m = input('menu > ').lower()
    match m:
        case "new": new_menu()
        case "set": setting_menu()
        case "crud": crud_menu()
        case _: menutab()
