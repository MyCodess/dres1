from django.urls import path

from . import views

app_name = "ap1"
urlpatterns = [
    path("", views.index, name="index"),
]

