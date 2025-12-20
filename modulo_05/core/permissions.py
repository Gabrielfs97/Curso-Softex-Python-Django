from rest_framework import permissions

class IsGerente(permissions.BasePermission):
    """
    Permissão customizada que concede acesso apenas se o usuário
    pertencer ao grupo 'Gerente'.
    """
    def has_permission(self, request, view):
        # 1. Verificação : Usuário deve estar logado
        if not request.user or not request.user.is_authenticated:
            return False
        # 2. Verificação de Grupo: Checa se 'Gerente' está na lista de grupos
        return request.user.groups.filter(name='Gerente').exists()


class IsAdminOrOwner(permissions.BasePermission):
    """
    Permissão customizada que permite acesso se:
    1. O usuário é admin/staff (is_staff = True) - tem acesso completo
    2. O usuário é o dono do objeto (para objetos que têm campo 'user')
    """
    def has_permission(self, request, view):
        # Permite acesso se o usuário estiver autenticado
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # 1. Se o usuário é admin, permite acesso a qualquer objeto
        if request.user.is_staff:
            return True
        # 2. Se o objeto tem um atributo 'user', verifica se é o dono
        if hasattr(obj, 'user'):
            return obj.user == request.user
        
        # 3. Se não tem atributo 'user', verifica se o objeto é o próprio usuário
        return obj == request.user