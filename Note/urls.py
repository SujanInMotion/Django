"""
URL configuration for Note project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path('',home,name='home'),
    path('note-type/',note_type),
    path('admin/', admin.site.urls), 
    path('create-note/', create_note,name="create-note"),
    path('edit-note/<int:pk>/',edit_note,name='edit-note'),
    path('delete-note/<int:pk>/', delete_note,name='delete-note'),
    path('delete-all/', delete_all,name='delete-all'),
    path('register/',register,name='register'),
     path('login/',user_login,name='login'),

]
