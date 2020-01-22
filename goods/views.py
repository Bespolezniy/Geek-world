from django.shortcuts import render, redirect
from django.views.generic.base import ContextMixin, TemplateView
from django.views.generic.list import ListView
from generic.mixins import CaregoryListMixin, PageNumberMixin
from goods.models import Good, GoodImage
from categories.models import Category
from generic.controllers import PageNumberView
from django.views.generic.detail import DetailView
from django.forms.models import inlineformset_factory
from goods.forms import GoodForm
from django.contrib import messages
from django.urls import reverse

# Create your views here.
class SortMixin(ContextMixin):
    sort = "0"
    order = "A"

    def get_context_data(self, **kwargs):
        context = super(SortMixin, self).get_context_data(**kwargs)
        context["sort"] = self.sort
        context["order"] = self.order
        return context

class GoodListView(PageNumberView, ListView, SortMixin, CaregoryListMixin):
    template_name = "goods_index.html"
    model = Good
    paginate_by = 10
    cat = None

    def get(self, request, *args, **kwargs):
        if self.kwargs["pk"] == None:
            self.cat = Category.objects.first()
        else:
            self.cat = Category.objects.get(pk = self.kwargs["pk"])
        return super(GoodListView, self).get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super(GoodListView, self).get_context_data(**kwargs)
        context["category"] = self.cat
        return context

    def get_queryset(self):
        goods = Good.objects.filter(category=self.cat)
        if self.sort == "2":
            if self.order == "D":
                goods = goods.order_by("-in_stock", "name")
            else:
                goods = goods.order_by("in_stock", "name")
        elif self.sort == "1"
            if self.order == "D":
                goods = goods.order_by("-price", "name")
            else:
               goods = goods.order_by("price", "name") 
        else:
            if self.order == "D":
                goods = goods.order_by("-name")
            else:
                goods = goods.order_by("name")

class GoodDetailView(PageNumberView, DetailView, SortMixin, PageNumberMixin):
    model = Good
    template_name = "good.html"
    

GoodImagesFormset = inlineformset_factory(Good, GoodImage, can_order=True)

class GoodCreate(PageNumberView, TemplateView, SortMixin, PageNumberMixin):
    template_name = "good_add.html"
    cat = None
    form = None
    formset = None

    def get(self, request, *args, **kwargs):
        if self.kwargs["pk"] == None:
            self.cat = Category.objects.first()
        else:
            self.cat = Category.objects.get(pk = self.kwargs["pk"])
        self.form = GoodForm(initial= {"category": self.cat})
        self.formset = GoodImagesFormset()
        return super(GoodCreate, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(GoodCreate, self).get_context_data(**kwargs)
        context["category"] = self.cat
        context["form"] = self.form
        context["formset"] = self.formset
        return context

    def post(self, request, *args, **kwargs):
        self.form = GoodForm(request.POST, request.FILES)
        if self.form.is_valid():
            new_good = self.form.save()
            self.formset = GoodImagesFormset(request.POST, request.FILES, instance=new_good)
            
            if self.formset.is_valid():
                self.formset.save()
                messages.add_message(request, messages.SUCCESS, "A good was added")
                return redirect(reverse("goods_index", kwargs = {"pk": new_good.category.pk}) + "?page=" +
                self.request.GET["page"] + "$sort" + self.request.GET["sort"] + "&order" + self.request.GET["order"])
            
            if self.kwargs['pk'] == None:
                self.cat = Category.objects.first()
            else:
                self.cat = Category.objects.get(pk = self.kwargs["pk"])
            
            self.formset = GoodImagesFormset(request.POST, request.FILES)
            return super(GoodCreate, self).post(request, *args, **kwargs)
    

        
