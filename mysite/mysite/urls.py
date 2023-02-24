"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from todo import views
from todo import todos
from photo import photo


urlpatterns = [
    path('', views.home),
    path('admin/', admin.site.urls),
    path('todo/', todos.index, name='index'),
    path('todo/delete', todos.delete, name='index'),
    path('todo/add', views.add, name='index'),
    path('todo/hello', views.hello, name='index'),
    path('todo/karan', views.karan, name='index'),
    path('todo/karan-saran', todos.karan, name='index'),
    path('todo/create', todos.create, name='index'),
    path('photos/', photo.index, name='index'),
    path('photos/create', photo.create, name='index'),
    
]
