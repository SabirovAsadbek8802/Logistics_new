from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator, EmailValidator
from django.forms import CharField
from captcha.fields import CaptchaField
import datetime


class ModalForm(forms.Form):
    email = forms.EmailField(validators=[EmailValidator(message="Invalid email address.")])
    phone_number = forms.CharField(max_length=20, validators=[
        RegexValidator(
            regex=r'^\+\d{1,20}$',
            message="Phone number must be in the format +1234567890."
        )
    ])


class ContactForm(forms.Form):
    car_types = [
        ('Car', 'Car'),
        ('SUV', 'SUV'),
        ('Pickup', 'Pickup'),
        ('Motorcycle', 'Motorcycle'),
        ('Van', 'Van'),
        ('ATV', 'ATV'),
        ('RV', 'RV'),
        ('Boat', 'Boat'),
        ('Heavy', 'Heavy'),
        ('Equipment', 'Equipment'),
        ('Large', 'Large'),
        ('Yacht', 'Yacht'),
        ('Other', 'Other')
    ]
    car_run_choices = [
        ('Open', 'Open'),
        ('Drive away', 'Drive away'),
        ('Enclosed', 'Enclosed'),
    ]

    current_year = datetime.datetime.now().year
    start_year = 2011
    car_year_choices = [(str(year), str(year)) for year in range(start_year, current_year + 1)]

    email = forms.EmailField(label="Email address")
    phone_number = forms.CharField(max_length=20, label="Phone number")
    first_name = forms.CharField(max_length=255, label="First Name")
    last_name = forms.CharField(max_length=255, label="Last Name")
    car_type = forms.ChoiceField(label="Type", choices=car_types, widget=forms.Select(attrs={'class': 'nice-select'}))
    car_year = forms.ChoiceField(label="Year", choices=car_year_choices,
                                 widget=forms.Select(attrs={'class': 'nice-select'}))
    car_make = forms.CharField(max_length=255, label="Make")
    car_model = forms.CharField(max_length=255, label="Model")
    car_run = forms.CharField(max_length=255, label="Running Condition")
    type_of_carrier = forms.ChoiceField(label="Type of Carrier", choices=car_run_choices,
                                        widget=forms.Select(attrs={'class': 'nice-select'}))
    origin_city = forms.CharField(max_length=255, label="Origin City")
    origin_state = forms.CharField(max_length=255, label="Origin State")
    origin_zip = forms.CharField(max_length=255, label="Origin Zip")
    destination_city = forms.CharField(max_length=255, label="Destination City")
    destination_state = forms.CharField(max_length=255, label="Destination State")
    destination_zip = forms.CharField(max_length=255, label="Destination Zip")
    comment = forms.CharField(max_length=255, label="Comment", widget=forms.Textarea())
    proposed_ship_date = forms.DateField(
        label="Proposed Ship Date",
        widget=forms.DateInput(format="%m-%d-%Y", attrs={'type': 'date'}),
    )
    captcha = CaptchaField(label="Type the characters you see in the picture above.")
