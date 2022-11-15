from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import pandas as pd

engine = create_engine('sqlite:///teste.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Pessoa(Base):
  __tablename__ = 'pessoas'
  
  id = Column(Integer, primary_key=True)
  nome = Column(String)
  
  def __repr__(self):
    return self.nome
  
Base.metadata.create_all(engine)

# p1 = Pessoa(nome='Anderson')
# p2 = Pessoa(nome='Thais')
# p3 = Pessoa(nome='Thaison')
# p4 = Pessoa(nome='Thaison')

# session.add(p1)
# session.add_all([p2, p3, p4])
# session.commit()