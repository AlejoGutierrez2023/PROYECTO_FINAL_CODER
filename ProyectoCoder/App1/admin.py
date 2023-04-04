from django.contrib import admin
from .models import*

# Register your models here.

# admin.site.register(Blog)

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Blog._meta.get_fields()]

    def has_delete_permission(self, request, obj=None):
        # Permitir que los usuarios con permisos de superusuario puedan eliminar cualquier blog
        if request.user.is_superuser:
            return True
        # Permitir que los usuarios puedan eliminar solo sus propios blogs
        if obj is not None and (obj.author == request.user or request.user.has_perm('App1.can_delete_any_blog')):
            return True
        return False


    def has_change_permission(self, request, obj=None):
        # Permitir que los usuarios con permisos de superusuario puedan editar cualquier blog
        if request.user.is_superuser:
            return True
        # Permitir que los usuarios puedan editar solo sus propios blogs
        if obj is not None and (obj.author == request.user or request.user.has_perm('App1.can_edit_any_blog')):
            return True
        return False