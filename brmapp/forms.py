from django import forms

class NewBookFrom(forms.Form):
 title=forms.CharField(label='Title',max_length=50)
 price=forms.FloatField(label='Price')
 author=forms.CharField(label='Author', max_length=50)
 publisher=forms.CharField(label='Publisher' ,max_length=50)

class SearchFrom(forms.Form):
 title=forms.CharField(label='Title', max_length=50)
