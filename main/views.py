from django.shortcuts import render
from django.views.generic.base import TemplateView
from generic.mixins import CaregoryListMixin

# Create your views here.
class MainPageView(TemplateView, CaregoryListMixin):
    template_name = 'main.html'
