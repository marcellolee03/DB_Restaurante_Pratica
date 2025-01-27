from tabelas import session, Pratos, Clientes, Pedidos, ItensDoPedido
import numpy as np

#Funções para refinamento do código das funções principais
def tem_certeza_adicionar(adição):
    user_input = input("As informações acima estão corretas?(S/N) ").upper()

    if user_input == "S":
        session.add(adição)
        session.commit()
    else:
        return


def tem_certeza_remover(remocao, tipo):

    if tipo == "nome":
        user_input = input(f"Gostaria de apagar o item de nome {remocao.nome}?(S/N) ").upper()
    elif tipo == "pedido":
        user_input = input(f"Gostaria de apagar o pedido de ID {remocao.id_pedido}?(S/N) ").upper()
    else:
        user_input = input(f"Gostaria de apagar os itens de um pedido ID {remocao.id_item_pedido}?(S/N) ").upper()
    
    if user_input == "S":
        session.delete(remocao)
        session.commit()


def existe(objeto):
    if objeto is None:
        return False
    else:
        return True


#C - Create
def create():
    user_input = input("O que gostaria de adicionar? Um novo prato, cliente, pedido ou itens de um pedido (itens_pedido)? ")
    match user_input.lower():


        case "prato":
            nome = input("Digite o nome do prato: ").lower()
            descricao = input("Digite a descrição do prato: ")

            try:
                preco = float(input("Digite o preço do prato: R$ "))

                prato = Pratos(nome, descricao, preco)

                print(f"Nome: {prato.nome}\nDescrição: {prato.descricao}\nPreço: R$ {prato.preco}")
                tem_certeza_adicionar(prato)

            except ValueError:
                print("Preço inválido. Digite apenas números!")
                exit()
        

        case "cliente":
            nome = input("Digite o nome do cliente: ").lower()
            email = input("Digite o email do cliente: ").lower()

            try:
                telefone = int(input("Digite o telefone do cliente: "))

                cliente = Clientes(nome, email, telefone)

                print(f"Nome: {cliente.nome}\nEmail: {cliente.email}\nTelefone: {cliente.telefone}")
                tem_certeza_adicionar(cliente)
                
            
            except ValueError:
                print("Número inválido. Digite apenas números!")
                exit()


        case "pedido":
            user_input = input("Digite o nome do cliente: ").lower()
            cliente = session.query(Clientes).filter_by(nome = user_input).first()

            try:
                data = int(input("Digite a data do pedido no formato (ddmmaaaa): "))
                status = input("Digite o status do pedido: ").lower()

                pedido = Pedidos(cliente.id_cliente, data, status)

                print(f"Nome: {cliente.nome}\nData: {pedido.data_pedido}\nStatus: {pedido.status}")
                tem_certeza_adicionar(pedido)

            except ValueError:
                print("Data inválida. Digite apenas números!")
        
        
        case "itens_pedido":
            try:
                user_input1 = int(input("Digite o id do pedido: "))
                user_input2 = input("Digite o prato: ").lower()
                qtde = int(input("Digite a quantidade: "))

                pedido = session.query(Pedidos).filter_by(id_pedido = user_input1).first()
                prato = session.query(Pratos).filter_by(nome = user_input2).first()

                itens_do_pedido = ItensDoPedido(pedido = pedido.id_pedido, prato = prato.id_prato, quantidade = qtde)

                print(f"ID do pedido: {itens_do_pedido.id_pedido}\nPrato: {prato.nome}\nQuantidade: {itens_do_pedido.quantidade}")
                tem_certeza_adicionar(itens_do_pedido)

            except ValueError:
                print("Dados inválidos. Utilize apenas números ao descrever ID e quantidade!")
        

        case _:
            print("Operação Inválida. Tente novamente.")


#R - Read
def read():
    user_input = input("Qual tabela gostaria de analisar? Pedido ou itens de um pedido (itens_pedido)? ")
    match user_input.lower():
        case "pedido":
            lista = session.query(Pedidos.id_cliente).all()

            valores_unicos, contagem = np.unique(lista, return_counts = True)
            print(f"ID dos clientes que fizeream pedidos: {valores_unicos}")
            print(f"Quantidade de pedidos: {contagem}")
        
        case "itens_pedido":
            lista = session.query(ItensDoPedido.id_prato).all()

            valores_unicos, contagem = np.unique(lista, return_counts = True)
            print(f"ID dos pratos pedidos: {valores_unicos}")
            print(f"Quantidade de vezes que foram pedidos: {contagem}")
        
        case _:
            print("Operação Inválida. Tente novamente.")
    

#U - Update
def update():
    user_input = input("O que gostaria de atualizar? Um prato, cliente, pedido ou itens de um pedido (itens_pedido)? ")
    match user_input.lower():
        case "prato":
            user_input = input("Qual prato deseja atualizar? ")

            prato = session.query(Pratos).filter_by(nome = user_input).first()

            if existe(prato):

                prato.nome = input("Digite o nome do prato: ").lower()
                prato.descricao = input("Digite a descrição do prato: ")

                try:
                    prato.preco = float(input("Digite o preço do prato: R$ "))

                    print(f"Nome: {prato.nome}\nDescrição: {prato.descricao}\nPreço: R$ {prato.preco}")
                    tem_certeza_adicionar(prato)

                except ValueError:
                    print("Preço inválido. Digite apenas números!")
                    exit()
            
            else:
                print("Prato não encontrado.")


        case "cliente":
            user_input = input("Qual cliente deseja atualizar? ")
            
            cliente = session.query(Clientes).filter_by(nome = user_input).first()

            if existe(cliente):
                cliente.nome = input("Digite o nome do cliente: ").lower()
                cliente.email = input("Digite o email do cliente: ").lower()

                try:
                    cliente.telefone = int(input("Digite o telefone do cliente: "))

                    print(f"Nome: {cliente.nome}\nEmail: {cliente.email}\nTelefone: {cliente.telefone}")
                    tem_certeza_adicionar(cliente)
                    
                
                except ValueError:
                    print("Número inválido. Digite apenas números!")
                    exit()
            
            else:
                print("Cliente não encontrado.")
        

        case "pedido":
            user_input = input("Qual é o ID do pedido que deseja atualizar? ")
            pedido = session.query(Pedidos).filter_by(id_pedido = user_input).first()

            if existe(pedido):
                try:
                    pedido.data = int(input("Digite a data do pedido no formato (ddmmaaaa): "))
                    pedido.status = input("Digite o status do pedido: ").lower()

                    print(f"Nome: {cliente.nome}\nData: {pedido.data_pedido}\nStatus: {pedido.status}")
                    tem_certeza_adicionar(pedido)

                except ValueError:
                    print("Data inválida. Digite apenas números!")
            else:
                print("Pedido não encontrado.")
        
        
        case "itens_pedido":
            user_input = input("Qual é o ID do pedido que deseja atualizar? ")
            itens_do_pedido = session.query(ItensDoPedido).filter_by(id_item_pedido = user_input).first()

            if existe(itens_do_pedido):
                try:
                    user_input1 = int(input("Digite o id do pedido: "))
                    user_input2 = input("Digite o prato: ").lower()
                    qtde = int(input("Digite a quantidade: "))

                    pedido = session.query(Pedidos).filter_by(id_pedido = user_input1).first()
                    prato = session.query(Pratos).filter_by(nome = user_input2).first()

                    itens_do_pedido.id_pedido = pedido.id_pedido
                    itens_do_pedido.id_prato = prato.id_prato
                    itens_do_pedido.qtde = qtde

                    print(f"ID do pedido: {itens_do_pedido.id_pedido}\nPrato: {prato.nome}\nQuantidade: {itens_do_pedido.quantidade}")
                    tem_certeza_adicionar(itens_do_pedido)

                except ValueError:
                    print("Dados inválidos. Utilize apenas números ao descrever ID e quantidade!")
            else:
                print("ID não encontrado")
        
        case _:
            print("Operação Inválida. Tente novamente.")



#D - Delete
def delete():
    user_input = input("O que gostaria de remover? Um prato, cliente, pedido ou itens de um pedido (itens_pedido)? ")
    match user_input.lower():
        case "prato":

            nome_prato = input("Digite o nome do prato: ").lower()
            prato = session.query(Pratos).filter_by(nome = nome_prato).first()

            tem_certeza_remover(prato, "nome")
        

        case "cliente":
            nome_cliente = input("Digite o nome do cliente: ").lower()
            cliente = session.query(Clientes).filter_by(nome = nome_cliente).first()

            tem_certeza_remover(cliente, "nome")


        case "pedido":
            try:
                id = int(input("Digite o ID do pedido: "))
                pedido = session.query(Pedidos).filter_by(id_pedido = id).first()

                tem_certeza_remover(pedido, "ID")
            
            except ValueError:
                print("ID inválido. Digite apenas números!")
        

        case "itens_pedido":
            try:
                id = int(input("Digite o ID do pedido: "))
                itens_pedido = session.query(ItensDoPedido).filter_by(id_item_pedido = id).first()

                tem_certeza_remover(itens_pedido, "_")
            
            except ValueError:
                print("ID inválido. Digite apenas números!")
        
        case _:
            print("Operação Inválida. Tente novamente.")