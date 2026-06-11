from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Books)
class BooksAdmin(admin.ModelAdmin):
    exclude = ('views', )