from sqlalchemy import create_engine, Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base


#criando o banco de dados
db = create_engine("sqlite:///meubanco.db")
Session = sessionmaker(bind = db)
session = Session()

Base = declarative_base()

#criando as tabelas
class Pratos(Base):
    __tablename__ = "pratos"

    id_prato = Column("id_prato", Integer, primary_key = True, autoincrement = True)
    nome = Column("nome", String)
    descricao = Column("descrição", String)
    preco = Column("preço", Float)

    def __init__(self, nome, descricao, preco):
        self.nome = nome
        self.descricao = descricao
        self.preco = preco


class Clientes(Base):
    __tablename__ = "clientes"

    id_cliente = Column("id_cliente", Integer, primary_key = True, autoincrement = True)
    nome = Column("nome", String)
    email = Column("e-mail", String)
    telefone = Column("telefone", Integer)

    def __init__(self, nome, email, telefone):
        self.nome = nome
        self.email = email
        self.telefone = telefone

class Pedidos(Base):
    __tablename__ = "pedidos"

    id_pedido = Column("id_pedido", Integer, primary_key = True, autoincrement = True)
    id_cliente = Column("id_cliente", ForeignKey("clientes.id_cliente"))
    data_pedido = Column("data", Integer)
    status = Column("status", String)

    def __init__(self, cliente, data, status):
        self.id_cliente = cliente
        self.data_pedido = data
        self.status = status


class ItensDoPedido(Base):
    __tablename__ = "itensdopedido"

    id_item_pedido = Column("id_item_pedido", Integer, primary_key = True, autoincrement = True)
    id_pedido = Column("id_pedido", ForeignKey("pedidos.id_pedido"))
    id_prato = Column("id_prato", ForeignKey("pratos.id_prato"))
    quantidade = Column("qtde", Integer)

    def __init__(self, pedido, prato, quantidade):
        self.id_pedido = pedido
        self.id_prato = prato
        self.quantidade = quantidade

Base.metadata.create_all(bind = db)