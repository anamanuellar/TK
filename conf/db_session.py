import sqlalchemy as sa
# Para acessar o bd, necessitamos ter um (Handler, que é
#  um manipulador de tabelas no bd, torna o acesso do sql 
# mais fácil de usar com esta classe de objetos)

# Criar sessões
from sqlalchemy.orm import sessionmaker
# No SqLite3 para criar pastas e arquivos 
from pathlib import Path
# Para tipagem de dados
from typing import Optional
from sqlalchemy.orm import Session
from sqlalchemy.future.engine import Engine
# Para definição das Tabelas no BD (DDL), caso necessário.
from Models.model_base import ModelBase

# Variável Global da engine do BD
__engine: Optional[Engine] = None

def create_engine(banco:str = "SQLite") -> Engine:
    
    """
        Criar a configuração ao BD
    """
    global __engine
    
    if __engine is None:
        if banco=="SQLite":
            arquivo_db = "db/estoque.sqlite" #estoque.db
            # Criar o banco no diretório (pasta) Pai
            folder = Path(arquivo_db).parent
            folder.mkdir(parents=True, exist_ok=True)
            # String de conexão do banco
            conn_str = f"sqlite:///{arquivo_db}"
            # Versões antigas do PySqLite n permitiam conexões em multithreads, isso agiliza agora.
            __engine = sa.create_engine(url=conn_str, echo=False, connect_args={"check_same_thread":False})
            
        elif banco == "PostgreSQL":
            conn_str = "postgresql://local:meuBanco@localhost:5432/estoque"
            __engine = sa.create_engine(url=conn_str, echo=False)  
        else:
            __engine = create_engine("mysql+pymysql://user:estoque@estoque/estoque?charset=utf8mb4")
            conn_str = __engine.connect()
        insp = sa.inspect(__engine)
        if not insp.has_table("Clientes"):
            create_tables()

    return __engine

def create_session() -> Session:
    """
        Criar a sessão de conexão ao BD
    """
    global __engine

    if not __engine:
        create_engine("SQLite")
    
    # O comportamento Session.commit() é que, por padrão, expira o estado 
    #  de todas as instâncias presentes após a conclusão do commit. 
    #  Para desabilitar este comportamento, colocamos um 'expire_on_commit=False'
    __session = sessionmaker(__engine, expire_on_commit=False, class_=Session)
    session:Session = __session()
    return session
    
def create_tables() -> None:
    """
        Criar as tabelas do BD
    """
    global __engine

    if not __engine:
        create_engine("SQLite")
    import Models.__all_models
    ModelBase.metadata.drop_all(__engine)
    ModelBase.metadata.create_all(__engine)
