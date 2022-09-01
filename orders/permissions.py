from rest_framework.permissions import BasePermission


class ClientOrderDeletePermissions(BasePermission):
    message = "Only clients can create a store order."

    def has_permission(self, request, view):
        user = request.user
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True
            
        if user.role == "CL" and request.method in ["POST", "DELETE"]:
            return True

    def has_obj_permission(self, request, view, obj):
        if request.method in ["GET", "DELETE"]:
            if obj.client == request.user:
                return True
