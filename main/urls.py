from django.urls import path, include
from .import views

urlpatterns= [
    path('', views.main, name="main"),
    path('/answer', views.send_question, name="send_question"),
    path('/log', views.send_to_log, name='send_to_log'),
    ]