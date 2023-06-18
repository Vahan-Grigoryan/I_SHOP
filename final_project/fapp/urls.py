from django.urls import path
from fapp import drf_views

urlpatterns = [
    path('registration', drf_views.Registration.as_view()),
    path('oauth_registration', drf_views.OAuthRegistration.as_view()),
    path('users_mini_info', drf_views.UserMiniInfo.as_view()),
    path('users_profile/<int:pk>', drf_views.UserDetailProfileInfo.as_view()),
    path('mailing_list', drf_views.MailingList.as_view()),
    path('receive_mail', drf_views.ReceiveQuestion.as_view()),
    path('categories', drf_views.CategoryList.as_view()),
    path('category_children/<str:category_name>', drf_views.CategoryChildren.as_view()),
    path('category_products/<str:category_name>', drf_views.CategoryProducts.as_view()),
    path('brands_index', drf_views.BrandIndexList.as_view()),
    path('blogs_index', drf_views.BlogIndexList.as_view()),
    path('blogs', drf_views.BlogList.as_view()),
    path('blogs/<int:pk>', drf_views.BlogDetail.as_view()),
    path('blog_categories', drf_views.BlogCategoryList.as_view()),
    path('products_index', drf_views.ProductList.as_view()),
    path('products/<int:pk>', drf_views.ProductDetail.as_view()),
    path('comments', drf_views.CommentCreating.as_view()),
    path('filter_products', drf_views.FilteredProducts.as_view()),
    path('available_filters', drf_views.AvailableFilters.as_view()),

]