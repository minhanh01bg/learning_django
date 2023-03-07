# todo/todo_api/urls.py : API urls.py
from django.urls import path, include
from .views import (
    TodoListApiView,
    TodoDetailAptView,
    createUser
)

urlpatterns = [
    path('api', TodoListApiView.as_view()),
    path('api/<int:todo_id>', TodoDetailAptView.as_view()),
    path('api-auth', createUser.as_view()),
]