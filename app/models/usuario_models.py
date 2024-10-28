from sqlalchemy import Column, String, Integer 
from sqlalchemy.orm import declarative_base
from config.database import db

Base = declarative_base ()

class Usuario(Base):
    ## DEFININDO CARACTERISTICAS DA TABELA NO BANCO DE DADOS.
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(150))
    email = Column(String(150))
    senha = Column(String(150))

    ## DEFININDO CARACTERISTICAS DA CLASSE.
    def __init__(self, nome: str, email: str, senha: str):
        self.nome = nome
        self.email = email
        self.senha = senha

## CRIANDO TABELA NO BANCO DE DADOS.
Base.metadata.create_all(bind=db)