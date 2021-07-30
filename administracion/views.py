from .permissions import administradorPost
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework import response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from .serializers import *
from .models import *
from uuid import uuid4
from django.conf import settings
import os


class CategoriaController(generics.ListCreateAPIView):
    queryset = CategoriaModel.objects.all()
    serializer_class=CategoriaSerializer
      

    def get(self, request):
        respuesta=self.serializer_class(
            instance=self.get_queryset(), many=True)
        return Response({
            'success':True,
            'content':respuesta.data,
            'message':None
          })
    def post(self, request):
        nuevaCategoria=self.serializer_class(data=request.data)
        if nuevaCategoria.is_valid():
            nuevaCategoria.save()
            return Response({
             'success':True,
             'content':nuevaCategoria.data,
             'message':'Categoria creado exitosamente'
           }, status.HTTP_201_CREATED)
        else:
            return Response({
                'success': False,
                'content': nuevaCategoria.errors,
                'message': 'Error al crear el nuevo Usuario'
            }, status.HTTP_400_BAD_REQUEST)

class CategoriasController(generics.RetrieveUpdateDestroyAPIView):
    queryset=CategoriaModel.objects.all()
    serializer_class=CategoriaSerializer

    def get_queryset(self, id):
        return CategoriaModel.objects.get(categoriaId=id)

    def get(self, request, id):
        resultado = self.serializer_class(instance=self.get_queryset(id))
        return Response({
            'success':True,
            'content':resultado.data,
            'message':'Categoria Encontrada'
        }) 
    def put(self, request, id):
        categoria= self.get_queryset(id)
        respuesta=self.serializer_class(instance=categoria,data=request.data)
        if respuesta.is_valid():
            respuesta.update()
            return Response(data={
                     "success":True,
                     "content":respuesta.update(),
                     "message":"se actualizo correctamente" 
                }) 
        else:
            return Response(data={
                    "success":False,
                     "content":respuesta.errors,
                     "message":"Data incorrecta"  
                },status=status.HTTP_400_BAD_REQUEST)        

    def delete(self, request, id):
        categoria= self.get_queryset(id)
        categoria.delete()
        return Response({
            'success':True,
            'content':None,
            'message':'se elimino correctamente'
        })        

class RegistrarUsuarioController(generics.CreateAPIView):
    serializer_class = RegistroUsuarioSerializer

    def post(self, request):
        nuevoUsuario = self.serializer_class(data=request.data)
        if nuevoUsuario.is_valid():
            nuevoUsuario.save()
            return Response({
                'success': True,
                'content': nuevoUsuario.data,
                'message': 'Usuario creado exitosamente'
            }, status.HTTP_201_CREATED)
        else:
            return Response({
                'success': False,
                'content': nuevoUsuario.errors,
                'message': 'Error al crear el nuevo Usuario'
            }, status.HTTP_400_BAD_REQUEST)


      

class ProductoController(generics.ListCreateAPIView):
    queryset = ProductoModel.objects.all()
    serializer_class=ProductoSerializer
      

    def get(self, request):
        respuesta=self.serializer_class(
            instance=self.get_queryset(), many=True)
        return Response({
            'success':True,
            'content':respuesta.data,
            'message':None
          })
    def post(self, request):
        #formato=request.FILES['productoFoto'].name.split('.')[1]
        #nombre=str(uuid4())+'.'+formato
        #request.FILES['productoFoto'].name=nombre
        respuesta=self.serializer_class(data=request.data)
        if respuesta.is_valid():
            respuesta.save()
            return Response({
             'success':True,
             'content':respuesta.data,
             'message':'Producto creado exitosamente'
           }, status.HTTP_201_CREATED)
        else:
            return Response({
                'success': False,
                'content': respuesta.errors,
                'message': 'Error al crear el Producto'
            }, status.HTTP_400_BAD_REQUEST)   

class ProductosController(generics.RetrieveUpdateDestroyAPIView):
    queryset=ProductoModel.objects.all()
    serializer_class=ProductoSerializer

    def get_queryset(self, id):
        return ProductoModel.objects.get(productoId=id)

    def get(self, request, id):
        resultado = self.serializer_class(instance=self.get_queryset(id))
        return Response({
            'success':True,
            'content':resultado.data,
            'message':'Producto encontrado'
        }) 
    def put(self, request, id):
        producto= self.get_queryset(id)
        #formato=request.FILES['productoFoto'].name.split('.')[1]
        #nombre=str(uuid4())+'.'+formato
        #request.FILES['productoFoto'].name=nombre
        respuesta=self.serializer_class(instance=producto,data=request.data)
        if respuesta.is_valid():
            respuesta.update()
            return Response(data={
                     "success":True,
                     "content":respuesta.update(),
                     "message":"se actualizo correctamente" 
                }) 
        else:
            return Response(data={
                    "success":False,
                     "content":respuesta.errors,
                     "message":"Data incorrecta"  
                },status=status.HTTP_400_BAD_REQUEST)        

    def delete(self, request, id):
        producto= self.get_queryset(id)
        #foto= str(producto.productoFoto)
        #try:

         #   ruta_imagen=settings.MEDIA_RUT / foto
         #   os.remove(ruta_imagen)

        #except:
         #   print('fotografia del producto no existe') 
        producto.delete()
        return Response({
            'success':True,
            'content':None,
            'message':'se elimino correctamente'
        }) 

class PedidoController(generics.CreateAPIView):
    queryset = PedidoModel.objects.all()
    serializer_class=PedidosEscrituraSerializer
    serializer_class1=PedidosLecturaSerializer
 
    #permission_classes=[IsAuthenticated]  
    #permission_classes=[IsAuthenticatedOrReadOnly,administradorPost]
    def get(self, request):
        respuesta=self.serializer_class1(instance=self.get_queryset(), many=True)
        return Response({
            'success':True,
            'content':respuesta.data,
            'message':None
          })
    def post(self, request):
        nuevaGasto=self.serializer_class(data=request.data)
        if nuevaGasto.is_valid():
            nuevaGasto.save()
            return Response({
             'success':True,
             'content':nuevaGasto.data,
             'message':'Pedido creado exitosamente'
           }, status.HTTP_201_CREATED)
        else:
            return Response({
                'success': False,
                'content': nuevaGasto.errors,
                'message': 'Error al crear el nuevo Pedido'
            }, status.HTTP_400_BAD_REQUEST)

class PedidosController(generics.RetrieveUpdateDestroyAPIView):
    queryset=PedidoModel.objects.all()
    serializer_class=PedidosEscrituraSerializer
    
    def get_queryset(self, id):
        return PedidoModel.objects.get(pedidoId=id)

    def get(self, request, id):
        resultado = self.serializer_class(instance=self.get_queryset(id))
        return Response({
            'success':True,
            'content':resultado.data,
            'message':'Pedido encontrado'
        }) 
    def put(self, request, id):
        pedido= self.get_queryset(id)
        respuesta=self.serializer_class(instance=pedido,data=request.data)
        if respuesta.is_valid():
            respuesta.update()
            return Response(data={
                     "success":True,
                     "content":respuesta.update(),
                     "message":"se actualizo correctamente" 
                }) 
        else:
            return Response(data={
                    "success":False,
                     "content":respuesta.errors,
                     "message":"Data incorrecta"  
                },status=status.HTTP_400_BAD_REQUEST)        


    def delete(self, request, id):
        pedido= self.get_queryset(id)
        pedido.delete()
        return Response({
            'success':True,
            'content':None,
            'message':'se elimino correctamente'
        })
