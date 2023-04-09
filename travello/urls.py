from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Kerala/', views.Kerala, name='Kerala'),
    path('Chennai/', views.Chennai, name='Chennai'),
    path('Rajasthan/', views.Rajasthan, name='Rajasthan'),
]