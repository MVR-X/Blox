from django.urls import path
from . import views

urlpatterns = [
    path('dummy/', views.dummy, name='dummy'),
    path('', views.home, name=''),
]