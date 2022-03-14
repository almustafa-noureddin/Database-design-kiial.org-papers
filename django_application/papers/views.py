from django.shortcuts import render
from django.contrib import messages

from .forms import SearchForm
from .models import (
	Paper,
	
	
	)
from django.core.paginator import Paginator
from django.views import generic
from django.views.generic.edit import ModelFormMixin
from .filters import PapersFilter
#from . forms import 

#class IndexView(generic.TemplateView):
#	template_name = "papers/index.html"
#
#	def get_context_data(self, **kwargs):
#		context = super().get_context_data(**kwargs)
#		
#		papers = Paper.objects.all()[:10]
#		researchers = Researcher.objects.all()[:10]
#		papersupervisors = PaperSupervisor.objects.all()
#		degrees = Degree.objects.all()[:10]
#		
#		context["papers"] = papers
#		context["researchers"] = researchers
#		context["papersupervisors"] = papersupervisors
#		context["degrees"] = degrees
#		return context
#

class IndexView(generic.ListView):
    template_name = 'papers/index.html'
    context_object_name = 'papers'
    model = Paper
    paginate_by = 5
    
    def get_queryset(self):
        return super().get_queryset().all().order_by('title')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        return context
	
    
    def get_paginate_by(self, queryset):
        return self.request.GET.get("paginate_by", self.paginate_by)
    



# Create your views here.
#
#
#class LandingPageView(generic.TemplateView):
#    template_name = "index.html"
#    def get_context_data(self, **kwargs):
#		context = super().get_context_data(**kwargs)
#        papers = Paper.objects.all()
#        context["papers"] = papers
#        return context