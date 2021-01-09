from django.urls import path

from ..views.blogs import (BlogCreateView, BlogDetailView, BlogListView,
                           BlogUpdateView)

app_name = "blogs"

urlpatterns = [
    path('all/', BlogListView.as_view(), name="blogs_list"),
    path('add/', BlogCreateView.as_view(), name="blog_add"),
    path('<int:pk>/edit', BlogUpdateView.as_view(), name="blog_update"),
    path('<int:pk>/details/', BlogDetailView.as_view(), name='blog_details'),
]
