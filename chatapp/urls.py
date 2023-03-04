from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home' ),
    path('chat/', views.chat, name='chat' ),
    path('index/', views.home, name='index'),
    path('contact/', views.contact, name='index'),
    path('gallery/', views.gallery, name='index'),
    path('aboutus/', views.aboutus, name='index'),
]