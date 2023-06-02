import json, requests

from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import redirect
from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from fapp.business import get_formatted_categories_for_front
from fapp import serializers, drf_pagination
from django_filters import rest_framework as dfilters
from . import filters
from fapp.models import *
from fapp import mailing_logic



class UserDetailProfileInfo(generics.RetrieveAPIView):
    """User profile info for site profile page"""
    permission_classes = [IsAuthenticated]
    queryset = User.objects.distinct()
    serializer_class = serializers.UserProfileSerializer


class UserMiniInfo(generics.RetrieveAPIView):
    """User mini info for site header"""
    serializer_class = serializers.UserSerializer

    def get_object(self):
        """Get user by id or email"""
        url_params = self.request.GET
        assert url_params.get('email') or url_params.get('id'), 'Provide id or email field'
        if url_params.get('email'):
            obj = get_object_or_404(User, email=url_params.get('email'))
        elif url_params.get('id'):
            obj = get_object_or_404(User, id=url_params.get('id'))

        self.check_object_permissions(self.request, obj)
        return obj


class MailingList(APIView):
    def post(self, request):
        if request.data.get('for_delete'):
            mailing_msg = mailing_logic.del_mail_from_mail_list(request.data.get('mail'))
            return Response(mailing_msg, status=202)
        else:
            mailing_msg = mailing_logic.send_first_mail_and_add_to_mail_list(request.data.get('mail'))
            return Response(mailing_msg, status=200)

class Registration(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

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

class CategoryProducts(APIView):
    def get(self, request, category_name):
        """
        Return products of category(max category level is center).
        If current_product_id provided, from products it will be excluded.
        """
        category = Category.objects.get(name=category_name)
        current_product_id = request.GET.get('current_product_id')

        if category.child_cats.count():
            child_cats = category.child_cats.all()
            products = Product.objects.filter(category__in=child_cats)
            sz = serializers.ProductsOfCategory(products, many=True)
            return Response(sz.data)

        else:
            sz = serializers.ProductsOfCategory(category.products.exclude(id=current_product_id), many=True)
            return Response(sz.data[:5])

class ProductDetail(generics.RetrieveAPIView):
    queryset = Product.objects.prefetch_related('images')
    serializer_class = serializers.ProductDetailSerializer

class ProductList(generics.ListAPIView):
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
