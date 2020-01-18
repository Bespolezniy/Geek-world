from django.shortcuts import render
from django.views.generic.dates import ArchiveIndexView
from django.views.generic.detail import DetailView
from news.models import New
from generic.mixins import CaregoryListMixin, PageNumberMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from generic.controllers import PageNumberView

# Create your views here.

class NewsListView(ArchiveIndexView, CaregoryListMixin):
    model = New
    template_name = "news_index.html"
    date_field = "date"
    paginate_by = 10
    allow_empty = True
    allow_future = True

class NewDetailView(DetailView, PageNumberMixin):
    model = New
    template_name = "new.html"

class NewCreateView(SuccessMessageMixin, CreateView, CaregoryListMixin):
    model = New
    template_name = "new_add.html"
    success_url = reverse_lazy("news_index")
    success_message = "New was created"
    fields=['title', 'description', 'content']

class NewUpdateView(SuccessMessageMixin, PageNumberView, UpdateView, PageNumberMixin):
    model = New
    template_name = "new_edit.html"
    success_url = reverse_lazy("news_index")
    success_message = "New was changed"

class NewDeleteView(PageNumberView, DeleteView, PageNumberMixin):
    model = New
    template_name = "new_delete.html"
    success_url = reverse_lazy("news_index")

    def post(self, request, *args, **kwargs):
        messages.add_message(request, messages.SUCCESS, "New was deleted")
        return super(NewDeleteView, self).post(request, *args, **kwargs)



