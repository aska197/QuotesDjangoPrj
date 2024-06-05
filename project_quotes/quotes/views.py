from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .utils import get_mongodb
from .forms import AuthorForm, QuoteForm
from .models import Tag, Author, Quote

def main(request, page=1):
    db = get_mongodb()
    quotes = db.quotes.find()
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