from django.urls import path
from . import views

urlpatterns = [
	path('', views.index),
	path('2001/', views.special_2001),
	path('<year>/', views.years),
	]
