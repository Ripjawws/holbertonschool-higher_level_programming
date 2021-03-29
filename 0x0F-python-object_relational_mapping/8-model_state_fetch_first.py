#!/usr/bin/python3
"""
sessions
"""
import MySQLdb
import sqlalchemy
from sqlalchemy import (create_engine)
import sys
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    """sessions"""

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        our_user = session.query(State).order_by(State.id).first()
        print("{}: {}".format(our_user.id, our_user.name))
    except:
        print("Nothing")
    session.close()
