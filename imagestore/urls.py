from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from imagestore.views import get_list, upload_file, delete_file

urlpatterns = [
    url(r"^$", login_required(get_list), name="imagestore_index"),
    url(r"^upload/$", login_required(upload_file), name="imagestore_upload"),
    url(r"^(?P<pk>\d+)/delete/$", login_required(delete_file), name="imagestore_delete"),
]