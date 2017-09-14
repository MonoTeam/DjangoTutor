from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def test(request):
    return HttpResponse('<h2>Hello World</h2>')

def index(request):
    dt = datetime.now()
    return render(request, "index.html", {'user': request.user, 'time': dt})