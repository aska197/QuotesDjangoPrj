from django import forms
from .models import Quote, Author, Tag

class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = ['quote', 'author', 'tags']

    def save(self, commit=True):
        quote = super().save(commit=False)
        if commit:
            quote.save()
            self.save_m2m()  # This is necessary to save the many-to-many relationships
        return quote
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['author'].queryset = Author.objects.all()  # Set queryset for author field
        self.fields['tags'].queryset = Tag.objects.all()  # Set queryset for tags field

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['fullname', 'born_date', 'born_location', 'description']

    def __str__(self):
        return self.fullname

