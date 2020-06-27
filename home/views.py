from django.shortcuts import render 
from django.http import HttpResponse , request
from home.models import Contact
from home.models import Blog



# Create your views here.

# def home(request):
#     return render(request,'index.htm' )

def home(request):
    # return HttpResponse("THIS IS FIRST WEB ON DJANGO")
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        desc = request.POST['desc']
       # print(name , email , desc)
        contact = Contact(name = name , email = email, desc = desc)
        contact.save()
    return render(request, 'contact.html')

# def blog(request):
#     blogs = Blog.objects.all()
#     context = {'blogs': blogs}
#     return render(request, 'blog.html' , context)

# def post(request , slug):
#     blogs = Blog.objects.filter(slug = slug).first()
#     context = {'blogs': blogs}
#     return render(request, 'post.html' , context)

# def search(request):
#     return render(request, 'search.html')

