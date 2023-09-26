from django.shortcuts import redirect
from rest_framework.generics import get_object_or_404, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from final_project import settings
from payments.business import db_manipulations
from fapp.models import Order
from fapp.serializers import OrderSerializer
from payments.models import StripePayment
from payments.serializers import StripePaymentSerializer


class PayPalCreateOrder(APIView):
    """ Create order and return redirect url to approve page for front page """
    permission_classes = [IsAuthenticated]

    def post(self, request, order_pk):
        approve_url = db_manipulations.paypal_create_order(request, order_pk)
        if approve_url:
            return Response({'purchase_url': approve_url})

        return Response({'detail': 'Order not created'})


class PayPalCaptureOrder(APIView):
    """
    Capture approved order, this view work on through url
    between server and front approved_url redirect page,
    for server side operations
    """
    def get(self, request, order_pk):
        response = db_manipulations.paypal_capture_order_payment(order_pk)
        if response.status_code == 201:
            return redirect(
                request.GET.get('front_redirect_url'),
                captured=True
            )

        return Response({'detail': 'Order not captured'})


class PayPalReceiveOrder(APIView):
    """View for approve that order products successfully received"""
    permission_classes = [IsAuthenticated]

    def get(self, request, order_pk):
        order = db_manipulations.paypal_receive_order(order_pk)
        return redirect(f'{settings.FRONT_HOST}/#/profile/{order.user.id}')


class PayPalRefundOrder(APIView):
    """Refund payment and return changed order"""
    permission_classes = [IsAuthenticated]

    def get(self, request, order_pk):
        response = db_manipulations.paypal_refund_order_payment(order_pk)
        if response.status_code == 201:
            order = get_object_or_404(Order, id=order_pk)
            sz_data = OrderSerializer(order).data
            return Response(sz_data)

        return Response({'detail': 'Order not refunded'})


class StripeCreateCardOwner(APIView):
    """
    Receive user card data from front,
    create customer in Stripe with card
    """
    permission_classes = [IsAuthenticated]

    def post(self, request):
        stripe_payment_id = db_manipulations.stripe_create_card_owner(request)

        if stripe_payment_id:
            return Response({'stripe_payment_id': stripe_payment_id})
        return Response({'detail': 'Что то пошло не так'})


class StripeDelCardFromOwner(DestroyAPIView):
    permission_classes = [IsAuthenticated]

    queryset = StripePayment.objects.all()
    serializer_class = StripePaymentSerializer


class StripePayOrder(APIView):
    """Pay pointed order with customer's card"""
    permission_classes = [IsAuthenticated]

    def get(self, request, order_pk):
        changed_order = db_manipulations.stripe_pay_order(
            request.user.id,
            order_pk
        )
        sz_data = OrderSerializer(changed_order).data
        return Response(sz_data)


class StripeRefundOrder(APIView):
    """Refund pointed order with customer's card"""
    permission_classes = [IsAuthenticated]

    def get(self, request, order_pk):
        changed_order = db_manipulations.stripe_refund_order(
            request.user.id,
            order_pk
        )
        sz_data = OrderSerializer(changed_order).data
        return Response(sz_data)


