from rest_framework.permissions import BasePermission, SAFE_METHODS

class soloAdministrador(BasePermission):
    def has_permission(self, request, view):
        print(SAFE_METHODS)
        print(request.user.usuarioTipo)
        if request.user.usuarioTipo == 1:
            return True

        else:    
            return False


class administradorPost(BasePermission):
    def has_permission(self, request, view):
        print(type(view))
        if request.method == 'POST':
            if request.user.usuarioTipo==1:
                return True
            else:
                return False
        else:            
            return True      

class soloUsuarios(BasePermission):
    def has_permission(self, request, view):
        #solamente pueden ser usuarios simples
        if request.user.usuarioTipo == 2:
            return True
        return False   