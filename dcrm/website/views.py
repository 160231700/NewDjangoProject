from django.shortcuts import render
from django.contrib.auth import login
# Remove: from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.urls import reverse
from .forms import CustomUserCreationForm

# Create your views here.


# Views for the website/ template
def index(request):
    return render(request,'website/index.html')

def information(request):
    return render(request,'website/information.html')

def dashboard(request):
    return render(request, "website/dashboard.html")


# Views for the registration/ template

#Creates a new user
def sign_up(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        #Validates the form filled out by the user
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("dashboard"))
    #If the request isn't a post (The form hasn't been sent) it'll send a form to the user
    else:
        form = CustomUserCreationForm()
    return render(request, "registration/sign_up.html", {"form": form})