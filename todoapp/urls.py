from django.urls import path
from todoapp import views

app_name = 'todoapp'

urlpatterns = [
    path('', views.todolist, name='todolist'),
    path('delete/<list_id>', views.delete, name='delete'),
]
