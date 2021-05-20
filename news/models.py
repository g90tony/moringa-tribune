from datetime import date
from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name
    
    
class Article(models.Model):
    title = models.CharField(max_length=60)
    post = HTMLField()
    editor = models.ForeignKey(User, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)
    pub_date = models.DateTimeField(auto_now_add=True)
    article_img = CloudinaryField('image', default=None)
    
    
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
    
    @classmethod
    def search_by_title(cls, search_term):
        news = cls.objects.filter(title__icontains=search_term)
        
        return news
    
    
class NewsLetterRecipients(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    
    def save_recipient(self):
        self.save()
    
    def __str__(self):
        self.save()