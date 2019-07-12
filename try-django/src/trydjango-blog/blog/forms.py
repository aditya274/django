from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder' : 'Blog title'}))
    content = forms.CharField(required=True, widget=forms.Textarea(
    attrs={
    'placeholder': 'Blog content',
    'rows' : 100,
    'cols' : 120,
    }
    ))
    class Meta:
        model = Article
        fields = [
        'title',
        'content',
        'active',
        ]
