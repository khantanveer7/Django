from django.contrib import admin
from django.urls import include, path
from . import views



urlpatterns = [
    path("", views.blog, name = 'Blog'),
    # path('<slug:slug>/', views.post.as_view(), name='post'),
    path('<slug>/', views.post, name='post'),
]
