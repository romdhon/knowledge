from django.urls import path
from . import views

app_name = 'post'

urlpatterns = [
    path('detail/<slug:slug>/', views.post_detail, name='detail'),
    path('create/', views.post_create, name="create"),
    path('edit/<slug:slug>/', views.post_edit, name="edit"),
    path('categories/', views.category_list, name="categories"),
    path('categories/<single_slug>/', views.category_series, name="series"),
    path('categories/post/<slug>/', views.category_post, name="category_post"),
    path('categories/series/<slug>/', views.first_post, name="first_post"),
]