from django.urls import path
from.import views

urlpatterns = [
    path("", views.is_newyear, name="newyear")
]
