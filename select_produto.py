from conf.db_session import create_session
from Models.produto import Produto

def lista_Produtos() -> None:
    try:
        with create_session() as session:
            # Retorna um objeto[Produto] = session.query(Produto)
            
            # Retorna uma lista
            listaProduto = session.query(Produto)#.order_by(Cliente.matricula.desc()).all()
            enviarLista=[]
            for prod in listaProduto:
                enviarLista.append([
                    prod.codigo,
                    prod.descricao,
                    prod.preco,
                    prod.estoqmin,
                    prod.estoqmax,
                ])
            session.commit()
            return enviarLista
    except:
        print("Erro ao consultar Produto!")

# Para testar:
#lista_Produto()
