from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))

class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    name = Column(String(250),nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User, backref='category')

    '''RETURN OBJECT DATA IN EASILY SEARIALIZABLE'''
    @property
    def serialize(self):
        return {
            'name'      :self.name,
            'id'        :self.id
        }


class Items(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    description = Column(String(250))
    category_id = Column(Integer,ForeignKey('category.id'))
    category = relationship(Category, backref='items', cascade='all, delete')
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User, backref='items')

    '''RETURN OBJECT DATA IN EASILY SEARIALIZABLE'''

    @property
    def serialize(self):
        return {
            'name':             self.name,
            'id':               self.id,
            'description' :    self.description,
            'category':         self.category
        }



### Add in the end of database file ###
engine = create_engine('sqlite:///catalog.db')
Base.metadata.create_all(engine)