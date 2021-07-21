from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db.models.fields import DecimalField
from .authmanager import UsuarioManager


class UsuarioModel(AbstractBaseUser, PermissionsMixin):
    """Modelo de la base de datos del usuario del sistema"""
    TIPO_USUARIO = [
        (1, 'ADMINISTRADOR'),
        (2, 'USUARIO'),
        
    ]

    usuarioId = models.AutoField(
        primary_key=True,
        unique=True,
        db_column='usuario_id'
    )
    usuarioCorreo = models.EmailField(
        db_column='usuario_correo',
        max_length=30,
        verbose_name='Correo del usuario',
        unique=True
    )
    usuarioTipo = models.IntegerField(
        db_column='usuario_tipo',
        choices=TIPO_USUARIO,
        verbose_name='Tipo del usuario'
    )
    usuarioNombre = models.CharField(
        max_length=45,
        null=False,
        db_column='usuario_nombre',
        verbose_name='Nombre del usuario'
    )
    usuarioApellido = models.CharField(
        max_length=45,
        null=False,
        db_column='usuario_apellido',
        verbose_name='Apellido del usuario'
    )
    password = models.TextField(
        db_column='usuario_contrasena',
        verbose_name='Contraseña del usuario'
    )
  
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    
    objects = UsuarioManager()
    
    USERNAME_FIELD = 'usuarioCorreo'
   
    REQUIRED_FIELDS = ['usuarioNombre', 'usuarioTipo', 'usuarioApellido']

    class Meta:
        db_table = 't_usuario'
        verbose_name = 'usuario'
        verbose_name_plural = 'usuarios'

class CategoriaModel(models.Model):
    categoriaId = models.AutoField(
        primary_key=True,
        db_column="categoria_id",
        null=False
    )
    categoriaNombre = models.CharField(
        db_column='categoria_nombre',
        max_length=40,
        null=False,
        verbose_name='Nombre de categoria'
    )
    def __str__(self):
       return self.categoriaNombre
    
    class Meta:
        db_table = 't_categoria'
        verbose_name = 'Categoria'

class ProductoModel(models.Model):
    productoId = models.AutoField(
        primary_key=True,
        db_column='producto_id',
        null=False
    )
    productoNombre = models.CharField(
        db_column='producto_nombre',
        null=False,
        verbose_name='Nombre del producto',
        max_length=50
    )
    productoStock = models.IntegerField(
        db_column='producto_stock',
        verbose_name='Cantidad de los productos',
        null=False
    )
    productoFoto = models.ImageField(
        upload_to='producto/',
        db_column='producto_foto',
        verbose_name='Foto del producto',
        null=False
    )
    productoPrecio = models.DecimalField(
        db_column='producto_precio',
        max_digits=5,
        decimal_places=2,
        null=False,
        verbose_name='Precio del producto'
    )
    categoria=models.ForeignKey(
        to=CategoriaModel,
        on_delete=models.PROTECT,
        db_column='categoria_id',
        null=False
    )
    #campos de auditoria
    createdAt=models.DateTimeField(
        auto_now_add=True,
        db_column='created_at'
    )
    updateAt=models.DateTimeField(
        auto_now=True,
        db_column='update_at'
    )
    def __str__(self):
       return self.productoNombre

    class Meta:
        db_table = 't_producto'
        verbose_name = 'Producto'        


class PedidoModel(models.Model):

    TIPO_PAGO=[
        (1,'EFECTIVO'),
        (2,'TARJETA')
    ]


    pedidoId=models.AutoField(
        primary_key=True,
        unique=True,
        db_column='pedido_id'
    )
    pedidoFecha=models. DateField(
        db_column='pedido_fecha',
        null=False
    )
    
    pedidoTipoPago=models.IntegerField(
        db_column='pedido_tipopago',
        choices=TIPO_PAGO,
        verbose_name='Tipo de pago'

    )
    pedidoCantidad = models.IntegerField(
        db_column='pedido_cantidad',
        verbose_name='Cantidad de los pedidos',
        null=False
    )   
    producto=models.ForeignKey(
        to=ProductoModel,
        on_delete=models.PROTECT,
        null=False,
        db_column='producto_id',
        related_name='productoPedido'
    ) 
    usuario=models.ForeignKey(
        to=UsuarioModel,
        on_delete=models.PROTECT,
        db_column='usuario_id',
        related_name='usuarioPedido',
        null=False
    )


  
    
    class Meta:
        db_table = 't_pedido'
        verbose_name = 'Pedidos'


