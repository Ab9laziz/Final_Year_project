from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string



def send_welcome_email(user, password, request):
    current_site = get_current_site(request)
    subject = 'Pangani Youth Soccer Academy Portal Account Activation'
    message = render_to_string('account/emails/welcome.html', {
        'user': user.first_name,
        'email': user.email,
        'domain': current_site.domain,
        'password': password,
        })
    email = EmailMultiAlternatives(
    subject, message, from_email='admin@pysa.com', to=[user.email, ])
    email.content_subtype = 'html'
    email.send()

def send_suspension_email(user, request):
    current_site = get_current_site(request)
    subject = f'{current_site.name} Account Suspension'
    message = render_to_string('account/emails/account_deactivated.html', {
        'user': user.first_name,
        'domain': current_site.domain,
        'site_name': current_site.name.title(),
        })
    print(request)
    email = EmailMultiAlternatives(
    subject, message, from_email='admin@pysa.com', to=[user.email, ])
    email.content_subtype = 'html'
    email.send()

def send_activation_email(user, request):
    current_site = get_current_site(request)
    subject = f'{current_site.name} Account Activation'
    message = render_to_string('account/emails/account_reactivated.html', {
        'user': user.first_name,
        'domain': current_site.domain,
        'site_name': current_site.name.title(),
        })
    print(request)
    email = EmailMultiAlternatives(
    subject, message, from_email='admin@pysa.com', to=[user.email, ])
    email.content_subtype = 'html'
    email.send()
