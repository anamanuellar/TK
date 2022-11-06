from typing import List
from conf.db_session import create_session
from Models.cliente import Cliente 

# Funções de Agregação
from sqlalchemy import func

def filtra_cliente(codigo:int) -> None:
    try:
        with create_session() as session:
            # Retorna um objeto
            cli = session.query(Cliente).filter(Cliente.matricula==codigo).one_or_none()
            #cli = session.query(Cliente).where(Cliente.matricula==codigo).one_or_none()
            #first(), one_or_none(), one()
            print(f"Codigo: {cli.matricula}")
            print(f"Nome: {cli.nome}")
            print(f"Endereço: {cli.endereco}")
            session.commit()
    except:
        print("Erro ao consultar Clientes!")


filtra_cliente(2)
