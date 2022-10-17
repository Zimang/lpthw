from nose.tools import *
from app import app
app.config['TESTING']=True
web=app.test_client()
# I can run nose on win because its python has a higher version
# so I will try this in Ubuntu
def test_index():
    rv =web.get('/',follow_redirects=True)
    assert_equal(rv.status_code,404)

    rv =web.get('/hello',follow_redirects=True)
    assert_equal(rv.status_code,200)
    assert_in(b"Fill Out This Form",rv.data)

    data={'name':'黄子明','greet':'Hola'}
    rv=web.post('/hello',follow_redirects=True,data=data)
    assert_in(b'黄子明',rv.data)
    assert_in(b'Hola',rv.data)
