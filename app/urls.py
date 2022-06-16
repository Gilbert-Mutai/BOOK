from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns =[
    path('', views.index,name='home'),
    path('', include("django.contrib.auth.urls")),
    path("register/", views.register, name="register"),
    path('profile/', views.profile, name='profile'),
    path('updateprofile/', views.updateprofile, name='updateprofile'),
    path('booking/', views.booking, name='booking'),
    path('about-us/', views.about_us, name='about-us'),
    path('contact-us/', views.contact_us, name='contact-us'),
    path('stations/', views.stations, name='stations'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)