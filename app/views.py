from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def home(request):
    return HttpResponse("hello world")

def note_type(request):
    template = loader.get_template("type.html")
    return HttpResponse(template.render())