from rest_framework import viewsets
from .models import Products
from .serializers import ProductSerializer
from rest_framework import filters,pagination
from django.contrib.auth.models import User

class ProductViewset(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['title', 'price']
    ordering = ['price']

