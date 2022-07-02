
from django import forms
from django.forms import widgets



class PostForm(forms.Form):

    author = forms.CharField(max_length=40, required=True, label='имя', widget=forms.TextInput(attrs={'placeholder':'name'}))
    email = forms.EmailField(max_length=200, required=True, label='email', widget=forms.TextInput(attrs={'placeholder':'email'}))
    text = forms.CharField(max_length=3000, required=True, label='Text', widget=widgets.Textarea)