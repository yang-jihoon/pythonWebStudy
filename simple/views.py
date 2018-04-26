from django.shortcuts import render
from .models import Note

from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
# Create your views here.
#from django.http import HttpResponse

import random

def hello(request):
    x = random.randint(1,100000)
    v = {'value':x}
    #html = "<h1>Hello, Django {}</h1>".format(str(x))
    return render(request,'simple/hello.html',{'data':v})

def note(request):
    notes = Note.objects.all().order_by('-published_date')
    return render(request, 'simple/note.html', {'notes': notes})


class Write(CreateView):
    model = Note
    fields = ['name', 'text']
    success_url = reverse_lazy('note')