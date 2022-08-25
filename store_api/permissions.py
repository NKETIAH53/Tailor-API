from rest_framework.permissions import BasePermission
from .models import Store

class StoreOwnerWritePermissions(BasePermission):
    message = "Only store owners can edit store information"

    def has_permission(self, request, view):
        if request.method in ['POST', 'PUT', 'DELETE', 'PATCH']:
            if request.user.role == "STORE_OWNER":
                return True

        elif request.method == 'GET':
            return True

    def has_object_permission(self, request, view, obj):
        if request.method == 'GET':
            return True

        elif request.method in ['PUT', 'PATCH', 'DELETE']:
            if request.user == obj.store_owner:
                return True


class BranchCreatePermission(BasePermission):
    message = "Only respective store owners can create and edit store branch information."

    def has_permission(self, request, view):
        print('===============================')
        if request.method == 'GET':
            print('===============================zzzzzzzz')
            return True

        elif request.method in ['POST', 'PUT', 'DELETE', 'PATCH']:
            print('=========================aaaaaaaaaaa')
            if Store.storeobjects.filter(store_owner=request.user).exists():
                print('sssssssssssss===========================zzzzzzzz')
                return True

    def has_obj_permission(self, request, view, obj):
        print('===============================')
        if request.method == 'GET':
            print('======gjgnlhke;hgnlk ==========')
            return True

        elif request.method in ['POST', 'PUT', 'DELETE', 'PATCH']:
            print('========786451226453653===============')
            if request.user == obj.store.store_owner:
                print('===============================zzzzzzzz')
                return True
        