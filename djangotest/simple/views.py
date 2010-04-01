from django.conf import settings
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import Context
from django.template import loader
from djangotest.simple.models import UserInfo
from djangotest.simple.models import UserInfoForm

def main(request):
    error = []
    if (request.POST.has_key('username') and request.POST.has_key('userpass')):
        error = login_user(request)
    
    info = UserInfo.objects.get()
    
    data = {
        'info': info,
        'settings': settings
        }
    if error:
        data['error'] = error
    if request.user.is_authenticated():
        data['user_display_name'] = request.user.first_name + \
        " " + request.user.last_name
    c = Context(data)
    t = loader.get_template('main.html')
    return HttpResponse(t.render(c))

@login_required
def edit(request):
    info = UserInfo.objects.get()
    if request.method == 'POST':
        form = UserInfoForm(request.POST, instance=info)
    else:
        form = UserInfoForm(instance=info)
    if form.is_valid():
        form.save()
    data = {'info': info, 'form': form}
    c = Context(data)
    t = loader.get_template('edit.html')
    return HttpResponse(t.render(c))

def login_user(request):
    username = request.POST['username']
    password = request.POST['userpass']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return
    else:
        return {"type": 1, "value": "pass incorrect"}

def logout_user(request):
    logout(request)
    return HttpResponseRedirect("../")