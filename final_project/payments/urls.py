from django.urls import path
from payments import drf_views


urlpatterns = [
    path('stripe_create_card_owner', drf_views.StripeCreateCardOwner.as_view()),
    path('stripe_del_card_from_owner/<int:pk>', drf_views.StripeDelCardFromOwner.as_view()),
    path('stripe_pay_order/<int:order_pk>', drf_views.StripePayOrder.as_view()),
    path('stripe_refund_order/<int:order_pk>', drf_views.StripeRefundOrder.as_view()),

    path('paypal_create_order/<int:order_pk>', drf_views.PayPalCreateOrder.as_view()),
    path('paypal_capture_order/<int:order_pk>', drf_views.PayPalCaptureOrder.as_view()),
    path('paypal_receive_order/<int:order_pk>', drf_views.PayPalReceiveOrder.as_view()),
    path('paypal_refund_order/<int:order_pk>', drf_views.PayPalRefundOrder.as_view()),
]
