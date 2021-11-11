from django.shortcuts import render, redirect, get_object_or_404
from .models import Books, Category
from .forms import BookForm
from django.contrib.auth.decorators import login_required


# Create your views here.

def homepage(request):
    # show a homepage
    if request.user.is_authenticated:
        return redirect("list_books")
    return render(request, "books/homepage.html")

@login_required
def list_books(request):
    book = Books.objects.all().order_by("created_at")
    return render(request, "books/list_books.html",
                  {"book": book})

def add_book(request):
    if request.method == 'GET':
        form = BookForm()
    else:
        form = BookForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='list_books')

    return render(request, "books/add_book.html", {"form": form})  
    
def category_filter(request, categories):
    books=Category.objects.filter(categories_name=categories)
    return render(request, 'books/book_categories.html', {"books":books, "categories": categories})

