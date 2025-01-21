# url dispatching

from django.contrib import admin
from django.urls import path
from myapp import views




urlpatterns = [
    # path('myadmin/', admin.site.urls, name='myadmin'),  # Custom namespace

     path('admin/', admin.site.urls),
    path("", views.index, name='myapp'),
    path("about/", views.about, name='about'),
    path("services/", views.services, name='services'),
    path("contact/", views.contact, name='contact'),
]

