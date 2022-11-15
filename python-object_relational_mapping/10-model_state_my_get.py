#!/usr/bin/python3

"""
This script list all State objects with the name passed as argument
"""


if __name__ == '__main__':
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State
    import sys

    username, password, database_name, state_name = sys.argv[1:]
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost/{database_name}')

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter_by(name=state_name).first()

    print(state.id) if state else print('Not found')
