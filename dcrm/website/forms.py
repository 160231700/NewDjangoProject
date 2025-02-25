from django.contrib.auth.forms import UserCreationForm
from django import forms 
from .models import Ticket  # Import your Ticket model


#Form for user creation
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email",)

#Ticket form
class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket #The model called on in models.py
        #Specify the fields
        fields = ['Quantity', 'Arrival_Time', 'Departure_Time', 'Booking_Date', 'Price','User']

        widgets = {
            'Quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'Arrival_Time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'Departure_Time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'Booking_Date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'Price' :forms.HiddenInput(attrs={'required':False}),
            'User' :forms.HiddenInput(attrs={'required':False}),

        }
        #Labels will show up on the front-end. Descriptions for the user.
        labels = {
            'Quantity': 'Number of People',
            'Arrival_Time': 'Arrival Time',
            'Departure_Time': 'Departure Time',
            'Booking_Date': 'Booking Date',
        }

        help_texts = {
            'Quantity': 'Enter the number of people for this ticket.',
            'Arrival_Time': 'Select the arrival time.',
            'Departure_Time': 'Select the departure time.',
            'Booking_Date': 'Select the date',
        }

        error_messages = {
            'Quantity': {
                'required': 'Please enter the number of people.',
                'invalid': 'Please enter a valid number.'
            }
        }

