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
        form = ContactForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            car_type = form.cleaned_data['car_type']
            car_year = form.cleaned_data['car_year']
            car_make = form.cleaned_data['car_make']
            car_model = form.cleaned_data['car_model']
            car_run = form.cleaned_data['car_run']
            type_of_carrier = form.cleaned_data['type_of_carrier']
            origin_city = form.cleaned_data['origin_city']
            origin_state = form.cleaned_data['origin_state']
            origin_zip = form.cleaned_data['origin_zip']
            destination_city = form.cleaned_data['destination_city']
            destination_state = form.cleaned_data['destination_state']
            destination_zip = form.cleaned_data['destination_zip']
            comment = form.cleaned_data['comment']
            proposed_ship_date = form.cleaned_data['proposed_ship_date']

            fullname = f'{first_name} {last_name}'
            subject = 'Thank you for contacting us!'
            message = f'Hi {fullname},\n\nThank you for contacting us. We have received your inquiry and will get back to you shortly.'
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [email]

            send_mail(subject, message, from_email, recipient_list)

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
            send_mail(admin_subject, admin_message, from_email, [
                "support@weproautotransport.com",
                "hi@moorfo.uz",
                "leads@wpa.msgplane.com"
            ])
            print("mail sent")
            return redirect('contact')
        return render(request, self.template_name, context={'form': form})


