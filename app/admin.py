from django.contrib import admin

# Register your models here.
from .models import Note,NoteType

admin.site.register(Note)
admin.site.register(NoteType)
