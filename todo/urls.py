# todo/urls.py
from django.urls import path
from .views import todoView, addTodo

urlpatterns = [
	path('', todoView, name='home'),
	path('addTodo', addTodo, name='add')
]