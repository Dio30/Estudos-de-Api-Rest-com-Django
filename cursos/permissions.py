from rest_framework import permissions

class SuperUser(permissions.BasePermission):
    
    def has_permission(self, request, view):
        if request.method == 'DELETE':
            if request.user.is_superuser:
                return True # permitir o delete
            return False # nao permitir o delete
        
        elif request.method == 'PUT':
            if request.user.is_superuser:
                return True # permitir o editar
            return False   # nao permitir o editar
        
        elif request.method == 'PATCH':
            if request.user.is_superuser:
                return True # permitir o editar
            return False   # nao permitir o editar
        return True # se for qualquer outro metodo de requisao(GET, POST) permitir o usuario de fazer método escolhido