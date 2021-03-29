#!/usr/bin/python3
"""
sessions
"""
from sqlalchemy import create_engine
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """sessions"""

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    state = State(name='Louisiana')
    session.add(state)
    session.commit()
    print(state.id)

    session.close()
