from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import PostForm
# Create your views here.

def show_posts(request):
    posts = Book.objects.filter(status='active')
    return render(request, 'main.html', {'posts': posts})


def add_post(request, *args, **kwargs):
    if request.method == 'GET':
        forms = PostForm()
        return  render(request, 'add_post.html', {'forms': forms})
    elif request.method == 'POST':
        forms = PostForm(data=request.POST)
        if forms.is_valid():
            post = Book.objects.create(author=forms.cleaned_data['author'],
                                         email=forms.cleaned_data['email'],
                                         text=forms.cleaned_data['text']
                                         )
            return redirect('show_posts')
        else:
            return render(request, 'add_post.html',{'forms': forms})

# def article_update_view(request, pk):
#
#     article = get_object_or_404(Article, pk=pk)
#
#     if request.method == 'GET':
#
#         form = ArticleForm(initial={
#
#             'title': article.title,
#
#             'text': article.text,
#
#             'author': article.author
#
#         })
#
#         return render(request, 'update.html', context={'form': form, 'article': article})
#
#     elif request.method == 'POST':
#
#         form = ArticleForm(data=request.POST)
#
#         if form.is_valid():
#
#             article.title = form.cleaned_data['title']
#
#             article.text = form.cleaned_data['text']
#
#             article.author = form.cleaned_data['author']
#
#             article.save()
#
#             return redirect('article_view', pk=article.pk)
#
#         else:
#
#             return render(request, 'update.html', context={'form': form, 'article': article})



def edit_post(request, pk):
    post = get_object_or_404(Book, pk=pk)
    if request.method == 'GET':
        forms = PostForm(
            initial={
                'author': post.author,
                'email': post.email,
                'text': post.text,
            }
        )
        return  render(request, 'edit.html', {'forms': forms})
    elif request.method == 'POST':
        forms = PostForm(data=request.POST)
        if forms.is_valid():
            post = Book.objects.create(author=forms.cleaned_data['author'],
                                         email=forms.cleaned_data['email'],
                                         text=forms.cleaned_data['text']
                                         )
            return redirect('show_posts')
        else:
            return render(request, 'edit.html',{'forms': forms})