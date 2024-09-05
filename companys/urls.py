from django.urls import path

from .views import RegView

urlpatterns = [
    path("", RegView.as_view(), name="menu"),
]