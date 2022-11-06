from datetime import datetime
import sqlalchemy as sa
from datetime import datetime
from Models.model_base import ModelBase

class Produto(ModelBase):
    __tablename__:str = "Produtos"

    codigo:int = sa.Column(sa.INTEGER, primary_key=True)
    descricao:str = sa.Column(sa.VARCHAR(200), nullable=False)
    preco:float = sa.Column(sa.FLOAT)
    estoqueMinimo:int =  sa.Column(sa.INTEGER)
    estoqueAtual:int =  sa.Column(sa.INTEGER)
    data_cad: datetime = sa.Column(sa.DateTime, default=datetime.now, index=True)
    
    
    def __repr__(self) -> str:
        return f"<Produto: {self.nome}>"   
    
'''
    Para testar:
    python
    Models.produto import Produto
    cli=(nome="Carlos Gomes")
    print( cli )

'''