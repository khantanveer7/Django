from django.contrib import admin
from django.urls import include, path
from . import views



urlpatterns = [
    path("", views.blog, name = 'Blog'),
    path("<str:slug>", views.post, name = 'Post'),

]
