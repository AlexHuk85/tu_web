from django import forms
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.mail import send_mail, get_connection
from django.conf import settings
from phonenumber_field.formfields import PhoneNumberField

class ContactForm(forms.Form):
    yourname = forms.CharField(max_length=100, label='Your Name')
    email = forms.EmailField(required=False, label='Your Email Address')
    phone_number = PhoneNumberField(label='Your Phone Number')
    message = forms.CharField(widget=forms.Textarea)

def contact(request):
    submitted = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            email_from = settings.EMAIL_HOST_USER
            email_to = cd.get('email', 'siteowner@example.com')
            #assert False
            #con = get_connection('django.core.mail.backends.console.EmailBackend')
            send_mail(
                cd['subject'],
                cd['message'],
                email_from,
                [email_to, 'alex.huk85@gmail.com']
                #connection=con
            )
            return HttpResponseRedirect('/contact?submitted=True')
    else:
        form = ContactForm()
        if 'submitted' in request.GET:
            submitted = True

    return render(request,
        'contact/contact.html',
        {'form': form, 'submitted': submitted})