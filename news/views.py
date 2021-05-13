from django.shortcuts import render
from django.http import HttpResponse
import datetime as dt 

def convert_date(date):
    day_num = dt.date.weekday(date)
    
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    
    day_str = days[day_num]
    
    return day_str

# Create your views here.
def welcome(request):
    
    return HttpResponse('Welcome to the Moringa Tribune')    


def news_of_day(request):
    today = dt.date.today()
    
    day = convert_date(today)
    
    markup = f''' 
                <html>
                    <body>
                        <h1>{day} - {today.month} - {today.year} </h1>
                    </body>
                </html>
              '''
              
    return HttpResponse(markup)


