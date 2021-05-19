from django import forms

class NewsLetterForm(forms.Form):
    subscriber_name = forms.CharField(label='First Name', default=None)
    subscriber_email = forms.EmailField(label='Email')