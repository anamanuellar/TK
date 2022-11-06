from conf.db_session import create_session
from Models.cliente import Cliente 
from sqlalchemy import func
from typing import List

def lista_clientes() -> None:
    try:
        with create_session() as session:
            # Retorna um objeto
            # listaCliente:List[Cliente] = session.query(Cliente)
            
            # Retorna uma lista
            resultado:List = session.query(
                func.sum(Cliente.matricula).label("soma"),
                func.avg(Cliente.matricula).label("media"),
                func.max(Cliente.matricula).label("maximo"),
                func.min(Cliente.matricula).label("minimo")
            ).all()
            
        print(f"soma = {resultado[0][0]}")
        print(f"Média = {resultado[0][1]}")
        print(f"Maior = {resultado[0][2]}")
        print(f"Menor = {resultado[0][3]}")

        session.commit()
    except:
        print("Erro ao consultar Clientes!")


lista_clientes()
