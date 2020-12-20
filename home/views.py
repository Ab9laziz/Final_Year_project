from django.shortcuts import render
from django.views.generic import TemplateView
from portal.models import ConsentForm

class IndexTemplateView(TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["consent_form"] = ConsentForm.objects.last()
        return context

