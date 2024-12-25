from django.forms import ModelForm,TextInput,Select,Textarea
from django import forms
from.models import Note

class NoteForm(ModelForm):
    class meta:
        model = Note
        fields = ['name','type','description']
        widgets = {
            'name':TextInput(attrs={'class':'form-control'}),
            'type':Select(attrs={'class':'form-select'}),
            'description': Textarea(attrs={'class':'form-control'})                                
                                    
             }