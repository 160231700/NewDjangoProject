from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse
from .models import Ticket
from .forms import CustomUserCreationForm, TicketForm
from datetime import time, timedelta, datetime, date


#Define any extra functions up here
def calculate_price(arrival_time, departure_time):
    """Calculates the price based on arrival and departure times."""
    hours = (departure_time.hour - arrival_time.hour) + (1 if departure_time.minute > 0 else 0)
    return hours * 1.49


# Create your views here.


#Views for the website/ template
def index(request):
    return render(request,'website/index.html')

def information(request):
    return render(request,'website/information.html')

def dashboard(request):
    return render(request, "website/dashboard.html")

def ticket(request):
    print("Ticket accessed")
    if request.method == 'POST':
        print("Post method")
        print(request.POST.get('Arrival_Time'))
        
        updated_request = request.POST.copy()
        updated_request.update({'User':request.user})
        form = TicketForm(updated_request)
        if form.is_valid():
            print("Form is valid")
            ticket = form.save(commit=False)
            arrival_time = form.cleaned_data['Arrival_Time']
            departure_time = form.cleaned_data['Departure_Time']
            ticket.Price = calculate_price(arrival_time, departure_time)
            ticket.save()
            print("Redirecting")
            return redirect(reverse('index'))
        else:
            print(form.errors) 
    else:
        form = TicketForm()  # Just create the empty form
    return render(request, 'website/ticket.html', {'form': form})

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