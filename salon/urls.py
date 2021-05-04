from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('contact/message/', views.message, name='message'),
    path('contact/message/<int:num>', views.message, name='message'),
]