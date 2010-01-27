from django.template import loader, Context
from django.http import HttpResponse
from djangotest.simple.models import UserInfo

def main(request):
    info = UserInfo.objects.get()
    t = loader.get_template('main.html')
    c = Context({'info': info})
    return HttpResponse(t.render(c))
