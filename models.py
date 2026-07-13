from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Tarefa(Base):
    __tablename__ = 'tarefas'

    id = Column(Integer, primary_key=True)
    descricao = Column(String)
    concluida = Column(Boolean, default=False)
