from django.urls import path

from . import views

app_name = 'main'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact-us/', views.contact_us, name='contact-us'),
    # path('contact-us/', views.ContactUsView.as_view(), name='contact-us'),
]
