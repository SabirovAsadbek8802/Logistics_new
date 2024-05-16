from django.shortcuts import render, redirect
from django.views import View
from .forms import ContactForm, ModalForm
from django.conf import settings
from django.core.mail import send_mail


class HomeView(View):
    template_name = 'index.html'
    context = {
        'form': ContactForm(),
        'form_modal': ModalForm()
    }

    def get(self, request):
        return render(request, self.template_name, context=self.context)

    def post(self, request):
        email = request.POST.get('email', None)
        phone_number = request.POST.get('phone_number', None)

        subject = 'Thank you for contacting us!'
        message = f'Hi {email},\n\nThank you for contacting us. We have received your inquiry and will get back to you shortly.'
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [email]

        send_mail(subject, message, from_email, recipient_list)

        admin_email = settings.RECEIVER_EMAIL
        admin_subject = 'New Inquiry Received'
        admin_message = f'Email: {email}, Phone: {phone_number}'
        send_mail(admin_subject, admin_message, from_email, [admin_email])

        return redirect('home')


class AboutView(View):
    template_name = 'about.html'

    def get(self, request):
        return render(request, self.template_name)


class ContactView(View):
    template_name = 'contact.html'
    context = {'form': ContactForm()}

    def get(self, request):
        return render(request, self.template_name, context=self.context)

    def post(self, request):
        email = request.POST.get('email', None)
        phone_number = request.POST.get('phone_number', None)
        first_name = request.POST.get('first_name', None)
        last_name = request.POST.get('last_name', None)
        car_type = request.POST.get('car_type', None)
        car_year = request.POST.get('car_year', None)
        car_make = request.POST.get('car_make', None)
        car_model = request.POST.get('car_model', None)
        car_run = request.POST.get('car_run', None)
        type_of_carrier = request.POST.get('type_of_carrier', None)
        origin_city = request.POST.get('origin_city', None)
        origin_state = request.POST.get('origin_state', None)
        origin_zip = request.POST.get('origin_zip', None)
        destination_city = request.POST.get('destination_city', None)
        destination_state = request.POST.get('destination_state', None)
        destination_zip = request.POST.get('destination_zip', None)
        comment = request.POST.get('comment', None)
        proposed_ship_date = request.POST.get('proposed_ship_date', None)

        # Create the subject and message for the user
        fullname = f'{first_name} {last_name}'
        subject = 'Thank you for contacting us!'
        message = f'Hi {fullname},\n\nThank you for contacting us. We have received your inquiry and will get back to you shortly.'
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [email]

        # Send the email to the user
        send_mail(subject, message, from_email, recipient_list)
        print("mail sent 1")
        admin_subject = 'New Inquiry Received'
        admin_message = (
            f'New inquiry received from {fullname}.\n'
            f'Email: {email}\n'
            f'Phone: {phone_number}\n'
            f'Car Type: {car_type}\n'
            f'Car Year: {car_year}\n'
            f'Car Make: {car_make}\n'
            f'Car Model: {car_model}\n'
            f'Running Condition: {car_run}\n'
            f'Type of Carrier: {type_of_carrier}\n'
            f'Origin: {origin_city}, {origin_state} {origin_zip}\n'
            f'Destination: {destination_city}, {destination_state} {destination_zip}\n'
            f'Proposed Ship Date: {proposed_ship_date}\n'
            f'Comment: {comment}'
        )

        # Send the email to the admin
        send_mail(admin_subject, admin_message, from_email, [
            "support@weproautotransport.com",
            "hi@moorfo.uz",
            "leads@wpa.msgplane.com"
        ])
        print("mail sent")

        return redirect('contact')
