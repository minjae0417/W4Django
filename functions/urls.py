from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index),
    path('image/', views.image),
    path('lucky/', views.lucky, name="lucky"),
    path('birthday/', views.birthday),
    path('ranking/', views.ranking),
    path('language/<str:name>/', views.language),
]