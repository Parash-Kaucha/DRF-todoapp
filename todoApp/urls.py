from django.urls import path
from todoApp import views

urlpatterns = [
    path('todoapi', views.ToDo_API.as_view()),
]
