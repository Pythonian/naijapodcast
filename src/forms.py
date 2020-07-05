from django import forms
from .models import NewsletterEmail


class ContactForm(forms.Form):
	name = forms.CharField()
	email = forms.EmailField()
	message = forms.CharField(
		widget=forms.Textarea)

class SearchForm(forms.Form):
	query = forms.CharField()

class NewsletterEmailForm(forms.ModelForm):
	class Meta:
		model = NewsletterEmail
		fields = ['email']
		