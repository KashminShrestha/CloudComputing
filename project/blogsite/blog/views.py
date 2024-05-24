from django.shortcuts import render
from blog.models import Blog

# Create your views here.

def index(request):
    blogs = Blog.objects.all()
    return render(request, 'index.html', {'blogs': blogs})