from typing import List
from conf.db_session import create_session
from Models.cliente import Cliente 

# Funções de Agregação
from sqlalchemy import func

def filtra_clientes() -> None:
    try:
        with create_session() as session:
            # Retorna um objeto
            listaClientes:List[Cliente] = session.query(Cliente).filter(Cliente.matricula<=2)
            # listaClientes:List[Cliente] = session.query(Cliente).where(Cliente.matricula<=2)
            for cli in listaClientes:
                print(f"Codigo: {cli.matricula}")
                print(f"Nome: {cli.nome}")
                print(f"Endereço: {cli.endereco}")
            session.commit()
    except:
        print("Erro ao consultar Clientes!")


filtra_clientes()
