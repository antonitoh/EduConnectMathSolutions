from django.urls import path
from .views import home, login, register ,calendario ,carrito

urlpatterns = [
    path('', home, name="home"),
    path('login/', login, name="login"),
    path('calendario/', calendario, name="calendario"),
    path('register/', register, name="register"),
    path('carrito/', carrito, name="carrito"),
]
