from celery import shared_task
from django.contrib.auth.tokens import default_token_generator
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from account.models import User
from core import settings


def send_activation_email(user_id, site=settings.SITE_URL):
    user = get_object_or_404(User, pk=user_id)
    token = default_token_generator.make_token(user)
    uid = urlsafe_base64_encode(force_bytes(user_id))

    active_email_url = reverse_lazy('activate', kwargs={'uidb64': uid, 'token': token})
    subject = 'Activate your account on BookShop'
    message = (f'Thank you for registering on the BookShop website. To activate your account, please follow the '
               f'link: {site}/{active_email_url}')
    return user.email_user(subject=subject, message=message)


@shared_task
def activation_email_task(user_id):
    return send_activation_email(user_id)
