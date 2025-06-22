from django import forms

class RegistrationForm(forms.Form):
    ROLE_CHOICES = [
        ('Exhibitor', 'Exhibitor'),
        ('Attendee', 'Attendee'),
        ('Sponsor', 'Sponsor'),
    ]

    role = forms.ChoiceField(choices=ROLE_CHOICES, label="I want to be a *")
    company_name = forms.CharField(label="Your Company Name *", max_length=100)
    name = forms.CharField(label="Your Name *", max_length=100)
    whatsapp = forms.CharField(label="Your WhatsApp Number *", max_length=20)
    email = forms.EmailField(label="Your Email ID *")
