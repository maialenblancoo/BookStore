from django.views.generic import TemplateView, ListView, DetailView, CreateView
from django.urls import reverse_lazy
from django.contrib import messages

from .models import Book, Author, Editorial
from .forms import BookForm

class IndexView(TemplateView):
    template_name = "bookstore/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

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

        context["featured_books"] = featured_books
        return context

class BookListView(ListView):
    model = Book
    template_name = "bookstore/book_list.html"
    context_object_name = "books"


class BookDetailView(DetailView):
    model = Book
    template_name = "bookstore/book_detail.html"
    context_object_name = "book"

class BookCreateView(CreateView):
    model = Book
    template_name = "bookstore/book_form.html"
    form_class = BookForm
    success_url = reverse_lazy("book_list")

    def form_valid(self, form):
        messages.success(self.request, "El libro ha sido creado correctamente.")
        return super().form_valid(form)

class AuthorListView(ListView):
    model = Author
    template_name = "bookstore/author_list.html"
    context_object_name = "authors"

class AuthorDetailView(DetailView):
    model = Author
    template_name = "bookstore/author_detail.html"
    context_object_name = "author"

class EditorialListView(ListView):
    model = Editorial
    template_name = "bookstore/editorial_list.html"
    context_object_name = "editorials"

class EditorialDetailView(DetailView):
    model = Editorial
    template_name = "bookstore/editorial_detail.html"
    context_object_name = "editorial"
