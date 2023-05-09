from rest_framework import serializers
from fapp.models import *


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        exclude = 'parent',