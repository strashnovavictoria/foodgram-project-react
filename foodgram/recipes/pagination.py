from rest_framework.pagination import PageNumberPagination


class LimitPaginaton(PageNumberPagination):
    page_size_query_param = 'limit'