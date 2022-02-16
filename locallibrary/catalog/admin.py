from django.contrib import admin

# Register your models here.
from .models import Author, Genre, Book, BookInstance, Language

# admin.site.register(Book)
# admin.site.register(Author)
admin.site.register(Genre)
# admin.site.register(BookInstance)
admin.site.register(Language)


class AuthorInstanceInline(admin.TabularInline):
    model = Book
    fields = ['title', 'isbn']
    extra = 0


# Define the admin class
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]

    inlines = [AuthorInstanceInline]


# Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)


class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 0


# Register the Admin classes for Book using the decorator
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]


# Register the Admin classes for BookInstance using the decorator
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')
    list_display = ('book', 'imprint', 'id', 'status', 'due_back', 'borrower')

    fieldsets = (
        (None, {
            'fields': ('book', 'imprint')
        }),
        ('Availability', {
            'fields': ('status', 'due_back', 'borrower')
        }),
    )
