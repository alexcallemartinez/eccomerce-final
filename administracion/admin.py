from django.contrib import admin
from .models import UsuarioModel,CategoriaModel,ProductoModel,PedidoModel

# Register your models here.


admin.site.register(UsuarioModel)
admin.site.register(CategoriaModel)
admin.site.register(ProductoModel)
admin.site.register(PedidoModel)