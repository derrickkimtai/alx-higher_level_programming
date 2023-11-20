#!/usr/bin/python3
from sqlalchemy impor create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("input those lacking part of the input pls")
        sys.exit(1)
    username, password, database_name = sys.argv[1], sys.argv[1], sys.argv[3]
     engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{database_name}')
     Base.metadata.bind = engine

    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    states = session.query(State).order_by(State.id).all()

    for state in states:
        print(f"{state.id}: {state.name}")

    session.close()
