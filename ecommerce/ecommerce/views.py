from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ContactForm, LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, get_user_model

def home_page(request):
    return HttpResponse("<h1>Hello World!</h1>")

def home(request):
    context = {

        "title": "Home",
        "content": "Welcome to Home Page.",
        "premium_content": "You are God!"
    }
    return render(request, "home.html", context)


def about(request):
    context = {

        "title": "About",
        "content" : "Welcome to About Page."
    }
    return render(request, "home.html", context)


def contact(request):
    contact_form = ContactForm(request.POST or None)
    context = {

        "title": "Contact",
        "content" : "Welcome to Contact Page.",
        "form": contact_form
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    # if request.method == "POST":
    #     print(request.POST)
    #     print(request.POST.get("full_name"))
    return render(request, "contact.html", context)


def login_user(request):
    form = LoginForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print(request.user.is_authenticated)
            login(request, user)
            context["form"] = LoginForm()
            return redirect("/")
        else:
            print("Error")

    return render(request, "login.html", context)

User = get_user_model()
def register_user(request):
    form = RegisterForm(request.POST or None)
    context = {

        "form": form
    }
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        email = form.cleaned_data.get("email")
        new_user = User.objects.create_user(username, email, password)
        print(new_user)

    return render(request, "register.html", context)