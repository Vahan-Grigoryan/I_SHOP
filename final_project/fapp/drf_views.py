from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from . import drf_pagination
import requests
from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from fapp import business
from fapp import serializers, drf_pagination
from django_filters import rest_framework as dfilters
from . import filters
from fapp.models import *
from fapp import mailing_logic


class UserMiniInfo(generics.RetrieveAPIView):
    """User mini info for site header"""
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.UserMiniInfoSerializer

    def get_object(self):
        """Get user by id, email"""
        url_params = self.request.GET
        assert (
            url_params.get('email') or
            url_params.get('id')
        ), 'Provide id, or email field'
        if url_params.get('email'):
            obj = get_object_or_404(User, email=url_params.get('email'))
        elif url_params.get('id'):
            obj = get_object_or_404(User, id=url_params.get('id'))

        self.check_object_permissions(self.request, obj)
        return obj

class UserDetailProfileInfo(generics.RetrieveAPIView):
    """User profile info for site profile page"""
    permission_classes = [IsAuthenticated]
    queryset = User.objects.distinct()
    serializer_class = serializers.UserProfileSerializer

class UserEditOrDel(generics.UpdateAPIView, generics.DestroyAPIView):
    """Update or delete User"""
    permission_classes = [IsAuthenticated]
    queryset = User.objects.distinct()
    serializer_class = serializers.UserCreationUpdateSerializer

class UserAddViewedProduct(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, user_pk, product_pk):
        """Detail in add_or_del_viewed_product() func"""
        business.add_or_del_viewed_product(user_pk, product_pk)
        return Response(status=204)

class UserAddOrDelLikedProduct(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, user_pk, product_pk):
        """Add product to user liked list"""
        user, product = User.objects.get(pk=user_pk), Product.objects.get(pk=product_pk)
        user.liked_products.add(product)
        return Response(status=204)

    def delete(self, request, user_pk, product_pk):
        """Remove product from user liked list"""
        user, product = User.objects.get(pk=user_pk), Product.objects.get(pk=product_pk)
        user.liked_products.remove(product)
        return Response(status=204)

class UserAddOrDelOrderProduct(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, user_pk, product_pk):
        business.add_order_product(user_pk, product_pk)
        return Response(status=204)

    def delete(self, request, user_pk, product_pk):
        """Del product from order and return updated order for ui"""
        business.del_order_product(user_pk, product_pk)
        user, product = User.objects.get(pk=user_pk), Product.objects.get(pk=product_pk)
        sz_order = serializers.OrderSerializer(user.orders.get(status='pending'))
        return Response(sz_order.data)

class MailingList(APIView):
    """View for add mail in Independent mail_list(possible to receive new product info without registration)"""
    def post(self, request):
        """Add or del(if exists) Independent mail logic"""
        if request.data.get('for_delete'):
            mailing_msg = mailing_logic.del_mail_from_mail_list(request.data.get('mail'))
            return Response(mailing_msg, status=202)
        else:
            mailing_msg = mailing_logic.send_first_mail_and_add_to_mail_list(request.data.get('mail'))
            return Response(mailing_msg, status=200)

class Registration(generics.CreateAPIView):
    """Common registration"""
    queryset = User.objects.all()
    serializer_class = serializers.UserCreationUpdateSerializer


class OAuthRegistration(APIView):
    rs = requests.Session()
    from_url = ''

    @classmethod
    def get(cls, request):
        """
        OAuth2:
        Redirect user to page where he can select google account,
        after select redirect user to relevant front page(where come from) with tokens and user data in cookies
        """
        code = request.GET.get('code')
        if code:

            raw_query = ''
            for key, value in request.GET.items():
                raw_query += f'{key}={value}&'

            authenticate = cls.rs.post(
                f'http://127.0.0.1:8000/auth/o/google-oauth2/?{raw_query[:-1]}',
            )
            username = authenticate.json()['user']
            user = User.objects.get(username=username)
            sz_user = serializers.UserMiniInfoSerializer(user)

            response = HttpResponseRedirect(cls.from_url)
            for key, value in sz_user.data.items():
                response.set_cookie(f'user_{key}', value)
            response.set_cookie('access', authenticate.json()['access'])
            response.set_cookie('refresh', authenticate.json()['refresh'])

            return response
        else:
            cls.from_url = f"{request.META['HTTP_REFERER']}#{request.GET.get('from_url')}"
            view_uri = request.build_absolute_uri('/oauth_registration')
            auth_url = cls.rs.get(f'http://127.0.0.1:8000/auth/o/google-oauth2?redirect_uri={view_uri}')
            auth_url = auth_url.json()['authorization_url']
            return redirect(auth_url)



class CategoryList(APIView):
    """Return nested/center categories"""
    def get(self, request):
        if request.GET.get('categories_position') == 'center':
            # return only center(without children and parents) categories for index front page
            format_categories = business.get_formatted_categories_for_front(categories_position='center')
        else:
            # return nested all categories
            format_categories = business.get_formatted_categories_for_front()
        return Response(format_categories)

class CategoryChildren(APIView):
    """Return children categories(only 1 level) of pointed category for mega_category front page"""
    def get(self, request, category_name):
        children = Category.objects.get(name=category_name).child_cats.all()
        sz = serializers.CategorySerializer(children, many=True)
        return Response(sz.data)

class CategoryProducts(APIView):
    """
    Return products of category(max category level is center).
    If current_product_id provided, from products it will be excluded.
    """
    def get(self, request, category_name):
        category = Category.objects.get(name=category_name)
        current_product_id = request.GET.get('current_product_id')

        if category.child_cats.count():
            child_cats = category.child_cats.all()
            products = Product.objects.filter(category__in=child_cats)
            sz = serializers.ProductListSerializer(products, many=True)
            return Response(sz.data)

        else:
            sz = serializers.ProductsOfCategory(category.products.exclude(id=current_product_id), many=True)
            return Response(sz.data[:5])

class ProductDetail(generics.RetrieveAPIView):
    queryset = Product.objects.prefetch_related('images')
    serializer_class = serializers.ProductDetailSerializer

class ProductList(generics.ListAPIView):
    """Products list specified by sale_new_hit property in model class for front index page"""
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

class BrandList(generics.ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = serializers.BrandSerializer
    pagination_class = drf_pagination.BrandsPagination

class BlogCategoryList(generics.ListAPIView):
    queryset = BlogCategory.objects.all()
    serializer_class = serializers.BlogCategoryListSerializer

class BlogIndexList(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = serializers.BlogListSerializer

class BlogList(generics.ListAPIView):
    """Show all blogs and filter"""
    serializer_class = serializers.BlogListSerializer
    pagination_class = drf_pagination.BlogsPagination
    filter_backends = (dfilters.DjangoFilterBackend,)
    filterset_class = filters.BlogFilters

    def get_queryset(self):
        if self.request.GET.get('sort_by') == 'latest':
            return Blog.objects.order_by('id').prefetch_related()
        else:
            return Blog.objects.order_by('-id').prefetch_related()

class BlogDetail(generics.RetrieveAPIView):
    queryset = Blog.objects.all()
    serializer_class = serializers.BlogDetailSerializer

class ReceiveQuestion(APIView):
    """This is used for receive question from user in the form at the bottom of the front index page"""
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

class CommentCreating(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer

    def perform_create(self, serializer):
        serializer.save(
            user_id=self.request.data.get('user_id'),
            product_id=self.request.data.get('product_id')
        )

class AvailableFilters(APIView):
    def get(self, request):
        """Return all available filters for filters front page except categories"""
        available_filters = business.get_available_filters()
        return Response(available_filters)

class FilteredProducts(generics.ListAPIView):
    """
    Return filtered products by url params.
    If not param in url return all products.
    """
    serializer_class = serializers.ProductListSerializer
    pagination_class = drf_pagination.FilteredProductsPagination
    filter_backends = (dfilters.DjangoFilterBackend,)
    filterset_class = filters.ProductFilter

    def get_queryset(self):
        if self.request.GET.get('sort_by') == 'latest':
            return Product.objects.order_by('id').prefetch_related()
        else:
            return Product.objects.order_by('-id').prefetch_related()

