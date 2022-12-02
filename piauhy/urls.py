from django.contrib import admin
from django.urls import path, include
from app.views import home, novo_usuario, produto

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name= "home"),
    path('cadastro/', novo_usuario),
    path('produto/', produto),
]
