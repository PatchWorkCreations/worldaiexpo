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