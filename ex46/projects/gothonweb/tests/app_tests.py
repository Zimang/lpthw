from nose.tools import *
from app import app
app.config['TESTING']=True
web=app.test_client()

def test_index():
    rv =web.get()
