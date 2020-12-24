from .models import Notes
from django.forms import ModelForm, TextInput, Textarea
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class NotesForm(ModelForm):
    class Meta:
        model = Notes
        user = User
        fields = ['author', 'title', 'note']
        widgets = {
            "title": TextInput(attrs={ "class": 'form-control', "placeholder": 'Заголовок'}),
            "note":  Textarea (attrs={ "class": 'form-control', "placeholder": 'Описание'}),
        }


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name']
