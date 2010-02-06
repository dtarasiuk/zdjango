from windmill.authoring import WindmillTestClient
from django.contrib.auth import is_authenticated

def test_recordingSuite0():
    client = WindmillTestClient(__name__)

    if is_authenticated():
        client.click(link=u'Logout')
        client.waits.forPageLoad(timeout=u'20000')
    client.click(id=u'username')
    client.type(text=u'incorrectuser', id=u'username')
    client.click(value=u'Login')
    client.click(id=u'username')
    client.type(text=u'zimyand', id=u'username')
    client.type(text=u'123123z', id=u'userpass')
    client.click(value=u'Login')
    client.waits.forPageLoad(timeout=u'20000')