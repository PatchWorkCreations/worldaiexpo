from django.shortcuts import render

def home(request):
    return render(request, 'index.html')


from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings

def send_message_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('message')

        full_message = f"""
        Name: {name}
        Email: {email}
        Phone: {phone}

        Message:
        {message}
        """

        send_mail(
            subject="New Inquiry from Website",
            message=full_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.CONTACT_RECEIVER_EMAIL],  # set this in settings.py
            fail_silently=False,
        )

        messages.success(request, "Your message has been received! We'll respond as soon as possible.")
        return redirect('home')


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

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import SpeakerApplication

from django.shortcuts import render
from django.contrib import messages
from .models import SpeakerApplication

def apply_speaker_view(request):
    if request.method == 'POST':
        data = request.POST
        SpeakerApplication.objects.create(
            your_name=data.get('your_name'),
            company_name=data.get('company_name'),
            total_employees=data.get('total_employees'),
            speaker_name=data.get('speaker_name'),
            email=data.get('email'),
            isd_code=data.get('isd_code'),
            whatsapp_number=data.get('whatsapp_number'),
            linkedin=data.get('linkedin'),
            slot=data.get('slot')
        )
        # Pass flag to template instead of redirecting
        return render(request, 'apply_speaker.html', {'form_success': True})

    return render(request, 'apply_speaker.html')


def thank_you_view(request):
    return render(request, 'thank_you.html')

def venue_detail(request):
    return render(request, 'venue_section.html')

def become_sponsor(request):
    return render(request, 'become_sponsor.html')

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ExhibitRegistration

from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings
from .models import ExhibitRegistration

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

    if request.method == 'POST':
        exhibit_type = request.POST.get('type')
        company_name = request.POST.get('company_name')
        name = request.POST.get('name')
        whatsapp = request.POST.get('whatsapp')
        email = request.POST.get('email')

        ExhibitRegistration.objects.create(
            type=exhibit_type,
            company_name=company_name,
            name=name,
            whatsapp=whatsapp,
            email=email
        )

        # Send email confirmation to user
        html_message = render_to_string('emails/exhibit_registration_received.html', {
            'name': name,
            'company': company_name,
            'type': exhibit_type
        })

        email_msg = EmailMultiAlternatives(
            subject="📥 We've Received Your Exhibit Registration",
            body="Thank you for your application to exhibit at the World AI Summit 2026.",
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[email],
        )
        email_msg.attach_alternative(html_message, "text/html")
        email_msg.send()

        messages.success(request, 'Your registration has been successfully submitted!')
        return redirect('exhibit')

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


from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings
from .models import SponsorInquiry  # Import model

def become_a_sponsor(request):
    if request.method == 'POST':
        company = request.POST.get('company')
        name = request.POST.get('name')
        whatsapp = request.POST.get('whatsapp')
        email = request.POST.get('email')

        # Save to DB
        SponsorInquiry.objects.create(
            company=company,
            name=name,
            whatsapp=whatsapp,
            email=email
        )

        # ✅ Send polite confirmation email
        html_message = render_to_string('emails/sponsor_application_received.html', {
            'name': name,
            'company': company,
        })

        email_msg = EmailMultiAlternatives(
            subject="📥 We've Received Your Sponsorship Inquiry",
            body="Thank you for your interest in becoming a sponsor.",
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[email],
        )
        email_msg.attach_alternative(html_message, "text/html")
        email_msg.send()

        messages.success(request, "Thank you for submitting your sponsor application!")
        return redirect('become_a_sponsor')

    reasons = [
        {"text": "Worldwide Promotions", "icon": "fa-globe"},
        {"text": "Priority Branding Before the Expo", "icon": "fa-star-half-alt"},
        {"text": "Priority Branding at the Expo", "icon": "fa-bullhorn"},
        {"text": "Networking with Industry Leaders", "icon": "fa-handshake"},
        {"text": "Right Target Audience", "icon": "fa-bullseye"},
        {"text": "Speaker Opportunity", "icon": "fa-microphone"},
        {"text": "Participate in Award Programs", "icon": "fa-award"},
        {"text": "Exhibiting Opportunity", "icon": "fa-store"},
        {"text": "VIP Lounge Access", "icon": "fa-couch"},
        {"text": "Network with VVIPs", "icon": "fa-user-tie"},
        {"text": "Branding After the Expo", "icon": "fa-calendar-check"},
        {"text": "Branding in Digital Magazine", "icon": "fa-book"},
        {"text": "Startup Pitch Competition", "icon": "fa-lightbulb"},
        {"text": "Investor Meetup", "icon": "fa-users"},
        {"text": "Prefix Appointments Before the Event", "icon": "fa-calendar-alt"},
    ]

    return render(request, 'become_a_sponsor.html', {
        "reasons": reasons,
    })




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


from django.shortcuts import render
from .forms import StartupPitchForm
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings
from .forms import StartupPitchForm

def startup_pitching_view(request):
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
        if form.is_valid():
            data = form.cleaned_data
            submitted = True
            form = StartupPitchForm()  # Reset form after submission

            # Send confirmation email
            html_message = render_to_string('emails/startup_pitch_confirmation.html', {
                'name': data['full_name'],
                'company': data['company_name'],
                'email': data['email'],
                'selected_package': data['package'],
            })

            email = EmailMultiAlternatives(
                subject="📥 We've Received Your Startup Pitching Application",
                body="Thank you for submitting your application to World AI Summit 2026.",
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[data['email']],
            )
            email.attach_alternative(html_message, "text/html")
            email.send()

    else:
        form = StartupPitchForm()

    return render(request, "startup_pitching.html", {
        "form": form,
        "packages": packages,
        "submitted": submitted,
    })


from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings
from .models import MediaPartnerApplication

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

        # Save to database
        MediaPartnerApplication.objects.create(
            partner_type=partner_type,
            events=", ".join(events),
            company_name=company_name,
            name=name,
            email=email,
            whatsapp=whatsapp,
            country=country,
            address=address
        )

        # === Send Confirmation Email to User ===
        html_message = render_to_string('emails/media_partner_confirmation.html', {
            'name': name,
            'company': company_name,
            'partner_type': partner_type,
            'events': ", ".join(events),
        })

        confirmation_email = EmailMultiAlternatives(
            subject="✅ Media Partner Registration Received – World AI Summit 2026",
            body="Thank you for your application.",  # plain text fallback
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[email],
        )
        confirmation_email.attach_alternative(html_message, "text/html")
        confirmation_email.send()

        messages.success(request, "Thank you for registering as a Media Partner!")
        return redirect('register_media_partner')

    return render(request, 'media_partner_form.html')


# modal
from django.core.mail import send_mail, EmailMultiAlternatives
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.template.loader import render_to_string
from .models import GeneralRegistration

@csrf_exempt
@require_POST
def registration_form(request):
    role = request.POST.get('role')
    name = request.POST.get('name')
    isd_code = request.POST.get('isd_code')
    whatsapp = request.POST.get('whatsapp_number')
    email = request.POST.get('email')
    company = request.POST.get('company')

    # ✅ Save to PostgreSQL
    GeneralRegistration.objects.create(
        role=role,
        name=name,
        email=email,
        company=company,
        isd_code=isd_code,
        whatsapp_number=whatsapp,
    )

    # === Admin Notification Email ===
    admin_subject = f"[World AI Summit] New {role} Registration: {name}"
    admin_message = f"""
New Registration Submitted:

• Name: {name}
• Email: {email}
• WhatsApp: {isd_code} {whatsapp}
• Company: {company}
• Role: {role}
"""
    send_mail(
        admin_subject,
        admin_message,
        settings.DEFAULT_FROM_EMAIL,
        [settings.CONTACT_RECEIVER_EMAIL],
        fail_silently=False
    )

    # === Styled Confirmation Email to User ===
    html_message = render_to_string('emails/registration_confirmation.html', {
        'name': name,
        'role': role,
        'company': company,
        'isd_code': isd_code,
        'whatsapp': whatsapp
    })

    confirmation_email = EmailMultiAlternatives(
        subject="✅ You’re registered for World AI Summit 2026!",
        body="Thank you for registering.",  # plain text fallback
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[email],
    )
    confirmation_email.attach_alternative(html_message, "text/html")
    confirmation_email.send()

    return JsonResponse({"status": "ok", "message": "Registration successful."})

from django.shortcuts import render

def refund_policy(request):
    return render(request, 'legal/refund_policy.html')

def visitor_terms(request):
    return render(request, 'legal/visitor_terms.html')

def sponsorship_terms(request):
    return render(request, 'legal/sponsorship_terms.html')

def speaker_conditions(request):
    return render(request, 'legal/speaker_conditions.html')

def exhibitor_conditions(request):
    return render(request, 'legal/exhibitor_conditions.html')

def general_terms(request):
    return render(request, 'legal/terms_and_conditions.html')

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from openai import OpenAI
import json

client = OpenAI()

@csrf_exempt
def chatbot_response(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            prompt = data.get('message', '')

            if not prompt:
                return JsonResponse({'reply': 'No message provided.'})

            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "You are Ari – the official AI assistant of the World AI X Summit 2026. "
                            "Be friendly, clear, and helpful. You assist users by answering questions about the event. "
                            "Event Details:\n"
                            "- Name: World AI X Summit 2026\n"
                            "- Dates: January 29–30, 2026\n"
                            "- Venue: SMX Convention Center Manila, Pasay City, Philippines\n"
                            "- Theme: Where AI Rises With PURPOSE\n"
                            "- Contact: hello@iriseup.ai | +1740 583 0770 | +63 96373 86001\n"
                            "- Website: www.worldaixsummit.com\n"
                            "Ticket Info: [Click here to view ticket pricing](https://www.worldaixsummit.com/pricing)"

                            "Ticket Pricing:\n"
                            "1. PROFESSIONAL PASS – ₱4,950 / $89 USD\n"
                            "2. STUDENT PASS – ₱1,250 / $23 USD (limited slots, ID required)\n"
                            "3. VIP PASS – ₱18,500 / $335 USD (includes VIP experiences)\n"
                            "*Please remind users to check the official pricing page and read the terms and refund policy before purchasing."
                        )
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.8
            )

            reply = response.choices[0].message.content.strip()
            return JsonResponse({'reply': reply})

        except Exception as e:
            return JsonResponse({'reply': f'Sorry, an error occurred: {str(e)}'})
