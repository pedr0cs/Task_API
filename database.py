from models import Base
from sqlalchemy import create_engine

engine = create_engine('sqlite:///tarefas.db')

Base.metadata.create_all(engine)