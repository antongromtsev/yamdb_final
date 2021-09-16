from rest_framework import filters
from rest_framework.pagination import PageNumberPagination

from ..models.categories import Category
from ..permissions import IsAdminOrReadOnly
from ..serializers.categories import CategorySerializer
from .base import MixinViewSet


class CategoryViewSet(MixinViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = PageNumberPagination
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    lookup_field = 'slug'
