from django.template import loader, Context
from django.http import HttpResponse, HttpResponseRedirect
from djangotest.simple.models import UserInfo
from django.contrib.auth import authenticate, login, logout

def main(request):
    info = UserInfo.objects.get()
    if not info:
        raise Exception("Empty base")
    data = {'info': info}
    c = Context(data)
    t = loader.get_template('main.html')
    return HttpResponse(t.render(c))

