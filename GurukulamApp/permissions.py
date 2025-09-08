

from rest_framework.permissions import BasePermission

from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdminOrReadOnly(BasePermission):
    """
    - Anyone (including unauthenticated users) can do safe methods (GET, HEAD, OPTIONS).
    - Only authenticated users with role 'admin' can perform write operations (POST, PUT, DELETE).
    """

    def has_permission(self, request, view):
        # Allow safe methods (GET, HEAD, OPTIONS) for everyone
        if request.method in SAFE_METHODS:
            return True

        # For other methods, only admins can access
        return (
            request.user.is_authenticated 
            and getattr(request.user, "role", None) == "admin"
        )
