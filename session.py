from ming import create_datastore, Session
import os

if os.getenv('TEST') == 'y':
    bind = create_datastore('mim://localhost:27017', database='test')
    session = Session(bind)
else:
    bind = create_datastore('ggnore')
    session = Session(bind)

