from django.contrib import admin
from django.urls import path
from Home import views
urlpatterns = [
       path("",views.index,name='Home'),
       path("about",views.about,name='Home'),
       path("services",views.services,name='Home'),
       path("contact",views.contact,name='Home')
]