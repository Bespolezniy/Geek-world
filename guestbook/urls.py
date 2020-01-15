from guestbook.views import GuestbookView
from django.conf.urls import url

urlpatterns = [
    url(r"^$", GuestbookView.as_view(), name="guestbook"),
]
