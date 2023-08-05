from rest_framework import routers
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView

from kfsdutils.apps.docs.views.apibrowser import APIBrowserView

router = routers.DefaultRouter()
router.include_format_suffixes = False


urlpatterns = [
    path('', include(router.urls)),
    path('doc/schema/', SpectacularAPIView.as_view(), name='schema-api'),
    path("doc/", APIBrowserView.as_view(), name="schema-browser"),
]
