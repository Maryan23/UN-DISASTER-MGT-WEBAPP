from django.urls import path, include
from django.conf.urls import url, include
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('article', views.article, name='article'),
    path('categories', views.categories, name='categories'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
]
