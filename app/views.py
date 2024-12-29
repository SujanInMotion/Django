from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from .models import Note,NoteType
from .forms import NoteForm,UserForm
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate,login


# Create your views here.
def home(request):
    note_obj = Note.objects.all().order_by('id')
    data = {"notes":note_obj}
    return render(request,"index.html",context=data)

def note_type(request):
    note_obj = Note.objects.all().order_by('id')
    data = {"notes":note_obj}
    return render(request,"type.html",context=data)


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
    if request.method == 'POST':
        form_obj = NoteForm(instance=note_obj, data=request.POST)
        if form_obj.is_valid():
            form_obj.save()
    form_obj = NoteForm(instance=note_obj)
    data = {'form':form_obj}
    return render(request,'edit_note.html',context=data)

def delete_note(request,pk):    
    note_obj = Note.objects.get(id=pk)
    note_obj.delete()
    return redirect(home)
    
def delete_all(request):
    note_obj = Note.objects.get()
    note_obj.delete()
    return redirect(home)

def register(request):
    if request.method == 'POST':
        password = request.POST.get('password')
        hash_password = make_password(password)
        data = request.POST.copy()
        data['password'] = hash_password
        user_form_obj = UserForm(data = data)
        if user_form_obj.is_valid():
            user_form_obj.save()
    user_form_obj = UserForm()
    data = {'form':user_form_obj}    
    return render(request,'register.html',context=data)   

def user_login(request):
    if request.method == 'POST':
        user_username = request.POST.get('username')
        user_password = request.POST.get('password')
        
        user = authenticate(username=user_username,password=user_password)
        
        if user!= None:
            login(request,user)
            return redirect('home')
            
    user_form_obj = UserForm()
    data = {'form':user_form_obj}    
    return render(request,'login.html',context=data)   
    