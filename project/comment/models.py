from django.db import models
from post.models import Post

# Create your models here.

class PostComment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    text = models.TextField()

    def __str__(self):
        return self.text

