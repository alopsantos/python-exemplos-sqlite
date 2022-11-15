from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pprint import pprint
# firebird+fdb://user:password@host:port/path/to/db[?key=value&key=value...]
engine = create_engine('firebird://SYSDBA:masterkey@localhost:3050/teste', encoding="UTF8", echo=True)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()
pprint(session.bind_table())
# class Pessoa(Base):
#   __tablename__ = 'pessoas'
  
#   id = Column(Integer, primary_key=True)
#   nome = Column(String)
  
#   def __repr__(self):
#     return f'Pessoa(nome:"{self.nome}")'
  
# Base.metadata.create_all(engine)

# p1 = Pessoa(nome='Anderson')
# p2 = Pessoa(nome='Thais')
# p3 = Pessoa(nome='Thaison')
# p4 = Pessoa(nome='Thaison')

# session.add(p1)
# session.add_all([p2, p3, p4])
# session.commit()

# pprint(session.query(Pessoa).all())

# class Versao(Base):
#   __tablename__ = 'VERSAO'
  
#   CHAVE = Column(String, primary_key=True)
#   DADO = Column(Integer)
  
#   def __repr__(self):
#     return f'VERSAO(Chave: {self.CHAVE}, DADO: {self.DADO})'
  
#   Base.metadata.create_all(engine)
  
# pprint(session.query(Versao).all())