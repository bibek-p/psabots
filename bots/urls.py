from django.urls import path

from . import views

urlpatterns = [
    path('sendcoupon', views.index, name='index'),
]