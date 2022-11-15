from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pprint import pprint

engine = create_engine('sqlite:///teste.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Pessoa(Base):
  __tablename__ = 'pessoas'
  
  id = Column(Integer, primary_key=True)
  nome = Column(String)
  idade = Column(Integer)
  
  
  
  def __repr__(self):
    return f'Pessoa(id={self.id}, nome={self.nome}, idade={self.idade})'
  
Base.metadata.create_all(engine)

# p1 = Pessoa(nome='Anderson', idade=34)
# p2 = Pessoa(nome='Thais', idade=28)
# p3 = Pessoa(nome='Thaison', idade=1)
# p4 = Pessoa(nome='Thaisamara', idade=1)

# session.add(p1)
# session.add_all([p2, p3, p4])
# session.commit()

pprint(session.query(Pessoa).all())
pprint(session.query(Pessoa).filter_by(nome='Anderson').all())
pprint(session.query(Pessoa).filter_by(id=4).all())