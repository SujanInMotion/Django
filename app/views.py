from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Note,NoteType
from .forms import NoteForm

# Create your views here.
def home(request):
    note_obj = Note.objects.all().order_by('id')
    data = {"notes":note_obj}
    return render(request,"type.html",context=data)

def note_type(request):
    template = loader.get_template("type.html")
    return HttpResponse(template.render())

def create_note(request):
    note_form_obj = NoteForm()
    if request.method == 'POST':
        note_form_obj = NoteForm(data=request.POST)
        if note_form_obj.is_valid():
            note_form_obj.save()
    data = {'form':note_form_obj}
    return render(request,'create_note.html',context=data)

def edit_note(request,pk):
    note_obj = Note.objects.get(id=pk)
    if request == 'POST':
        form_obj = NoteForm(intance = note_obj,data=request.POSt)
        if form_obj.is_valid():
            form_obj.save()
    form_obj = NoteForm(instance=note_obj)
    data = {'form':form_obj}
    return render(request,'edit_note.html',context=data)