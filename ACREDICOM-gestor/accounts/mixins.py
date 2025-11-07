
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied

class AdminRequiredMixin(LoginRequiredMixin):
    admin_group_name = 'ADMINISTRADOR'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return super().dispatch(request, *args, **kwargs)
        if request.user.is_superuser or request.user.groups.filter(name=self.admin_group_name).exists():
            return super().dispatch(request, *args, **kwargs)
        raise PermissionDenied("No tienes permisos de administrador.")
