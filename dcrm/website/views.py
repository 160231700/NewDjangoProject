from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse
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
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.User = request.User
            arrival_time = form.cleaned_data['Arrival_Time']
            departure_time = form.cleaned_data['Departure_Time']
            ticket.Price = calculate_price(arrival_time, departure_time)
            ticket.save()
            return redirect('ticket_success')
    else:
        form = TicketForm()
        if 'Arrival_Time' in request.GET: # Check if Arrival Time is set
            arrival_time_str = request.GET.get('Arrival_Time')
            try:
                arrival_time = time.fromisoformat(arrival_time_str)
                departure_times = []
                for i in range(1, 13): # Generate up to 12 hours ahead
                    departure_time = (datetime.combine(date.today(), arrival_time) + timedelta(hours=i)).time()
                    departure_times.append((departure_time, departure_time.strftime('%H:%M'))) # Format for display
                form.fields['Departure_Time'].choices = departure_times
            except ValueError:
                # Handle invalid arrival time format
                pass
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