from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator, EmailValidator

class ModalForm(forms.Form):
    email = forms.EmailField(validators=[EmailValidator(message="Invalid email address.")])
    phone_number = forms.CharField(max_length=20, validators=[
        RegexValidator(
            regex=r'^\+\d{1,20}$',
            message="Phone number must be in the format +1234567890."
        )
    ])

class ContactForm(forms.Form):
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=20)
    fullname = forms.CharField(max_length=255)
    pick_up = forms.CharField(max_length=255)
    delivery = forms.CharField(max_length=255)
    vehicle_type = forms.CharField(max_length=255)
    transport_type = forms.CharField(max_length=255)
    car_info = forms.CharField(max_length=255)


    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email.endswith('@gmail.com'):
            raise ValidationError("Email must end with @gmail.com")
        if len(email) > 64:
            raise ValidationError("Email must be 64 characters or less!")
        elif len(email) < 16:
            raise ValidationError("Email can not be less than 6 characters!")
        return email
    
    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if not phone_number.startswith('+'):
            raise ValidationError("Phone number must start with +")
        if len(phone_number) > 32:
            raise ValidationError("Phone number must be 32 characters or less!")
        elif len(phone_number) < 6:
            raise ValidationError("Phone number can not be less than 6 characters!")
        return phone_number

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