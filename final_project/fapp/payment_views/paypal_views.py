from django.shortcuts import redirect
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from fapp.business import db_manipulations
from fapp.models import Order
from fapp.serializers import OrderSerializer


class CreateOrder(APIView):
    """ Create order and return redirect url to approve page for front page """
    permission_classes = [IsAuthenticated]
    def post(self, request, order_pk):
        approve_url = db_manipulations.paypal_create_order(request, order_pk)
        if approve_url:
            return Response({'purchase_url': approve_url})

        return Response({'detail': 'Order not created'})

class CaptureOrder(APIView):
    """
    Capture approved order,
    this view work on through url between server and front approved_url redirect page for server side operations
    """
    def get(self, request, order_pk):
        response = db_manipulations.paypal_capture_order_payment(order_pk)
        if response.status_code == 201:
            return redirect(request.GET.get('front_redirect_url'), captured=True)

        return Response({'detail': 'Order not captured'})

class RefundOrder(APIView):
    """Refund payment and return changed order"""
    def get(self, request, order_pk):
        response = db_manipulations.paypal_refund_order_payment(order_pk)
        if response.status_code == 201:
            order = get_object_or_404(Order, id=order_pk)
            sz_data = OrderSerializer(order).data
            return Response(sz_data)

        return Response({'detail': 'Order not refunded'})