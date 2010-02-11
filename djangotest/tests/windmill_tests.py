from windmill.authoring import WindmillTestClient

def test_auth():
    client = WindmillTestClient(__name__)

    client.click(id=u'username')
    client.type(text=u'zimyand', id=u'username')
    client.type(text=u'123123z', id=u'userpass')
    client.click(value=u'Login')
    client.waits.forPageLoad(timeout=u'20000')

    client.click(link=u'Logout')
    client.waits.forPageLoad(timeout=u'20000')