from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator, EmailValidator
from django.forms import CharField
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
        ('Driveway', 'Driveway'),
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
    car_year = forms.ChoiceField(label="Year", choices=car_year_choices, widget=forms.Select(attrs={'class': 'nice-select'}))
    car_make = forms.CharField(max_length=255, label="Make")
    car_model = forms.CharField(max_length=255, label="Model")
    car_run = forms.ChoiceField(label="Running Condition", choices=car_run_choices,
                                widget=forms.Select(attrs={'class': 'nice-select'}))
    type_of_carrier = forms.CharField(max_length=255, label="Type of Carrier")
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
        input_formats=['%m-%d-%Y']
    )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email.endswith('@gmail.com'):
            raise ValidationError("Email must end with @gmail.com")
        if len(email) > 64:
            raise ValidationError("Email must be 64 characters or less!")
        elif len(email) < 16:
            raise ValidationError("Email can not be less than 6 characters!")
        return email

# class FooterForm(forms.Form):
#     call_number = forms.CharField(max_length=20)   
#     def clean_phone_number(self):
#         phone_number = self.cleaned_data.get('phone_number')
#         if not phone_number.startswith('+'):
#             raise ValidationError("Phone number must start with +")
#         if len(phone_number) > 32:
#             raise ValidationError("Phone number must be 32 characters or less!")
#         elif len(phone_number) < 6:
#             raise ValidationError("Phone number can not be less than 6 characters!")
#         return phone_number
