from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from docmanager.models import *
# Create your views here.

def test(request):
    return HttpResponse('<h2>Hello World</h2>')

def index(request):
    dt = datetime.now()
    s = Author.objects.get(id=1)
    doc = Document.objects.all()
    return render(request, "index.html", {'user': s, 'time': dt,'users' : request.user,'docu' : doc})