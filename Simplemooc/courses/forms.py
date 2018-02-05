from django import forms
from django.core.mail import send_mail
from django.conf import settings

class ContactCourse(forms.Form):
    name = forms.CharField(label='Nome',max_length=100)
    email = forms.EmailField(label='Email')
    message = forms.CharField(label='Mensagem/Dúvidas',widget=forms.Textarea)

    def send_mail(self, course):
        subject = 'Dúvida - [%s]' % course
        message = 'Name: %(name)s; Email: %(email)s; %(message)s'
        context = {
            'Name': self.cleaned_data['name'],
            'Email': self.cleaned_data['email'],
            'message': self.cleaned_data['message'],
            }
        message = message % context
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [settings.CONTACT_EMAIL])
