from conf.db_session import create_session
from Models.cliente import Cliente

def excluir_cliente(codigo:int) -> None:
    
    try:
        with create_session() as session:
            cli:Cliente = session.query(Cliente).where(Cliente.matricula==codigo).one_or_none()
            print("**** ", cli)
            if cli:
                session.delete(cli)
                print("Cliente Excluído")
                session.commit()
            else:
                print("Matrícula não cadastrada")
    except:
        print("Erro ao excluir Cliente!")
excluir_cliente(2)
