
from . import views
from django.urls import path
urlpatterns = [
    path('/getData', views.testdata),
    ]