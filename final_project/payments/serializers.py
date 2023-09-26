from rest_framework import serializers
from payments.models import StripePayment


class StripePaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StripePayment
        fields = '__all__'
