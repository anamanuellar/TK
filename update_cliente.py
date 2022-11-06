from conf.db_session import create_session
from Models.cliente import Cliente

def atualizar_cliente(codigo:int, novoNome:str) -> None:
    
    try:
        with create_session() as session:
            cli:Cliente = session.query(Cliente).filter(Cliente.matricula==codigo).one_or_none()
            cli.nome = novoNome
            
            session.commit()
    except:
        print("Erro ao atualizar Cliente!")
    else:
        print("Cliente atualizado")    
        print(f"ID: {cli.matricula}, NOME: {cli.nome}")
atualizar_cliente(1, "Cliente 1")
