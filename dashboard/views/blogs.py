from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)
from home.models import Blog

from .index import DashboardView


class BlogCreateView(DashboardView, CreateView):
    model = Blog
    fields = ('title', 'description', 'photo',)
    template_name = 'dashboard/blogs/add.html'

    def get_success_url(self) -> str:
        messages.success(self.request, "Club News Added Successfully")
        return reverse_lazy("dashboard:blogs:blog_details", kwargs = {'pk': self.object.pk})


class BlogListView(DashboardView, ListView):
    model = Blog
    context_object_name = 'blogs'
    template_name = 'dashboard/blogs/list.html'


class BlogDetailView(DashboardView, DetailView):
    model = Blog
    context_object_name = 'blog'
    template_name = 'dashboard/blogs/details.html'


class BlogUpdateView(DashboardView, UpdateView):
    model = Blog
    fields = ('title', 'description', 'photo',)
    template_name = 'dashboard/blogs/edit.html'

    def get_success_url(self) -> str:
        messages.success(self.request, "Club News Updated Successfully")
        return reverse_lazy("dashboard:blogs:blog_details", kwargs = {'pk': self.object.pk})

