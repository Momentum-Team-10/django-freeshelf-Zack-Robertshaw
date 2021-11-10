from django.shortcuts import render, redirect, get_object_or_404
from .models import Books
from .forms import BookForm

# Create your views here.

def homepage(request):
    # show a homepage
    if request.user.is_authenticated:
        return redirect("list_books")
    return render(request, "books/homepage.html")

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

