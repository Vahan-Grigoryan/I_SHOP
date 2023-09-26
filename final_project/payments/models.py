from django.db import models
from fapp.models import User
from payments.business.payment_services.paypal_pay import PayPalPaymentMixin
from payments.business.payment_services.stripe_pay import CardPaymentMixin



class PayPalPayment(models.Model, PayPalPaymentMixin):
    """
    PayPal's payment integration model.
    use like that:
        1)Call create_order(), this method will create order with PayPal api,
        set order_id property for capture payment later,
        set through url between server and approve_url for server side operations before redirecting to front,
        return url(or None if any error occurred) for user can approve payment

        2)In through url(before redirecting to front page) view call capture_payment(),
        this method will set capture_id property for refund later if needed
        and return response(with 201 status_code if payment successfully captured)

        3)Optional. Call refund_payment() if user want refund,
        this method return response(with 201 status_code if payment successfully refunded)
    """
    order_id = models.CharField(max_length=200, null=True, blank=True)
    capture_id = models.CharField(max_length=200, null=True, blank=True)

class StripePayment(models.Model, CardPaymentMixin):
    """"""
    name = 'stripe'
    user = models.OneToOneField('fapp.User', on_delete=models.CASCADE, related_name='stripe_payment')
    invoice_id = models.CharField(max_length=200, null=True, blank=True)
    customer_id = models.CharField(max_length=200, null=True, blank=True)

