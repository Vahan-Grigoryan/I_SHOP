from os import getenv as _
import stripe, os
from fapp.models import OrderedProductInfo
from final_project import settings
from typing import List, Tuple
from loggeek import Logger 


stripe.api_key = _('stripe_secret_key')

logger = Logger(
    os.path.join(settings.BASE_DIR, 'logs', 'stripe_payments.log'),
    level="DEBUG",

)
#logger.add(
#    os.path.join(settings.BASE_DIR, 'logs', 'stripe_payments.log'),
#    level="DEBUG",
#    format="{level} {time:YYYY-MM-DD at HH:mm:ss} | {message}",
#)


class CardPaymentMixin:
    def create_customer(self, request_data) -> int | None:
        """
        If customer with name '{self.user.first_name} {self.user.last_name}' is not exist,
        create Stripe customer with payment_method_id received from front,
        else receive previously created customer with that name.
        """
        logger.debug(f'{self.user.email} | Creating customer')
        try:
            found_customers = stripe.Customer.search(
                query = f"metadata['user_id']:'{self.user.id}'",
                limit = 1,
            )["data"]
            if found_customers:
                customer = found_customers[0]
                logger.debug(f'{self.user.email} | Previously created customer received')
            else:
                customer = stripe.Customer.create(
                    email=self.user.email,
                    phone=self.user.tel,
                    payment_method=request_data.get('payment_method_id'),
                    invoice_settings={
                        'default_payment_method': request_data.get('payment_method_id')
                    },
                    metadata={
                        'user_id': self.user.id
                    },
                )
                
                logger.debug(f'{self.user.email} | Customer created')

        except Exception as e:
            # if eny error occured, delete model instance himself
            logger.error(f'{self.user.email} | Customer not created - {type(e).__name__}: {e}')
            self.delete()
            return
        else:
            # save customer id for refund later if needed
            self.customer_id = customer['id']
            self.save()
            return self.id

    def create_products_with_prices(self, order_pk) -> List[Tuple]:
        """Create Stripe Products, Prices and return Prices, quantities for invoice items structure"""
        logger.debug(f'{self.user.email} | Creating products(with prices)')
        price_ids_and_quantities = []
        try:
            for ordered_product in OrderedProductInfo.objects.filter(order_id=order_pk):
                product_with_price = stripe.Product.create(
                    name=ordered_product.product.name,
                    statement_descriptor='Bernu Veikals',
                    description=ordered_product.product.desc,

                    url=f'{settings.FRONT_HOST}/#/products/{ordered_product.product.id}',
                    default_price_data={
                        'currency': 'usd',
                        'unit_amount': (ordered_product.product.saled_price or ordered_product.product.price) * 100,
                    }
                )
                price_ids_and_quantities.append((product_with_price['default_price'], ordered_product.quantity))

            logger.debug(f'{self.user.email} | Products(with prices) created')
        except Exception as e:
            logger.error(f'{self.user.email} | Products(with prices) not created - {type(e).__name__}: {e}')

        return price_ids_and_quantities


    def create_invoice_items(self, price_ids_and_quantities, invoice_id) -> None:
        """Create invoice items for pointed invoice"""
        logger.debug(f'{self.user.email} | Creating invoice items')
        try:
            for price_id, quantity in price_ids_and_quantities:
                stripe.InvoiceItem.create(
                    customer=self.customer_id,
                    invoice=invoice_id,
                    currency='usd',
                    price=price_id,
                    quantity=quantity
                )
        except Exception as e:
            logger.error(f'{self.user.email} | Invoice items not created - {type(e).__name__}: {e}')
        else:
            logger.debug(f'{self.user.email} | Invoice items created')

    def create_and_pay_invoice(self, order) -> None:
        """Create and pay invoice"""
        logger.debug(f'{self.user.email} | Creating invoice')
        price_ids_and_quantities = self.create_products_with_prices(order.id)
        try:
            invoice = stripe.Invoice.create(
                customer=self.customer_id,
            )

        except Exception as e:
            logger.error(f'{self.user.email} | Invoice not created - {type(e).__name__}: {e}')
        else:
            logger.debug(f'{self.user.email} | Invoice created')
            self.invoice_id = invoice['id']
            self.save()
            self.create_invoice_items(price_ids_and_quantities, self.invoice_id)
            self.pay_invoice()

    def pay_invoice(self) -> None:
        """Pay invoice"""
        logger.debug(f'{self.user.email} | Paying invoice')
        try:
            stripe.Invoice.pay(self.invoice_id)
        except Exception as e:
            logger.error(f'{self.user.email} | Invoice not paid - {type(e).__name__}: {e}')
        else:
            logger.debug(f'{self.user.email} | Invoice paid')

    def create_refund(self) -> None:
        """Create refund"""
        logger.debug(f"{self.user.email} | Creating refund")
        invoice = stripe.Invoice.retrieve(self.invoice_id)
        try:
            stripe.Refund.create(charge=invoice["charge"])
        except Exception as e:
            logger.error(f"{self.user.email} | Refund not created - {type(e).__name__}: {e}")
        logger.debug(f"{self.user.email} | Refund created")


