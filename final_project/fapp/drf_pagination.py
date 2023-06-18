from rest_framework.pagination import PageNumberPagination

class FilteredProductsPagination(PageNumberPagination):
    page_size = 4
    page_size_query_param = 'page_size'
    page_query_param = 'pg'

class BlogsPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    page_query_param = 'pg'