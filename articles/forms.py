from django import forms
from .models import Article, Category

choices = Category.objects.all().values_list('name', 'name')

choice_list = []

for item in choices:
    choice_list.append(item)


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'author', 'category', 'body', 'description' )

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', }),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }