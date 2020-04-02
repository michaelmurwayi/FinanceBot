from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    permissions to allow only account creaters to modify the
    """
    def has_account_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # write permissions given only to account creators
        return obj.owner == request.user