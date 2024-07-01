from django import forms
from quotes.models import Quote, Author, Tag

class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = ['quote', 'author', 'tags']

    def save(self, commit=True):
        quote = super().save(commit=False)
        if commit:
            quote.save()
            self.save_m2m()  # Save many-to-many relationships
        return quote
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Ensure queryset is set for the author and tags fields
        self.fields['author'].queryset = Author.objects.all()
        self.fields['tags'].queryset = Tag.objects.all()

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['fullname', 'born_date', 'born_location', 'description']

    def __str__(self):
        return self.fullname


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name']

