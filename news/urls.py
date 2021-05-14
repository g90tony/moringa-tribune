from django.urls import path, re_path, register_converter

from . import views

app_name = 'news'

urlpatterns = [
    re_path('^$', views.news_of_day, name='Todays News'),
    re_path(r'^past-news/(?P<past_date>[0-9]{4}-[0-9]{2}-[0-9]{2})/$', views.past_days_news, name='Past News')
]
