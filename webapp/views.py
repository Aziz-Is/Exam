from django.shortcuts import render
from .models import Book
# Create your views here.

def show_posts(request):
    posts = Book.objects.filter(status='active')
    return render(request, 'main.html', {'posts': posts})