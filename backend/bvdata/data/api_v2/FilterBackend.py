from django_filters import rest_framework as filters

__all__ = "AuthorizedFilterBackend"


class AuthorizedFilterBackend(filters.DjangoFilterBackend):
    def to_html(self, request, queryset, view):
        if request.user.is_authenticated:
            return super(AuthorizedFilterBackend, self).to_html(request, queryset, view)
        return ""
