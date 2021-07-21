from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns=[
    path('categoria', CategoriaController.as_view()),
    path('categoria/<int:id>', CategoriasController.as_view()),
    path('registrocliente', RegistrarUsuarioController.as_view()),
    path('login', TokenObtainPairView.as_view()),
    path('refreshtoken', TokenRefreshView.as_view()),
    path('producto', ProductoController.as_view()),
    path('producto/<int:id>', ProductosController.as_view()),
    path('pedido',PedidoController.as_view()),
    path('pedido/<int:id>', PedidosController.as_view()),
]