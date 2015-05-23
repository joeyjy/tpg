from django.shortcuts import render
from django.views.generic import DetailView, TemplateView, ListView
from .models import Package

class PackageList(ListView):
    template_name = 'package/list.html'
    model = Package

    def get_context_data(self, **kwargs):
        ctx = super(PackageList, self).get_context_data(**kwargs)

        return ctx


