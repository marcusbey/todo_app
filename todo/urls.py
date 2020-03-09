# todo/urls.py
from django.urls import path
from .views import todoView

urlpatterns = [
	path('', todoView, name='home'),
]