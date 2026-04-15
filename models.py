from sqlalchemy import create_engine, Column, String, Integer, Boolean, Float, ForeignKey
from sqlalchemy.orm import declarative_base

db = create_engine('sqlite:///banco.db')

Base = declarative_base()

class Reels(Base):
    __tablename__ = 'reels'
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    conteudo = Column("conteudo", String, nullable=False)
    likes = Column("likes", Integer, default=0)
    views = Column("views", Integer, default=0)
    description = Column("description", String)
    status = Column("status", String, nullable=False)
    id_usuario = Column("id_usuario", ForeignKey("usuarios.id"))
    nome_usuario = Column("nome_usuario", ForeignKey("usuario.nome"))
    
    def __init__(self, conteudo, description, status, id_usuario, nome_usuario):
        self.conteudo = conteudo
        self.description = description
        self.status = status
        self.id_usuario = id_usuario
        self.nome_usuario = nome_usuario
    