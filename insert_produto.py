from conf.db_session import create_session
from Models.produto import Produto
from typing import Optional, List

def inserirProduto(dadosProduto:List) -> None:

    # Criando um objeto através da Classe Modelo 'Produto'
    cli:Produto = Produto(
        descricao=dadosProduto[0],
        preco=dadosProduto[1],
        estoqueMinimo=dadosProduto[2],
        estoqueAtual=dadosProduto[3]
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
        print("Erro ao cadastrar Produto!")
    else:
        print("Produto cadastrado com sucesso")    
        print(f"ID: {cli.produto}, DESCRICAO: {cli.descricao}")

