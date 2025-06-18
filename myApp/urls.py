from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('index/', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('book-now/', views.book_now, name='book_now'),
    path('coming-soon/', views.coming_soon, name='coming_soon'),
    path('contact/', views.contact_view, name='contact'),
    path('contact/thanks/', views.contact_thanks, name='contact_thanks'),

    path('error/', views.error_page, name='error'),
    path('event-list/', views.event_list, name='event_list'),
    path('event-detail/', views.event_detail, name='event_detail'),
    path('faq/', views.faq, name='faq'),
    path('gallery/', views.gallery, name='gallery'),
    path('news-list/', views.news_list, name='news_list'),
    path('news-single/', views.news_single, name='news_single'),
    path('pricing/', views.pricing, name='pricing'),
    path('product-list/', views.product_list, name='product_list'),
    path('product-single/', views.product_single, name='product_single'),
    path('search-result/', views.search_result, name='search_result'),
    path('speaker-detail/', views.speaker_detail, name='speaker_detail'),
    path('speaker-list/', views.speaker_list, name='speaker_list'),
    path('sponsers/', views.sponsers, name='sponsers'),
    path('testimonial/', views.testimonial, name='testimonial'),
    path('apply-speaker/', views.apply_speaker_view, name='apply_speaker'),
    path('thank-you/', views.thank_you_view, name='thank_you'),
    path('venue/', views.venue_detail, name='venue_detail'),
    path('sponsor/', views.become_sponsor, name='become_sponsor'),
    path('exhibit/', views.exhibit, name='exhibit'),
    path('book-ticket/', views.book_ticket, name='book_ticket'),
]
