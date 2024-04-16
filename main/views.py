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
        fullname = request.POST.get('fullname', None)
        email = request.POST.get('email', None)
        phone_number = request.POST.get('phone_number', None)
        pickup = request.POST.get('pickup', None)
        delivery = request.POST.get('delivery', None)
        vehicle_type = request.POST.get('vehicle_type', None)
        transport_type = request.POST.get('transport_type', None)
        car_info = request.POST.get('car_info', None)

        subject = 'Thank you for contacting us!'
        message = f'Hi {fullname},\n\nThank you for contacting us. We have received your inquiry and will get back to you shortly.'
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [email]

        send_mail(subject, message, from_email, recipient_list)

        admin_email = settings.RECEIVER_EMAIL
        admin_subject = 'New Inquiry Received'
        admin_message = f'New inquiry received from {fullname}. Email: {email}, Phone: {phone_number}'
        send_mail(admin_subject, admin_message, from_email, [admin_email])

        return redirect('contact')
