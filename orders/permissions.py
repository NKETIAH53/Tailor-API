from rest_framework.permissions import BasePermission, IsAuthenticated
from .models import OrderPayment, Order


class ClientOrderReadDeletePermissions(BasePermission):
    message = "Clients can only view their orders.."

    def has_permission(self, request, view):
        user = request.user
        if user.role ==  'CLIENT' and request.method in ['GET', 'POST']:
            return True
        

    def has_object_permission(self, request, view, obj):
        if request.method in ["GET", "DELETE"] and obj.client == request.user:
            return True


class PaymentCreatePermission(BasePermission):
    message = "Only respective clients can pay for their orders."

    def has_permission(self, request, view):
        user = request.user
        if user.role ==  'CLIENT':
            if request.method in ['GET', 'POST']:
                Order.objects.filter(client_id=user.id)
                return True

            # elif request.method in ['POST', 'DELETE',]:
            #     print('-=====================================')
            #     if OrderPayment.objects.filter(order__client_id=user.id):
            #         print('-=====================================')
            #         return True

    # def has_obj_permission(self, request, view, obj):
    #     print(obj)
    #     if request.method == 'GET':
    #         return True

    #     elif request.method in ['POST', 'PUT', 'DELETE', 'PATCH']:
    #         if request.user == obj.store.store_owner:
    #             return True