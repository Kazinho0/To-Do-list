from sqlalchemy import Integer , String , Boolean , Column
from database import base

class Tarefas(base):
    __tablename__ = 'tarefas'
#   (id int auto_increment primary key, titulo varchar(50) not null, descrição varchar(500) not null, estado bool default false)
    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(50), nullable=False)
    descrição = Column(String(500), nullable=False)
    estado = Column(Boolean, default=False)