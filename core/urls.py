from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # Real pages are matched before the placeholder catch-all, so a nav link
    # built with {% url 'placeholder_page' 'our-mentors' %} keeps working and
    # simply lands on the built page instead of the "under construction" stub.
    path('page/our-mentors/', views.mentors, name='mentors'),
    path('page/<slug:slug>/', views.placeholder_page, name='placeholder_page'),
]
