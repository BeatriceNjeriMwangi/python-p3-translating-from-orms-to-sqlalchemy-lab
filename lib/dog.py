from models import Dog
from sqlalchemy.orm import session

def create_table(base, engine):
    # engine= create_engine('sqlite:///dogs.db')
    base.metadata.create_all(engine)
    pass

def save(session, dog):
    session.add(dog)
    session.commit()
    pass

def get_all(session):
    return session.query(Dog).all()
    
    pass

def find_by_name(session, name):
    return session.query(Dog).filter_by(name=name).first() 
    
    # return [name for name in session.query(Dog.name)]
    pass

def find_by_id(session, id):
    return session.query(Dog).filter_by(id=id).first()
    pass

def find_by_name_and_breed(session, name, breed):
    return session.query(Dog).filter_by(name=name, breed=breed).first()
    pass

def update_breed(session, dog, breed):
    dog.breed = breed
    session.commit()
    pass

