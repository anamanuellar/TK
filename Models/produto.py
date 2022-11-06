from datetime import datetime
import sqlalchemy as sa
from datetime import datetime
from Models.model_base import ModelBase

class Cliente(ModelBase):
    __tablename__:str = "Clientes"

    matricula:int = sa.Column(sa.INTEGER, primary_key=True)
    nome:str = sa.Column(sa.VARCHAR(200), nullable=False)
    endereco:str = sa.Column(sa.VARCHAR(200))
    email:str =  sa.Column(sa.VARCHAR(50))
    telefone:str = sa.Column(sa.VARCHAR(50))
    data_cad: datetime = sa.Column(sa.DateTime, default=datetime.now, index=True)
    
    
    def __repr__(self) -> str:
        return f"<Cliente: {self.nome}>"   
    
'''
    Para testar:
    python
    Models.cliente import Cliente
    cli=(nome="Carlos Gomes")
    print( cli )

'''