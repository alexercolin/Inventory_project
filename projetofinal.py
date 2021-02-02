import io
import csv

DIC = []
dict_keys = ("id", "name", "price")

# ADICIONAR O ITEM - Status: OK.
def add_item(name, price):
    try:
        item_id = int (DIC[-1]["id"])+1
    except (IndexError, KeyError):
        item_id=1

    item = { 

        "id": str (item_id),
        "name":name,
        "price":price,        
     }

    DIC.append(item)
    print (" Item adicionado com sucesso")


#### REMOVER ITEM - Status: OK

def remove_item(id_item):
    item_remove = None

    for item in DIC:
        if item["id"] == id_item:
         item_remove = item
    
    if item_remove:
        r = input(f"Tem certeza que deseja remover {item_remove['name']}? (S/N): ")
        if r in ("s", "S"):
            DIC.remove(item_remove)
            print(f"{item_remove['name']} removido com sucesso.\n")
    else:
        print(f"Nenhum item com o id {id_item} encontrado.\n")


### GERAR CSV - STATUS : OK

def gerar_csv ():
    
    with io.open("inventario.csv", "w",newline="") as csv_file:
        fieldnames = ("id", "Nome", "Preço")
        writer = csv.DictWriter(csv_file, fieldnames = fieldnames, delimiter = ";")

        writer.writeheader()
        writer.writerow(DIC)



############ CABEÇALHO DO PROGRAMA - Status: OK
##### REFERÊNCIAS - Status: OK

answer = 0
while answer != 5:
    print (
     "XXXXX SISTEMA DE INVENTÁRIO\n"
     "1 - Adicionar item\n"
     "2 - Remover item\n"
     "3 - Listar itens\n"
     "4 - Gerar CSV dos itens existentes\n"
     "5 - Sair da aplicação"
     )

    answer = int (input("Escolha a opção desejada : "))

    if answer == 1:
     name = input ("Nome: ")
     price = float (input ("Preço: "))

     add_item(name, price)

    elif answer==2:

     id_item = input ("Digite o id que gostaria de remover: ")

     remove_item(id_item)

    elif answer ==3:
     print (f"{DIC}")

    elif answer == 4:
        gerar_csv()
        
    elif answer == 5:
     print ("Saindo do sistema...")
     quit()

    else:
        print(" Opção inválida")

    






    


