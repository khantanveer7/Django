from django.http import HttpResponse , request
from home.models import Blog
from django.shortcuts import render



# Create your views here.

# def blog(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

def blog(request):
    blogs = Blog.objects.all()
    context = {'blogs': blogs}
    return render(request, 'blog.html' , context)

def post(request , slug):
    blogs = Blog.objects.filter(slug=slug).first()
    context = {'blogs': blogs}
    return render(request, 'post.html' , context)