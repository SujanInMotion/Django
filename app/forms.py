from django.forms import ModelForm
from django import forms
from.models import Note
from django.contrib.auth.models import User

class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = ['name','type','description']
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'type':forms.Select(attrs={'class':'form-select'}),
            'description': forms.Textarea(attrs={'class':'form-control'})                             
                                    
            }
        
        
class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username','password']
        widgets = {         
            'username' : forms.TextInput(attrs={'class':'form-control mt-3'}),
            'password' : forms.PasswordInput(attrs={'class':'form-select mt-3'})                            
                                    
        }
        labels = {
            'username' : ('Username:')
        }
        help_texts = {
            'username':(),
        }