import CRUD
from tabelas import session, Clientes

ligado = True

while ligado:
    user_input = input("Digite a operação desejada: CREATE, UPDATE, READ ou DELETE: ").lower()
    match user_input:
        case "create":
            CRUD.create()

        case "read":
            CRUD.read()
        
        case "update":
            CRUD.update()

        case "delete":
            CRUD.delete()
        
        case "off":
            ligado = False
        
        case _:
            print("Caso inválido. Tente novamente.")