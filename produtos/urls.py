from django.urls import path
from . import views

app_name = 'produtos'

urlpatterns = [
    path('novo/', views.produto_new, name='produto_new'),
    path('', views.produto_lista, name='produto_lista'),
]
