from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .utils import get_mongodb
from .forms import AuthorForm, QuoteForm
from .models import Tag, Author, Quote

def main(request, page=1):
    db = get_mongodb()
    quotes = db.quotes.find().sort('created_at')  # Order by creation date or another field
    per_page = 10
    paginator = Paginator(list(quotes), per_page)
    quotes_one_page = paginator.page(page)
    return render(request, 'quotes/index.html', context={'quotes': quotes_one_page})

@login_required
def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quotes:root')  # Redirect to the main page
    else:
        form = AuthorForm()
    return render(request, 'quotes/add_author.html', {'form': form})

@login_required
def add_quote(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quotes:root')  # Redirect to the main page
    else:
        form = QuoteForm()
    return render(request, 'quotes/add_quote.html', {'form': form})