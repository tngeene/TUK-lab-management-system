from django.http import request
from core.utils import generate_random_string
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string



def send_activation_email(user, password,request):
    current_site = get_current_site(request)
    subject = 'TuK Account activation'
    message = render_to_string('account/password_reset_email.html', {
        'user': user.first_name,
        'email': user.email,
        'domain': current_site.domain,
        'password': password,
        })
    print(request)
    email = EmailMultiAlternatives(
    subject, message, from_email='tuklabs@tuk.ac.ke', to=[user.email, ])
    email.content_subtype = 'html'
    email.send()