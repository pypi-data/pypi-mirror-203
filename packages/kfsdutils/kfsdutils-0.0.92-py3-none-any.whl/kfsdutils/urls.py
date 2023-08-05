from django.urls import path, include, re_path
from django.views.generic.base import RedirectView

urlpatterns = [
    re_path(r'^$', RedirectView.as_view(url='doc/', permanent=False), name='index'),
    path('', include('kfsdutils.apps.endpoints.urls')),
]
