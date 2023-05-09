from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from fapp.models import *
from fapp.serializers import CategorySerializer


class Categories(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        result_dct = {}
        categories = Category.objects.all()





        sz = CategorySerializer(categories, many=True)
        return Response(sz.data)



