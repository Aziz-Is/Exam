"""guestbook URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from webapp.views import show_posts, add_post, edit_post, delete_post


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', show_posts, name="show_posts"),
    path('add/', add_post, name="add_post"),
    path('edit/<int:pk>', edit_post, name='edit_post'),
    path('delete/<int:pk>', delete_post, name='delete_post')
]
