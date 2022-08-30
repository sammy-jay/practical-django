from django import forms
from django.core.mail import send_mail
import logging

logger = logging.getLogger(__name__)


class ContactUsForm(forms.Form):
    name = forms.CharField(label='Your name', max_length=100)
    message = forms.CharField(label='Your message',
                              max_length=100,
                              widget=forms.Textarea)

    def send_mail(self):
        logger.info('Sending mail to customer service')
        message = "From: {0}\n{1}".format(
            self.cleaned_data['name'],
            self.cleaned_data['message'])

        send_mail(
            subject="Site message",
            message=message,
            from_email="site@booktime.com",
            recipient_list=['customerservice@booktime.com'],
            fail_silently=False,
        )
