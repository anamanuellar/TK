from conf.db_session import create_session
from Models.cliente import Cliente 

def lista_clientes() -> None:
    try:
        with create_session() as session:
            # Retorna um objeto
            # listaCliente:List[Cliente] = session.query(Cliente)
            
            # Retorna uma lista
            listaClientes = session.query(Cliente)#.order_by(Cliente.matricula.desc()).all()
            enviarLista=[]
            for cli in listaClientes:
                enviarLista.append([
                    cli.matricula,
                    cli.nome,
                    cli.endereco,
                    cli.email,
                    cli.telefone
                ])
            session.commit()
            print(enviarLista)
            return enviarLista
    except:
        print("Erro ao consultar Clientes!")

# Para testar:
#lista_clientes()
