from django.contrib import admin
from .models import Book, Author, Editorial
from django.contrib.auth.models import Group, Permission

admin.site.site_header = "Administración de Book Store"
admin.site.site_title = "Panel Book Store"
admin.site.index_title = "Gestión del catálogo"

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "publication_year", "editorial_name", "authors_list")
    list_filter = ("editorial", "publication_year")
    search_fields = ("title", "authors__first_name", "authors__last_name")

    def editorial_name(self, obj):
        return obj.editorial.name
    editorial_name.short_description = "Editorial"

    def authors_list(self, obj):
        return ", ".join(a.name for a in obj.authors.all())
    authors_list.short_description = "Autores"


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name", "birth_year")
    search_fields = ("first_name", "last_name")
    list_filter = ("birth_year",)


@admin.register(Editorial)
class EditorialAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    search_fields = ("name",)


def setup_roles():
    book_manager, created = Group.objects.get_or_create(name="Gestor de Libros")
    book_permissions = Permission.objects.filter(content_type__app_label="app", content_type__model="book")
    book_manager.permissions.set(book_permissions)

    editorial_manager, created = Group.objects.get_or_create(name="Gestor Editorial")
    editorial_permissions = Permission.objects.filter(content_type__app_label="app", content_type__model="editorial")
    editorial_manager.permissions.set(editorial_permissions)

    read_only, created = Group.objects.get_or_create(name="Lector del catálogo")
    read_permissions = Permission.objects.filter(codename__startswith="view_")
    read_only.permissions.set(read_permissions)