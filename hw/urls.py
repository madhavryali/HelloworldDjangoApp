from django.urls import path
from hw import views

urlpatterns = [
    path("", views.home, name="home"),
]