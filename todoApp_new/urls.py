from django.urls import path
from todoApp_new import views

urlpatterns = [
    path('todoapi', views.todo_api),
]
