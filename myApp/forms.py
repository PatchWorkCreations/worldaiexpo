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

#separate exhibitor form
class StartupPitchForm(forms.ModelForm):
    class Meta:
        model = StartupPitchApplication
        fields = ['full_name', 'email', 'phone', 'company_name', 'website', 'package']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            css_class = 'form-select' if field.widget.__class__.__name__ == 'Select' else 'form-control'
            field.widget.attrs.update({'class': css_class})

#separate exhibitor
from django import forms

EXHIBITOR_TIERS = [
    ("startup",    "Startup Booth — ₱28,880 (Early) / ₱35,880"),
    ("growth",     "Growth Booth — ₱47,880 (Early) / ₱52,880"),
    ("enterprise", "Enterprise Booth — ₱66,880 (Early) / ₱77,880"),
]

PRICING_CHOICES = [("early", "Early"), ("regular", "Regular")]

class ExhibitorApplicationForm(forms.Form):
    company_name   = forms.CharField(max_length=150)
    company_size   = forms.ChoiceField(choices=[("1-20","1–20"),("21-100","21–100"),("100+","100+")])
    industry       = forms.CharField(max_length=120, required=False)
    website        = forms.URLField(required=False)
    contact_name   = forms.CharField(max_length=120)
    email          = forms.EmailField()
    phone          = forms.CharField(max_length=40, required=False)

    tier           = forms.ChoiceField(choices=EXHIBITOR_TIERS, widget=forms.RadioSelect)

    add_logo       = forms.BooleanField(required=False, label="Logo on website & stage screen")
    add_power      = forms.BooleanField(required=False, label="Power outlet & extension")
    add_leads      = forms.BooleanField(required=False, label="Lead scanner access")

    notes          = forms.CharField(widget=forms.Textarea(attrs={"rows":4}), required=False)
    agree          = forms.BooleanField(label="I agree to the Exhibitor Terms & Privacy")

    # hidden, set by JS; server still recomputes totals
    pricing_mode   = forms.ChoiceField(choices=PRICING_CHOICES, widget=forms.HiddenInput, initial="early")
    total_price    = forms.IntegerField(widget=forms.HiddenInput, required=False)
