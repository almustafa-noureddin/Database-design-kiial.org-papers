from django.shortcuts import render
from django.contrib import messages

from .models import (
	Paper,
    Researcher,
    Supervisor,
	Degree,
    
	
	)

from django.views import generic
from . forms import 


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