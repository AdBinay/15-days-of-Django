from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound
from django.views.decorators.http import require_http_methods
from django.views.decorators.cache import cache_page
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views import View
import datetime as dt
# Create your views here.
# @cache_page(60*15)
@login_required
def home(request):
    print("home view is called..")
    print(dt.datetime.now)
    context = {
        'user':{
            'name':'binay',
            'age':'23',
            'address':'pokhara-05',
            'date':dt.datetime.now(),
        }
    }
    return render(request,"firstapp/home.html",context)

def login(request):
    return HttpResponse("<h1>This is login page</h1>", status = 200)

class IndexView(View):
    def get(self,request):
        return HttpResponse("<h1>This is index, a class based view</h1>")