from django.shortcuts import render
from django.views.generic.base import TemplateView
from generic.mixins import CaregoryListMixin
from news.models import New

# Create your views here.
class MainPageView(TemplateView, CaregoryListMixin):
    template_name = 'main.html'
    news = New.objects.all()[0:5]

    def get_context_data(self, **kwargs):
        context = super(MainPageView, self).get_context_data(**kwargs)
        context["news"] = self.news
        return context
    
