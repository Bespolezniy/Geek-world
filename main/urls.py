from django.conf.urls import url
from main.views import MainPageView

urlpatterns = [
    url(r'^main/$', MainPageView.as_view(), name='main')
]
