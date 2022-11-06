from conf.db_session import create_session
from Models.cliente import Cliente
from typing import Optional, List

def inserirCliente(dadosCliente:List) -> None:

    # Criando um objeto através da Classe Modelo 'Cliente'
    cli:Cliente = Cliente(
        nome=dadosCliente[0],
        endereco=dadosCliente[1],
        email=dadosCliente[2],
        telefone=dadosCliente[3]
    )

    # Trabalhando com Contexto: (Context Manager)
    try:
        with create_session() as session:
            session.add(cli)
            
            # Também podemos 'adicionar' uma lista
            #  de objs de uma só vez ao banco:
            # session.add_all([cli1, cli2, cli3,...])
            
            # Efetue todas as operações, ao final...
            session.commit()
    except:
        print("Erro ao cadastrar Cliente!")
    else:
        print("Cliente cadastrado com sucesso")    
        print(f"ID: {cli.matricula}, NOME: {cli.nome}")

