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



from django import forms
from .models import StartupPitchApplication

class StartupPitchForm(forms.ModelForm):
    class Meta:
        model = StartupPitchApplication
        fields = ['full_name', 'email', 'phone', 'company_name', 'website', 'package']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Full Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone or WhatsApp'}),
            'company_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Company Name'}),
            'website': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Company Website'}),
            'package': forms.Select(attrs={'class': 'form-select'}),
        }

# forms.py
class StartupPitchForm(forms.ModelForm):
    class Meta:
        model = StartupPitchApplication
        fields = ['full_name', 'email', 'phone', 'company_name', 'website', 'package']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            css_class = 'form-select' if field.widget.__class__.__name__ == 'Select' else 'form-control'
            field.widget.attrs.update({'class': css_class})
