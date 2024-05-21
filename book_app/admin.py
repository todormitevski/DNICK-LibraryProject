from django.contrib import admin

from book_app.models import Publisher, Book


# Register your models here.


class PublisherAdmin(admin.ModelAdmin):
    pass


class BookAdmin(admin.ModelAdmin):
    pass


admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Book, BookAdmin)