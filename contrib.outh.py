from django import forms
from django.contrib.auth import get_user_model

class LoginForm(forms.Form):
email = forms.EmailField()
password = forms.CharField(widget=forms.PasswordInput)






from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm

def user_login(request):
if request.method == "POST":
form = LoginForm(request.POST)
if form.is_valid():
email = form.cleaned_data["email"]
password = form.cleaned_data["password"]
user = authenticate(request, email=email, password=password)
if user is not None:
login(request, user)
return redirect("home")
else:
form.add_error(None, "Неверный логин или пароль")
else:
form = LoginForm()
return render(request, "login.html", {"form": form})







from django.urls import path
from .views import user_login

urlpatterns = [
path("login/", user_login, name="login"),
]






<form method="post">
{% csrf_token %}
{{ form.as_p }}
<button type="submit">Войти</button>
</form>
