import base64, requests, json, os
from loggeek import Logger 
from typing import Tuple, List, Dict
from os import getenv as _
from final_project import settings
from requests import Response as requests_response
from django.http import HttpResponseRedirect


logger = Logger(
    os.path.join(settings.BASE_DIR, 'logs', 'paypal_payments.log'),
    level="DEBUG",

)
#logger.add(
#    os.path.join(settings.BASE_DIR, 'logs', 'paypal_payments.log'),
#    level="DEBUG",
#    format="{level} {time:YYYY-MM-DD at HH:mm:ss} | {message}",
#)
class PayPalPaymentMixin:
    name = 'paypal'
    paypal_api_domain = 'https://api-m.sandbox.paypal.com/'  # change to https://api-m.paypal.com/ in production


    @staticmethod
    def parse_products_and_amount(order) -> Tuple[List, Dict]:
        """Format order products for valid PayPal order creation payload(for items, amount options)"""
        from fapp.models import OrderedProductInfo # import inside the func to avoid circular import


        logger.info('Parsing order products, amount')
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
        logger.info('Order products, amount parsed')

        return items, amount

    def get_access_token(self) -> str | None:
        """
        Generate access token for requests later.
        """
        logger.info('Generating access token')

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
        if 'access_token' not in response.json():
            logger.error(f'Access token not received, response status code - {response.status_code}')
            return
        else:
            logger.info(f'Access token received')
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

        Note: through approved_url will work paypal_capture_order/<int:id> url for server side operations,
        approved_url work after this
        """
        logger.info('Creating order')
        access_token = self.get_access_token()

        assert approved_url and cancel_url, 'Provide approve, cancel urls'

        # set through url for server side operations before redirect to front page
        approved_url = request.build_absolute_uri(f'/paypal_capture_order/{order.id}?front_redirect_url={approved_url}')
        logger.info('Set through url between server and front')

        items, amount = self.parse_products_and_amount(order)
        order_api = requests.post(
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
            order_api.json().get('status') == 'PAYER_ACTION_REQUIRED',
            order_api.json().get('purchase_units')[0]['payee']['email_address'] == 'Dj_bussiness@gmail.com',
            order_api.status_code == 200
        )):
            self.order_id = order_api.json()['id']
            self.save()
            logger.info('Order created')
            # return url that redirect to href with rel: payer-action(for receive user approve) for front page
            return order_api.json()['links'][1]['href']

        logger.error(f'Order not created, response status code - {order_api.status_code}')
        return

    def capture_payment(self) -> requests_response:
        """Capture confirmed payment and set capture_id for refund later"""
        logger.info('Capturing order payment')
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
            logger.info('Order payment captured')
        else:
            logger.error(f'Order payment not captured, response status code - {response.status_code}')

        return response

    def refund_payment(self) -> requests_response:
        """Refund payment and return response(with 201 status if successfully refunded)"""
        logger.info('Refunding order payment')
        access_token = self.get_access_token()
        response = requests.post(
            f'{self.paypal_api_domain}v2/payments/captures/{self.capture_id}/refund',
            headers={
                'Authorization': f'Bearer {access_token}',
                'Content-Type': 'application/json'
            }
        )
        if response.status_code != 201:
            logger.error(f'Order payment not refunded, response status code - {response.status_code}')
        else:
            logger.info('Order payment captured')

        return response
