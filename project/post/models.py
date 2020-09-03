from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse
from django.db.models.signals import pre_save
from django.utils.text import slugify

class Category(models.Model):
    category_name = models.CharField(max_length=200)
    category_description = models.CharField(max_length=200)
    category_slug = models.SlugField(max_length=200, default=1)

    def __str__(self):
        return self.category_name

class CategorySeries(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="categories", default=1)
    series_name = models.CharField(max_length=200)
    series_description = models.CharField(max_length=200)
    series_slug = models.SlugField(max_length=200)

    def __str__(self):
        return self.series_name

# Create your models here.
class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="post_categories", default=1)
    series = models.ForeignKey(CategorySeries, on_delete=models.CASCADE, related_name="category_series", default=1)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="post_user")
    content = RichTextUploadingField(null=True, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post:detail', kwargs={'slug': self.slug})

def post_receiver(sender, instance, *args, **kwargs):
    slug = slugify(instance.title)

    exist = Post.objects.filter(slug=slug).exists()
    if exist:
        slug = "{}-{}".format(slug, instance.id)
    
    instance.slug = slug

def series_receiver(sender, instance, *args, **kwargs):
    slug = slugify(instance.series_name)

    exists = CategorySeries.objects.filter(series_slug=slug).exists()

    if exists:
        slug = "{}-{}".format(slug, instance.id)

    instance.series_slug = slug


pre_save.connect(receiver=post_receiver, sender=Post)
pre_save.connect(receiver=series_receiver, sender=CategorySeries)
