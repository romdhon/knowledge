from django.contrib import admin
from comment.models import PostComment

# Register your models here.
class CommentAdmin(admin.ModelAdmin):
    list_display = ['text', 'post']
admin.site.register(PostComment, CommentAdmin)
