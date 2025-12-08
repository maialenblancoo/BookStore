from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'editorial', 'authors', 'publication_year']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'editorial': forms.Select(attrs={'class': 'form-control'}),
            'authors': forms.CheckboxSelectMultiple(),
            'publication_year': forms.NumberInput(attrs={'class': 'form-control'}),
        }
