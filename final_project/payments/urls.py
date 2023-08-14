from django.urls import path
from payments import drf_views


urlpatterns = [
    path('paypal_create_order/<int:order_pk>', drf_views.PayPalCreateOrder.as_view()),
    path('paypal_capture_order/<int:order_pk>', drf_views.PayPalCaptureOrder.as_view()),
    path('paypal_receive_order/<int:order_pk>', drf_views.PayPalReceiveOrder.as_view()),
    path('paypal_refund_order/<int:order_pk>', drf_views.PayPalRefundOrder.as_view()),
]