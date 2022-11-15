#!/usr/bin/python3

"""
This script prints the fiest PLace object from the database
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

    first_state = session.query(State).order_by(State.id).first()

    print(first_state) if first_state else print('Nothing')
