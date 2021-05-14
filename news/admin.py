from django.contrib import admin
from .models import Editor, Article, Tag

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    filter_horizontal = ('Tag')

admin.site.register(Editor)
admin.site.register(Article)
admin.site.register(Tag)