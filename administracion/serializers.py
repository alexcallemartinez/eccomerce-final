from .models import *
from django.db.models import fields
from rest_framework import serializers


class CategoriaSerializer(serializers.ModelSerializer):

    def update(self):
        print(self.instance)
        print(self.validated_data)
        self.instance.categoriaNombre = self.validated_data.get("categoriaNombre")
        self.instance.save()

        return self.data
        

    class Meta:
        model = CategoriaModel
        fields = '__all__'

        
class ProductoSerializer(serializers.ModelSerializer):
    def update(self):
        print(self.instance)
        print(self.validated_data)
        self.instance.productoNombre = self.validated_data.get("productoNombre")
        self.instance.productoCantidad = self.validated_data.get("productoCantidad")
        self.instance.productoFoto = self.validated_data.get("productoFoto")
        self.instance.productoPrecio = self.validated_data.get("productoPrecio")
        self.instance.categoria = self.validated_data.get("categoria")
        self.instance.save()

        return self.data



    class Meta:
        model=ProductoModel
        fields='__all__'


class RegistroUsuarioSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def save(self):
        usuarioCorreo = self.validated_data.get('usuarioCorreo')
        usuarioTipo = self.validated_data.get('usuarioTipo')
        usuarioNombre = self.validated_data.get('usuarioNombre')
        usuarioApellido = self.validated_data.get('usuarioApellido')
        password = self.validated_data.get('password')

        is_staff = False
        nuevoUsuario = UsuarioModel(
            usuarioCorreo=usuarioCorreo,
            usuarioTipo=usuarioTipo,
            usuarioNombre=usuarioNombre,
            usuarioApellido=usuarioApellido,
            is_staff=is_staff
        )
        # encriptamos la contraseña
        nuevoUsuario.set_password(password)
        nuevoUsuario.save()
        return nuevoUsuario

    class Meta:
        model = UsuarioModel
        # excluimos grupos porque no va a tener acceso al panel administrativo al igual que user_permissions (ambos sirven para indicar que puede hacer en el panel administrativo)
        exclude = ['groups', 'user_permissions'] 


class MostrarProductoSerializer(serializers.ModelSerializer):

    class Meta:
        model=ProductoModel
        fields=['productoNombre','productoFoto','productoPrecio']

class PedidosEscrituraSerializer(serializers.ModelSerializer):
    
    def update(self):
        print(self.instance)
        print(self.validated_data)
        self.instance.pedidoFecha = self.validated_data.get("pedidoFecha")
        self.instance.pedidoTipoPago = self.validated_data.get("pedidoTipoPago")
        self.instance.pedidoCantidad = self.validated_data.get("pedidoCantidad")
        self.instance.producto = self.validated_data.get("producto")
        self.instance.usuario = self.validated_data.get("usuario")
        self.instance.save()

        return self.data
    
    class Meta:
        model = PedidoModel
        fields = '__all__'

class PedidosLecturaSerializer(serializers.ModelSerializer):
   

    producto=MostrarProductoSerializer(many=False, read_only=True)
    class Meta:
        model = PedidoModel
        fields = '__all__'


