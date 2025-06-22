from django.shortcuts import render

def home(request):
    return render(request, 'index.html')
from django.shortcuts import render

def about(request):
    return render(request, "about.html")

def book_now(request):
    return render(request, "book-now.html")

def coming_soon(request):
    return render(request, "coming-soon.html")



from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings

def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        full_message = f"""
        Name: {name}
        Email: {email}
        Phone: {phone}
        
        Message:
        {message}
        """

        send_mail(
            subject=subject or "New Contact Message",
            message=full_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.CONTACT_RECEIVER_EMAIL],
            fail_silently=False,
        )

        return redirect('contact_thanks')  # Make sure this exists
    return render(request, 'contact.html')


def contact_thanks(request):
    return render(request, 'contact_thanks.html')


def error_page(request):
    return render(request, "error.html")

def event_list(request):
    return render(request, "event_list.html")

def event_detail(request):
    return render(request, "event-detail.html")

def faq(request):
    return render(request, "faq.html")

def gallery(request):
    return render(request, "gallery.html")

def index(request):
    return render(request, "index.html")

def news_list(request):
    return render(request, "news-list.html")

def news_single(request):
    return render(request, "news-single.html")

def pricing(request):
    return render(request, "pricing.html")

def product_list(request):
    return render(request, "product-list.html")

def product_single(request):
    return render(request, "product-single.html")

def search_result(request):
    return render(request, "search-result.html")

def speaker_detail(request):
    return render(request, "speaker_detail.html")

def speaker_list(request):
    return render(request, "speaker_list.html")

def sponsers(request):
    return render(request, "sponsers.html")

def testimonial(request):
    return render(request, "testimonial.html")

def apply_speaker_view(request):
    if request.method == 'POST':
        your_name = request.POST.get('your_name')
        company_name = request.POST.get('company_name')
        total_employees = request.POST.get('total_employees')
        speaker_name = request.POST.get('speaker_name')
        email = request.POST.get('email')

        # Updated WhatsApp field
        isd = request.POST.get('isd_code')
        number = request.POST.get('whatsapp_number')
        whatsapp_full = f"{isd}{number}"

        linkedin = request.POST.get('linkedin')
        slot = request.POST.get('slot')

        print("Speaker Application Received:", {
            "Your Name": your_name,
            "Company": company_name,
            "Employees": total_employees,
            "Speaker": speaker_name,
            "Email": email,
            "WhatsApp": whatsapp_full,
            "LinkedIn": linkedin,
            "Slot": slot
        })

        messages.success(request, "Your speaker application has been received!")
        return redirect('thank_you')

    return render(request, 'apply_speaker.html')


def thank_you_view(request):
    return render(request, 'thank_you.html')

def venue_detail(request):
    return render(request, 'venue_section.html')
def become_sponsor(request):
    return render(request, 'become_sponsor.html')

def exhibit(request):
    reasons = [
        {"text": "Showcase Your Innovative AI Product to a Worldwide Audience", "color": "#ff6b6b"},
        {"text": "Visitors from 20+ Countries", "color": "#f8a34e"},
        {"text": "Key Decision Makers (Entrepreneurs, CEOs, C-Level Executives, etc.)", "color": "#ffd166"},
        {"text": "Generate High-Quality Leads", "color": "#06d6a0"},
        {"text": "Launch Your Product to the Global Market", "color": "#1dd3b0"},
        {"text": "Prefix Appointments with Quality Buyers", "color": "#118ab2"},
        {"text": "Participate in Awards and Network with Winners", "color": "#73c2fb"},
    ]
    return render(request, 'exhibit.html', {'reasons': reasons})


def book_ticket(request):
    # Combine types with prices to avoid bracket-access errors in templates
    ticket_columns = [
        ("Regular", "USD 60"),
        ("Standard", "USD 204"),
        ("Premium", "USD 208"),
        ("VIP", "USD 590"),
        ("Limited Edition", "USD 959"),
    ]

    features = [
        ("Access to Expo", ["✔", "✔", "✔", "✔", "✔"], False),
        ("Access to Speaker Sessions", ["5 Sessions", "10 Sessions", "All Sessions", "All Sessions", "All Sessions"], False),
        ("Access to Networking Sessions", ["✔", "✔", "✔", "✔", "✔"], False),
        ("Access to VIP Lounge", ["✘", "✘", "✘", "✔", "✔"], False),
        ("Priority Seating", ["✘", "✘", "✘", "✔", "✔"], False),
        ("F & B - Coffee & Snacks (2 days)", ["✘", "✘", "✘", "✔", "✔"], False),
        ("Networking Lunch (2 days)", ["✘", "✘", "✘", "✔", "✔"], False),
        ("Entry Award Gala Ceremony", ["✘", "✘", "✘", "✘", "✔"], False),
        ("Networking Dinner & Cocktails @ Award Ceremony", ["✘", "✘", "✘", "✘", "✔"], False),
        ("Prefix Appointment Fixing", ["10 meetings", "upto 20", "upto 30", "upto 50", "upto 100"], True),
        ("Priority Registration", ["✘", "✘", "✔", "✔", "✔"], True),
        ("Network with Speakers", ["✔", "✔", "✔", "✔", "✔"], False),
        ("Network with VIP Participants", ["✘", "✘", "✔", "✔", "✔"], False),
    ]

    return render(request, "book_ticket.html", {
        "ticket_columns": ticket_columns,
        "features": features,
    })


def become_a_sponsor(request):
    return render(request, 'become_a_sponsor.html')


from django.shortcuts import render
from django import forms

class StartupPitchForm(forms.Form):
    full_name = forms.CharField(label="Full Name", widget=forms.TextInput(attrs={'class': 'form-control'}))
    company_name = forms.CharField(label="Company Name", widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="E-Mail ID", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    whatsapp = forms.CharField(label="WhatsApp Number", widget=forms.TextInput(attrs={'class': 'form-control'}))
    website = forms.URLField(label="Company Website", widget=forms.URLInput(attrs={'class': 'form-control'}))
    country = forms.CharField(label="Company Located", widget=forms.TextInput(attrs={'class': 'form-control'}))
    package = forms.ChoiceField(label="Package", widget=forms.Select(attrs={'class': 'form-select'}))

def startup_pitching_view(request):
    package_options = [
        ("Startup Pitching + 1 Regular Ticket", "$680"),
        ("Startup + 5 Regular Tickets + Table Top", "$880"),
        ("Startup Pitching + 5 Regular Tickets", "$860"),
        ("Startup Pitching + 2 VIP Tickets", "$1,175"),
        ("Startup Pitching + 3 VIP Tickets", "$1,400"),
        ("Startup Pitching + 5 VIP Tickets", "$1,679"),
    ]

    packages = [
        {"title": "Startup Pitching + 1 Regular Ticket", "price": "680"},
        {"title": "Startup + 5 Regular Tickets + Table Top", "price": "880", "original_price": "2000", "recommended": True},
        {"title": "Startup Pitching + 5 Regular Tickets", "price": "860", "original_price": "980"},
        {"title": "Startup Pitching + 2 VIP Tickets", "price": "1175", "original_price": "1270"},
        {"title": "Startup Pitching + 3 VIP Tickets", "price": "1400", "original_price": "1565"},
        {"title": "Startup Pitching + 5 VIP Tickets", "price": "1679", "original_price": "2155"},
    ]

    submitted = False

    if request.method == 'POST':
        form = StartupPitchForm(request.POST)
        form.fields['package'].choices = [(p[0], f"{p[0]} - {p[1]}") for p in package_options]
        if form.is_valid():
            submitted = True
    else:
        form = StartupPitchForm()
        form.fields['package'].choices = [(p[0], f"{p[0]} - {p[1]}") for p in package_options]

    return render(request, "startup_pitching.html", {
        "form": form,
        "packages": packages,
        "submitted": submitted,
    })



from django.shortcuts import render, redirect
from django.core.mail import send_mail  # optional if you want notifications
from django.contrib import messages

def register_media_partner(request):
    if request.method == 'POST':
        partner_type = request.POST.get('partner_type')
        events = request.POST.getlist('events')
        company_name = request.POST.get('company_name')
        name = request.POST.get('name')
        email = request.POST.get('email')
        whatsapp = request.POST.get('whatsapp')
        country = request.POST.get('country')
        address = request.POST.get('address')

        # Process/save/send/store logic here
        print("Received:", partner_type, events, company_name, name, email, whatsapp, country, address)

        messages.success(request, "Thank you for registering!")
        return redirect('register_media_partner')

    return render(request, 'media_partner_form.html')

    
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegistrationForm

def exhibit_registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # You can process the form here, save to DB or send email
            messages.success(request, 'Registration submitted successfully!')
            return redirect('exhibit_registration')
    else:
        form = RegistrationForm()
    return render(request, 'myApp/exhibit_registration.html', {'form': form})
