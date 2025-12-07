from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Book, Author, Editorial

def index(request):
    editorials = Editorial.objects.all()
    featured_books = {}

    for editorial in editorials:
        latest_book = (
            Book.objects
            .filter(editorial=editorial)
            .order_by('-publication_year')
            .first()
        )
        if latest_book:
            featured_books[editorial] = latest_book

    return render(request, 'bookstore/index.html', {
        'featured_books': featured_books
    })

def book_list(request):
    books = get_list_or_404(Book)
    return render(request, 'bookstore/book_list.html', {'books': books})

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'bookstore/book_detail.html', {'book': book})

def author_list(request):
    authors = get_list_or_404(Author)
    return render(request, 'bookstore/author_list.html', {'authors': authors})

def author_detail(request, pk):
    author = get_object_or_404(Author, pk=pk)
    return render(request, 'bookstore/author_detail.html', {'author': author})

def editorial_list(request):
    editorials = get_list_or_404(Editorial)
    return render(request, 'bookstore/editorial_list.html', {'editorials': editorials})

def editorial_detail(request, pk):
    editorial = get_object_or_404(Editorial, pk=pk)
    return render(request, 'bookstore/editorial_detail.html', {'editorial': editorial})
