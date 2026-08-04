from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('page/<slug:slug>/', views.placeholder_page, name='placeholder_page'),
]
