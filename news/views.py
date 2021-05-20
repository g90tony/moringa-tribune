from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.http import  Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import Article, NewsLetterRecipients
import datetime as dt 

from .forms import NewsLetterForm
from .email import send_welcome_email
# Create your views here.

def news_of_day(request):
    today = dt.date.today() 
    news = Article.todays_news()
    user = request.user
    
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['subscriber_name']
            email = form.cleaned_data['subscriber_email']
            
            recipient = NewsLetterRecipients(name= name, email = email)
            recipient.save()
            
            HttpResponseRedirect('Todays News')
    else: 
        form = NewsLetterForm()
        
    return render(request, 'all-news/todays-news.html', {'date': today, 'news': news, 'letterForm': form, "user": user})


def past_days_news(request, past_date):
    user = request.user
    try:
        query_date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()
        
    except ValueError:
        raise Http404()
        assert False
        
    if query_date == dt.date.today():
        return redirect(news_of_day)
        
            
    return render(request, 'all-news/past-news.html', {'date': query_date, "user": user})

def search_news(request):
    user = request.user
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            print('Form is valid')
            
    else: 
        form = NewsLetterForm()
        
    if 'article' in request.GET and request.GET['article']:
        search_term = request.GET.get('article')
        article_results = Article.search_by_title(search_term)
        
        search_header = f'"{search_term}"'
        
        return render(request, 'all-news/search.html', {"search_header":search_header, "articles" : article_results, 'letterForm': form, "user": user})
    
    else:
        search_header = "You haven't searched for any term"
        return render(request, 'all-news/search.html', {'search_header': search_header, 'letterForm': form, "user": user})
    
@login_required(login_url='/accounts/login/')
def article(request, article_id):
    user = request.user
    try:
        requested_article = Article.objects.get(id = article_id)
        
    except Article.DoesNotExist:
        raise Http404()
    
    return render(request, 'all-news/article.html', {'article':requested_article, "user":user})
