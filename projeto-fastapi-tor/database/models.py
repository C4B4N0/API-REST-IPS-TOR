from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class BancoIP(Base):
    __tablename__ = 'bancoIP'
    id = Column(Integer, primary_key=True, autoincrement=True)
    ip_address = Column(String, unique=True, nullable=False)

    
