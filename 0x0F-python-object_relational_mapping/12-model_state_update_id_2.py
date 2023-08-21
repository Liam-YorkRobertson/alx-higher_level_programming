#!/usr/bin/python3
"""
    script that changes the name of a State object
    from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    state_id = 2
    new_state_name = "New Mexico"

    state_to_update = session.query(State).get(state_id)

    if state_to_update:
        state_to_update.name = new_state_name
        session.commit()
    else:
        print("Not found")

    session.close()
