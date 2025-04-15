from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.greet, name="greet"),
    path("hilde", views.hilde, name="hilde"),
    path("manu", views.manu, name="manu")
]