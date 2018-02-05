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

'''
    ERRO:
    KeyError at /cursos/Django2-Python/

'name'

Request Method: 	POST
Request URL: 	http://127.0.0.1:8000/cursos/Django2-Python/
Django Version: 	2.0.1
Exception Type: 	KeyError
Exception Value:

'name'

Exception Location: 	/Users/Son/Documents/Python/django/RedeSocial/Simplemooc/Simplemooc/courses/forms.py in send_mail, line 18
Python Executable: 	/Users/Son/Documents/Python/django/RedeSocial/venv/bin/python3
Python Version: 	3.6.1
Python Path:

['/Users/Son/Documents/Python/django/RedeSocial/Simplemooc',
 '/Users/Son/Documents/Python/django/RedeSocial/venv/lib/python36.zip',
 '/Users/Son/Documents/Python/django/RedeSocial/venv/lib/python3.6',
 '/Users/Son/Documents/Python/django/RedeSocial/venv/lib/python3.6/lib-dynload',
 '/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6',
 '/Users/Son/Documents/Python/django/RedeSocial/venv/lib/python3.6/site-packages']

Server time: 	Seg, 5 Fev 2018 11:21:23 +0000
'''
