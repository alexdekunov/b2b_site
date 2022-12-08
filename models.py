from sqlalchemy import Column, Integer, String

from db import Base, engine


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String())
    email = Column(String(120), unique=True)

    def __repr__(self):
        return f'<User {self.name} {self.email}>'


if __name__ == '__main__':
    Base.metadata.create_all(bind=engine)   