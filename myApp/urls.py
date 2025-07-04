from django.urls import path
from . import views
from .views import registration_form

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
    path('become-a-sponsor/', views.become_a_sponsor, name='become_a_sponsor'),
    path('startup-pitch/', views.startup_pitching_view, name='startup_pitch'),
    path('register_media_partner/', views.register_media_partner, name='register_media_partner'),
    path('send-message/', views.send_message_view, name='send_message'),
    path('submit-registration/', registration_form, name='submit_registration'),

    path('legal/refund-policy/', views.refund_policy, name='refund_policy'),
    path('legal/visitor-terms/', views.visitor_terms, name='visitor_terms'),
    path('legal/sponsorship-terms/', views.sponsorship_terms, name='sponsorship_terms'),
    path('legal/speaker-conditions/', views.speaker_conditions, name='speaker_conditions'),
    path('legal/exhibitor-conditions/', views.exhibitor_conditions, name='exhibitor_conditions'),
    path('legal/terms-and-conditions/', views.general_terms, name='general_terms'),

]
