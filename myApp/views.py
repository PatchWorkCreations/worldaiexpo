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
    return render(request, 'exhibit.html')

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