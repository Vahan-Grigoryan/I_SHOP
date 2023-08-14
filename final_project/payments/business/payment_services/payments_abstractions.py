from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    """
    Class skeleton for any payment class(PayPal, PayU...),
    which send requests to available endpoints of payment method
    """
    name = 'paypal'
    paypal_api_domain = 'https://api-m.sandbox.paypal.com/'  # change to https://api-m.paypal.com/ in production

    @abstractmethod
    def parse_products_and_amount(self):
        pass

    @abstractmethod
    def get_access_token(self):
        pass

    @abstractmethod
    def create_order(self):
        pass

    @abstractmethod
    def capture_payment(self):
        pass

    @abstractmethod
    def refund_payment(self):
        pass