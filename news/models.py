from datetime import date
from django.db import models

# Create your models here.
class Editor(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    phone_number = models.CharField(max_length=10, blank=True)
    
    def __str__(self):
        return self.first_name
    
    class Meta:
        ordering = ['first_name']
    
        
class Tag(models.Model):
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name
    
    
class Article(models.Model):
    title = models.CharField(max_length=60)
    post = models.TextField()
    editor = models.ForeignKey(Editor, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)
    pub_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    @classmethod
    def todays_news(cls):
        today = date.today()
        news = cls.objects.filter(pub_date__date = today)
        
        return news
    
    
    @classmethod
    def days_news(cls, date):
        news = cls.objects.filter(pub_date__date = date)
        
        return news