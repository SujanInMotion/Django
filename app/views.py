from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Note

# Create your views here.
def home(request):
    note_obj = Note.objects.all()
    data = {"notes":note_obj}
    return render(request,"type.html",context=data)

def note_type(request):
    template = loader.get_template("type.html")
    return HttpResponse(template.render())

def create_note(request):
    pass