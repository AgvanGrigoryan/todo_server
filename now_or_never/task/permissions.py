from django.http import HttpResponse


class AuthorPermissionMixin:
    def has_permission(self):
        return self.get_object().author == self.request.user or self.request.user.is_active and self.request.user.is_superuser

    def dispatch(self, request, *args, **kwargs):
        if not self.has_permission():
            return HttpResponse(status=403)
        return super().dispatch(request, *args, **kwargs)
