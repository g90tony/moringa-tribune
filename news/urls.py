from django.urls import path, re_path

from . import views

app_name = 'news'

urlpatterns = [
    path('', views.welcome, name='index'),
    path('/today', views.news_of_day, name='Todays News'),
    re_path(r'/past-news/(\d{4}-\d{2}-\d{2})/$', views.past_days_news, name='pastNews')
]
