from django.urls import path
from . import views

urlpatterns = [
        path("djp-plugin/", views.demo_view, name="djp-demo"),
    ]
