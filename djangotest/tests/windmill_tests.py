from windmill.authoring import WindmillTestClient

def test_auth():
    client = WindmillTestClient(__name__)

    #check for correct user
    client.click(id=u'username')
    client.type(text=u'zimyand', id=u'username')
    client.type(text=u'123123z', id=u'userpass')
    client.click(value=u'Login')
    client.waits.forPageLoad(timeout=u'20000')
    #check no errors
    client.asserts.assertNotNode(xpath=u'/html/body/div[1]/span[1]')


    client.waits.forElement(link=u'Logout', timeout=u'8000')
    client.click(link=u'Logout')
    client.waits.forPageLoad(timeout=u'20000')

    #check for incorrect user
    client.type(text=u'zimyanderror', id=u'username')
    client.type(text=u'errorpass', id=u'userpass')
    client.click(value=u'Login')
    client.waits.forPageLoad(timeout=u'20000')
    #check for error field
    client.asserts.assertNode(xpath=u'/html/body/div[1]/span[1]')
