from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from designs.forms import DesignForm
from matching.services import run_matching_pipeline

class HomeView(TemplateView):
    template_name = "general/home.html"

    
class ContactView(TemplateView):
    template_name = "general/contact.html"


class LegalView(TemplateView):
    template_name = "general/legal.html"


class AboutView(TemplateView):
    template_name = "general/about.html"
