from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from portal.models import ConsentForm
from .models import Blog
class IndexTemplateView(TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["consent_form"] = ConsentForm.objects.last()
        context["blogs"] = Blog.objects.all().order_by("-created_at")
        return context


