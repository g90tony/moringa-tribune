from django.shortcuts import render
from django.http import HttpResponse, Http404
import datetime as dt 

def convert_date(day, month):

    
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    months = ['January, February', 'March', 'April', 'May', 'June', 'July' ,'August', 'September', 'October', 'November', 'December']
    
    day_str = days[day]
    month_str = months[month]
    
    return {'day': day_str, 'month': month_str}

# Create your views here.
def welcome(request):
    
    return HttpResponse('Welcome to the Moringa Tribune')    


def news_of_day(request):
    today = dt.date.today()
    
    converted = convert_date(today.weekday(), today.month -2)
    
    markup = f''' 
                <html>
                    <body>
                        <h1>{converted['day']} - {converted['month']} - {today.year} </h1>
                    </body>
                </html>
              '''
              
    return HttpResponse(markup)


def past_days_news(request, past_date):
    
    try:
        query_date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()
        
    except ValueError:
        raise Http404()

    converted = convert_date(query_date.weekday(), query_date.month)
    
    markup = f''' 
            <html>
                <body>
                    <h1>{converted['day']} {query_date.strftime("%d")} {converted['month']} {query_date.year} </h1>
                </body>
            </html>
            '''
            
    return HttpResponse(markup)