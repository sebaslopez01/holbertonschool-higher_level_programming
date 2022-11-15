#!/usr/bin/python3

"""
This script adds the State object 'Louisiana'
"""


if __name__ == '__main__':
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State
    import sys

    username, password, database_name = sys.argv[1:]
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost/{database_name}')

    Session = sessionmaker(bind=engine)
    session = Session()

    session.add(State(name='Louisiana'))
    session.commit()

    new_state = session.query(State).filter_by(name='Louisiana').first()

    print(new_state.id)
