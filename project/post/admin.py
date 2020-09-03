from django.contrib import admin
from .models import Post, Category, CategorySeries
from tinymce.widgets import TinyMCE
from django.db import models

# Register your models here.
class PostAdmin(admin.ModelAdmin):

    fieldsets = (
        ('Category', {'fields': ['category']}),
        ('Series', {'fields': ['series']}),
        ("Post", {'fields': ['title', 'slug', 'author', 'content']}),
    )

    # list_display = ['title', 'author', 'create_date']
    # prepopulated_fields = {'slug': ['title']}


admin.site.register(Category)
admin.site.register(CategorySeries)
admin.site.register(Post, PostAdmin)

