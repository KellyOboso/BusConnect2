from operator import index

from django.contrib import admin
from django.urls import path
from logisticsapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name='home'),
    path('about/', views.about,name='about'),
    path('contact/', views.contact,name='contact'),
    path('quote/', views.quote,name='quote'),
    path('pricing/', views.pricing,name='pricing'),
    path('details/', views.details,name='details'),
    path('services/', views.services,name='services'),
    path('starterpage/', views.starterpage,name='starterpage'),

]
