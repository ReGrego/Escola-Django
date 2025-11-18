from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('alunos.urls')), #incluindo as urls do app alunos
    path('produtos/', include('produtos.urls',  namespace='produtos')), #incluindo as urls do app produtos
]
    