from models import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///tarefas.db')
 
Base.metadata.create_all(engine)

factory = sessionmaker(bind=engine)