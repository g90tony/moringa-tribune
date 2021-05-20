from django.contrib import admin
from .models import  Article, Tag

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    filter_horizontal = ('Tag')

admin.site.register(Article)
admin.site.register(Tag)