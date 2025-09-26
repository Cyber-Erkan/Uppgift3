import csv
import os
import locale


def list_products(products):
    for idx , product in enumerate(products, 1):
        print(f"{idx} ) {product['name']} {product['price']}")


def view_product(idx, products):
    if products == "0":
        pass
    else:
        product = products[idx - 1]
    return product


def format_currency(value):
    return locale.currency(value,grouping=True)


def load_data(filename): 
    products = []  

    with open(filename, 'r') as file:       #öppnar en fil med read-rättighet
        reader = csv.DictReader(file)
        for row in reader:
            id = int(row['id'])
            name = row['name']
            desc = row['desc']
            price = float(row['price'])
            quantity = int(row['quantity'])
            products.append(
                {                   
                    "id": id,       
                    "name": name,
                    "desc": desc,
                    "price": price,
                    "quantity": quantity
                }
            )
    return products


#TODO: skriv en funktion som tar bort en specifik produkt med hjälp av id


locale.setlocale(locale.LC_ALL, 'sv_SE.UTF-8')  

products = load_data('db_products.csv')
os.system('cls')

while True:
    list_products(products)
    idx = int(input("Välj en produkt: "))

    if idx == 0:
        list_products(products)
        print("Choose options below: \n1.Remove \n2.change \n3.add product ")
        option = int(input("Press 1 - 3 to choose option: "))
        product = view_product(idx, products)
        if option == 1:
            idx = (int(input(f"What product do you want to remove: "))) - 1
            products.pop(idx)
        elif option == 2:
            idx = (int(input(f"What product do you want to change: "))) - 1
            
            def add_products(products):
                id = int(input("ID: "))
                name = input("Namn: ")
                desc = input("Beskrivning: ")
                price = float(input("Pris: "))
                quantity = int(input("Antal: "))

                product = {}
                
                product['id'] = id
                product['name'] = name
                product['desc'] = desc
                product['price'] = price
                product['quantity'] = quantity

                products.append(product)
                return products
    else:
        product = view_product(idx, products)
        print(f"product: {product['name']} | {product['desc']}")





