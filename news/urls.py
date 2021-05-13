from django.urls import path, re_path

from . import views

app_name = 'news'

urlpatterns = [
    path('', views.welcome, name='index'),
]
