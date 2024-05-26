from django.core.exceptions import PermissionDenied

def verificar_limite_publicaciones(user):
    if user.publicaciones_actuales() >= user.publicaciones_permitidas():
        raise PermissionDenied("Has alcanzado el límite de publicaciones permitidas para tu plan.")