from django.contrib.auth.decorators import permission_required
from news.views import NewsListView, NewDetailView, NewCreateView, NewUpdateView, NewDeleteView
from django.conf.urls import url
from django.urls import path

urlpatterns = [
    url(r"^$", NewsListView.as_view(), name="news_index"),
    url(r"^(?P<pk>\d+)/$", NewDetailView.as_view(), name="news_detail"),
    url(r"^add/$", permission_required("news.add_new")(NewCreateView.as_view()), name="news_add"),
    url(r"^(?P<pk>\d+)/update/$", permission_required("news.change_new")(NewUpdateView.as_view()), name="news_update"),
    url(r"^(?P<pk>\d+)/delete/$", permission_required("news.delete_new")(NewDeleteView.as_view()), name="news_delete"),
]
