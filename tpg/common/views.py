from django.shortcuts import render
from django.views.generic import DetailView, TemplateView, ListView

class SiteIndex(TemplateView):
    template_name = 'common/home.html'

    def get_context_data(self, **kwargs):
        ctx = super(SiteIndex, self).get_context_data(**kwargs)
    
        return ctx
