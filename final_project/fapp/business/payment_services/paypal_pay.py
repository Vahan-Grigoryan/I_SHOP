import base64, requests, json
from typing import Tuple, List, Dict
from os import getenv as _
from requests import Response as requests_response
from django.http import HttpResponseRedirect


class PayPalPaymentMixin:
    @staticmethod
    def parse_products_and_amount(order) -> Tuple[List, Dict]:
        """Format order products for valid PayPal order creation payload(for items, amount options)"""
        from fapp.models import OrderedProductInfo # import inside the func to avoid circular import
        items = []
        for through_ordered_product in OrderedProductInfo.objects.filter(order=order):
            p_desc = through_ordered_product.product.desc if len(through_ordered_product.product.desc) <= 100 else through_ordered_product.product.desc[:100]
            items.append(
                {
                    "name": through_ordered_product.product.name,
                    "quantity": str(through_ordered_product.quantity),
                    "description": p_desc,
                    "unit_amount": {
                        "currency_code": "USD",
                        "value": str(through_ordered_product.product.saled_price or through_ordered_product.product.price)
                    },
                }
            )

        amount = {
            "currency_code": "USD",
            "value": str(order.total_price()), # should equal to item.quantity * item.unit_amount.value for each item
            "breakdown": {
                "item_total": {
                    "currency_code": "USD",
                    "value": str(order.total_price()), # should equal to item.quantity * item.unit_amount.value for each item
                }
            }
        }

        return items, amount

    def get_access_token(self) -> str:
        """
        Generate access token for requests later.
        """
        auth_data = f"{_('paypal_app_client_id')}:{_('paypal_app_secret_key')}"
        auth_data_bytes = auth_data.encode('ascii')
        base64_bytes = base64.b64encode(auth_data_bytes)
        base64_auth = base64_bytes.decode('ascii')
        response = requests.post(
            f'{self.paypal_api_domain}v1/oauth2/token',
            {'grant_type': 'client_credentials'},
            headers={
                'Content-Type': 'application/x-www-form-urlencoded',
                'Authorization': f'Basic {base64_auth}'
            }
        )
        return response.json()['access_token']

    def create_order(self, request, order, approved_url=None, cancel_url=None) -> HttpResponseRedirect | None:
        """
        Create order with items and amount, for detail see https://developer.paypal.com/docs/api/orders/v2/.
        After creation validate response and return redirect url to approve purchase page.
        args:
            request: request
            order: order model with products
            approved_url: front url for redirecting if  payment successfully approved
            cancel_url: front url for redirecting if  payment canceled

        Note: through approved_url will work paypal_capture_order/<int:id> url for server side operations, approved_url work after this
        """
        access_token = self.get_access_token()

        assert approved_url and cancel_url, 'Provide approve, cancel urls'

        # set through url for server side operations before redirect to front page
        approved_url = request.build_absolute_uri(f'/paypal_capture_order/{order.id}?front_redirect_url={approved_url}')

        items, amount = self.parse_products_and_amount(order)
        order = requests.post(
            f'{self.paypal_api_domain}v2/checkout/orders',
            json.dumps({
                "intent": "CAPTURE",
                "purchase_units": [
                    {
                        "reference_id": "ORDER_ID_FOR_UPDATE_(#)%",
                        "description": "Order from site site_name",
                        "amount": amount,
                        "items": items

                    }
                ],
                "payment_source": {
                    "paypal": {
                        "experience_context": {
                            "payment_method_preference": "IMMEDIATE_PAYMENT_REQUIRED",
                            "brand_name": "Bernu Veikals",
                            "locale": "en-US",
                            "landing_page": "LOGIN", # GUEST_CHECKOUT for register(or login) new PayPal acc
                            "shipping_preference": "GET_FROM_FILE", # SET_PROVIDED_ADDRESS for point addresses
                            "user_action": "PAY_NOW",
                            "return_url": approved_url,
                            "cancel_url": cancel_url,
                        }
                    }
                }
            }),
            headers={
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {access_token}',
                'Prefer': 'return=representation',
            }
        )
        if all((
            order.json()['status'] == 'PAYER_ACTION_REQUIRED',
            order.json()['purchase_units'][0]['payee']['email_address'] == 'Dj_bussiness@gmail.com',
            order.status_code == 200
        )):
            self.order_id = order.json()['id']
            self.save()
            # return url that redirect to href with rel: payer-action(for receive user approve) for front page
            return order.json()['links'][1]['href']

        return

    def capture_payment(self) -> requests_response:
        """Capture confirmed payment and set capture_id for refund later"""
        access_token = self.get_access_token()
        response = requests.post(
            f'{self.paypal_api_domain}v2/checkout/orders/{self.order_id}/capture',
            headers={
                'Authorization': f'Bearer {access_token}',
                'Content-Type': 'application/json'
            }

        )
        if response.status_code == 201:
            self.capture_id = response.json()['purchase_units'][0]['payments']['captures'][0]['id']
            self.save()
        return response

    def refund_payment(self) -> requests_response:
        """Refund payment and return response(with 201 status if successfully refunded)"""
        access_token = self.get_access_token()
        response = requests.post(
            f'{self.paypal_api_domain}v2/payments/captures/{self.capture_id}/refund',
            headers={
                'Authorization': f'Bearer {access_token}',
                'Content-Type': 'application/json'
            }
        )
        return response