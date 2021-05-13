from django.shortcuts import redirect, render
from django.http import HttpResponse, Http404
import datetime as dt 


# Create your views here.
def welcome(request):
    
    return render(request, 'welcome.html', {"title": "Home: Moringa Tribune"})  


def news_of_day(request):
    today = dt.date.today() 
    
    return render(request, 'all-news/todays-news.html', {'date': today,})


def past_days_news(request, past_date):
    
    try:
        query_date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()
        
    except ValueError:
        raise Http404()
        assert False
        
    if query_date == dt.date.today():
        return redirect(news_of_day)
        
            
    return render(request, 'all-news/past-news.html', {'date': query_date})