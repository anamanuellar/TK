from decimal import Decimal
import sqlalchemy as sa
from datetime import datetime
from Models.model_base import ModelBase
# Para tipagem de dados
from typing import List

import sqlalchemy.orm as orm

from Models.cliente import Cliente
#from Models.produto import Produto

# Um Pedido pode ter vários Itens
# Montando então uma Entidade Itens
# com relacionamento ER(N:M)

itens_pedido = sa.Table(
    'Itens',
    ModelBase.metadata,
    sa.Column("cod_pedido",
              sa.Integer, 
              sa.ForeignKey('Pedidos.codigo')
    ),
    sa.Column("cod_produto",
              sa.Integer,
              sa.ForeignKey("Produtos.codigo")  
    )
)

class Pedido(ModelBase):
    __tablename__:str = "Pedidos"

    codigo: int = sa.Column(sa.Integer, primary_key=True)
    cod_cliente: int = sa.Column(sa.Integer, sa.ForeignKey('Clientes.matricula')) 
    situacao:str = sa.Column(sa.VARCHAR(1), nullable=False)
    data_pedido:str = sa.Column(sa.Date)
    total:float = sa.Column(sa.DECIMAL(10,2))
    
    # Um Pedido pode ter vários Itens e um Item esta interligado a um Pedido
    '''
    itens:List[Produto] = orm.relationship(Produto, 
                                            secondary=itens_pedido,
                                            backref="produto",
                                            lazy="dynamic"
    )
    '''
    # Um Pedido somente pode ter um Cliente
    cod_cliente:int = sa.Column(sa.Integer, sa.ForeignKey('Clientes.matricula'))
    cliente:Cliente = orm.relationship('Cliente', lazy='joined')
    
    def __repr__(self) -> str:
        return f"<{self.__tablename__}: {self.codigo}>"   
    
    '''
        Para testar:
        python
        Models.pedido import Pedido
        pe=(codigo=1, cod_cliente=1, situacao='P')
        pe
    '''
    

