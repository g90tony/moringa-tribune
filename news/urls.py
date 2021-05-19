from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'news'

urlpatterns = [
    re_path('^$', views.news_of_day, name='Todays News'),
    re_path('^search/', views.search_news, name='Search Results'),
    re_path(r'^past-news/(?P<past_date>[0-9]{4}-[0-9]{2}-[0-9]{2})/$', views.past_days_news, name='Past News'),
    path(r'^article/(?P<article_id>[0-9])/$', views.article, name='View Article')
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)   