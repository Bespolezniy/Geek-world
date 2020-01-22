from django.views.generic.base import View

class PageNumberView(View):
    def post(self, request, *args, **kwargs):
        try:
            pn = request.GET["page"]
        except KeyError:
            pn = "1"
        self.success_url = self.success_url + "?page" + pn
        return super(PageNumberView, self).post(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        try:
            self.sort = self.request.GET["order"]
        except KeyError:
            self.order = "A"
        return super(PageNumberView, self).get(request, *args, **kwargs)