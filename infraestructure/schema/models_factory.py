from sqlalchemy import String, Integer, Column, ForeignKey
from sqlalchemy.orm import relationship

from infraestructure.configuration.db import Base, engine, meta


class Establishment(Base):
    __tablename__ = 'establishment'
    uuid = Column(String(255), primary_key=True, unique=True)
    name = Column(String(255))
    portrait = Column(String(255))
    gallery = relationship("Gallery", back_populates="establishment")
    description = Column(String(255))
    opening_hours = Column(String(8))
    closing_hours = Column(String(8))
    days = Column(String(255))
    category_id = Column(Integer, ForeignKey('category.uuid'))
    category = relationship("Category", back_populates="establishment")
    service = relationship("Service", back_populates="establishment")
    address = Column(String(255))
    comment = relationship("Comment", back_populates="establishment")
    user_id = Column(String(255))

class Service(Base):
    __tablename__ = 'service'
    uuid = Column(String(255), primary_key=True, unique=True)
    name = Column(String(255))
    establishment_id = Column(String(255), ForeignKey('establishment.uuid'))
    establishment = relationship('Establishment', back_populates='service')


class Gallery(Base):
    __tablename__ = 'gallery'
    uuid = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    url = Column(String(255))
    establishment_id = Column(String(255), ForeignKey('establishment.uuid'))
    establishment = relationship('Establishment', back_populates='gallery')


class Category(Base):
    __tablename__ = 'category'
    uuid = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    name = Column(String(255), unique=True)
    establishment = relationship('Establishment', back_populates='category')


class Comment(Base):
    __tablename__ = 'comment'
    uuid = Column(String(255), primary_key=True, unique=True)
    user_id = Column(String(255))
    establishment_id = Column(String(255), ForeignKey('establishment.uuid'))
    comment = Column(String(255))
    rating = Column(Integer)
    establishment = relationship('Establishment', back_populates='comment')


Base.metadata.create_all(engine)
