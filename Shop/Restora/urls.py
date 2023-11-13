from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.home, name= 'home'),
    path('home/salads', views.show_salads, name= 'salads'),
    path('home/cold_dishes', views.show_cold_dishes, name= 'cold_dishes'),
    path('home/hot_dishes', views.show_hot_dishes, name= 'hot_dishes'),
    path('home/side_dishes', views.show_side_dishes, name= 'side_dishes'),
    path('home/desserts', views.show_desserts, name= 'desserts'),
    path('home/drinkables', views.show_drinkables, name= 'drinkables'),
    path('home/about', views.about, name= 'about'),
    path('home/contacts', views.contacts, name= 'contacts'),
]
