from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from pprint import pprint

engine = create_engine('sqlite:///teste3.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Produto(Base):
  __tablename__ = 'produtos'
  id = Column(Integer, primary_key=True)
  nome = Column(String)
  pessoa_id = Column(Integer, ForeignKey('pessoas.id'))
  pessoa = relationship('Pessoa')
  
  def __repr__(self):
    return f'Produto(id={self.id}, nome={self.nome}, pessoa={self.pessoa})'
  

class Pessoa(Base):
  __tablename__ = 'pessoas'
  
  id = Column(Integer, primary_key=True)
  nome = Column(String)
  idade = Column(Integer)
  produtos = relationship(Produto, backref='pessoas')
  
  def __repr__(self):
    return f'Pessoa(nome={self.nome}, idade={self.idade}, produtos={self.produtos})'
  
Base.metadata.create_all(engine)

# p1 = Pessoa(nome='Anderson', idade=34)
# p2 = Pessoa(nome='Thais', idade=28)
# p3 = Pessoa(nome='Thaison', idade=1)
# p4 = Pessoa(nome='Thaisamara', idade=1)
# pd1 = Produto(nome='iPhone 11', pessoas=p1)
# pd2 = Produto(nome='iPhone 8', pessoas=p2)

# session.add(p1)
# session.add_all([p2, p3, p4, pd1, pd2])
# session.commit()

pprint(session.query(Pessoa).all())
pprint(session.query(Produto).filter_by(nome='iPhone 11').filter(Pessoa.nome == 'Anderson'))