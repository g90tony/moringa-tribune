from news.models import Article
from django import forms

class NewsLetterForm(forms.Form):
    subscriber_name = forms.CharField(label='First Name')
    subscriber_email = forms.EmailField(label='Email')
    

class NewArticleForm(forms.ModelForm):
    class Meta:
        model= Article
        exclude = ['editor', 'pub_date']
        widgets= {
            'tags': forms.CheckboxSelectMultiple(),
        }