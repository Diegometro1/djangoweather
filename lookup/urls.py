from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home_page'),
    path('about.html', views.about, name='about_page')
]
