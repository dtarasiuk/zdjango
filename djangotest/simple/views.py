from django.template import loader, Context
from django.http import HttpResponse, HttpResponseRedirect
from djangotest.simple.models import UserInfo
from django.contrib.auth import authenticate, login, logout

def main(request):
    error = []
    if (request.POST.has_key('username') and request.POST.has_key('userpass')):
        error = loginUser(request)

    info = UserInfo.objects.get()
    if not info:
        raise Exception("Empty base")
    data = {'info': info}
    if error:
        data['error'] = error
    if request.user.is_authenticated():
        data['user_display_name'] = request.user.first_name+" "+request.user.last_name
    c = Context(data)
    t = loader.get_template('main.html')
    return HttpResponse(t.render(c))

def loginUser(request):
    username = request.POST['username']
    password = request.POST['userpass']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return
    else:
        return {"type": 1, "value": "pass incorrect"}

def logoutUser(request):
    logout(request)
    return HttpResponseRedirect("../")