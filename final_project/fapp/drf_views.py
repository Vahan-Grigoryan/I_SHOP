from django.core.mail import send_mail
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from fapp.business import get_formatted_categories_for_front
from fapp import serializers
from django_filters import rest_framework as dfilters

from final_project import settings
from . import filters
from fapp.models import *
from fapp import mailing_logic


class MailingList(APIView):
    def post(self, request):
        if request.data.get('for_delete'):
            mailing_msg = mailing_logic.del_mail_from_mail_list(request.data.get('mail'))
            return Response(mailing_msg, status=202)
        else:
            mailing_msg = mailing_logic.send_first_mail_and_add_to_mail_list(request.data.get('mail'))
            return Response(mailing_msg, status=200)


class CategoryList(APIView):

    def get(self, request):
        if request.GET.get('categories_position') == 'center':
            format_categories = get_formatted_categories_for_front(categories_position='center')
        else:
            format_categories = get_formatted_categories_for_front()
        return Response(format_categories)

class CategoryChildren(APIView):
    def get(self, request, category_name):
        children = Category.objects.get(name=category_name).child_cats.all()
        sz = serializers.CategorySerializer(children, many=True)
        return Response(sz.data)

class ProductDetail(generics.RetrieveAPIView):
    queryset = Product.objects.prefetch_related('images')
    serializer_class = serializers.ProductDetailSerializer

    def get(self, request, *args, **kwargs):
        mailing_logic.send_msg_to_all_mails('TEST T1', 'TEST MSG1')
        return super().get(request, *args, **kwargs)

class ProductIndexList(generics.ListAPIView):
    serializer_class = serializers.ProductListSerializer

    def get_queryset(self):
        products = filters.filter_by_sale_new_hit(self.request.GET)
        return products

    def get(self, request, *args, **kwargs):
        if self.request.GET.get('sale_new_hit'):
            return super().get(request, *args, **kwargs)
        else:
            return Response({'ERROR': 'Provide sale_new_hit request param'})

class BrandIndexList(generics.ListAPIView):
    queryset = Brand.objects.all()[:12]
    serializer_class = serializers.BrandSerializer

class BlogIndexList(generics.ListAPIView):
    queryset = Blog.objects.all()[:6]
    serializer_class = serializers.BlogSerializer

class ReceiveQuestion(APIView):
    def post(self, request):
        if request.data.get('mail_msg_tel'):
            send_mail(
                request.data.get('mail_msg_name'),
                'tel: ' + request.data.get('mail_msg_tel') + '\n\n' + request.data.get('mail_msg_body'),
                request.data.get('mail_msg_mail'),
                (settings.EMAIL_HOST_USER, ),
                fail_silently=False,
            )
        else:
            send_mail(
                request.data.get('mail_msg_name'),
                request.data.get('mail_msg_body'),
                request.data.get('mail_msg_mail'),
                (settings.EMAIL_HOST_USER,),
                fail_silently=False,
            )
        return Response(status=200)