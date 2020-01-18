from django.views.generic.base import ContextMixin

class CaregoryListMixin(ContextMixin):
    def get_context_data(self, **kwargs):
        context = super(CaregoryListMixin, self).get_context_data(**kwargs)
        context['current_url'] = self.request.path
        return context

class PageNumberMixin(CaregoryListMixin):
    def get_context_data(self, **kwargs):
        context = super(PageNumberMixin, self).get_context_data(**kwargs)
        try:
            context["pn"] = self.request.GET["page"]
        except KeyError:
            context["pn"] = "1"
        return context