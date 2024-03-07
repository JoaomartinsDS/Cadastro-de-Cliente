from sqlalchemy.orm import declarative_base, relationship, Session
from sqlalchemy import Column, ForeignKey, Engine, create_engine, inspect, select
from sqlalchemy import String
from sqlalchemy import Integer

Base = declarative_base()


class User(Base):
    __tablename__ = 'user_account'
    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    age = Column(Integer)

    address= relationship('Address',back_populates='user')

    def __repr__(self):
        return f'User(id={self.id}, name={self.name},age={self.age})'

class Address(Base):
    __tablename__ = 'user_address'
    id = Column(Integer, primary_key=True)
    address = Column(String(30), nullable=False)
    cep = Column(Integer,nullable=False)
    user_id = Column(Integer,ForeignKey('user_account.id'))

    user = relationship('User', back_populates='address')

    def __repr__(self):
        return f'Address(address={self.address},cep={self.cep})'


engine = create_engine('sqlite://')
Base.metadata.create_all(engine)

with Session(engine) as session:
    usuario1 = User(
        name='joao',
        address=[Address(address='joao',cep='09320070')],


    )
    session.add_all([usuario1])
    session.commit()
stmt_user = select(User).order_by(User.id.asc())

for result in session.scalars(stmt_user):
    print(result)