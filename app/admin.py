from django.contrib import admin
from .models import Book, Author, Editorial

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Editorial)
