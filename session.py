from ming import create_datastore, Session
import os

# use the inmemory database if we're running tests
if os.getenv('TEST') == 'y':
    bind = create_datastore('mim://localhost:27017', database='test')
else:
    bind = create_datastore('ggnore')

session = Session(bind)

