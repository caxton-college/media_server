from django.urls import path

from . import views

urlpatterns = [
    path("", views.Index.as_view(), name="index"),
    path("image/random", views.FetchRandomImage.as_view(), name="random-image"),
]
