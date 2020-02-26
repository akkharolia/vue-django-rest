from rest_framework import routers
from loginsys.viewsets import ProductViewset

router = routers.DefaultRouter()

router.register(r'product',ProductViewset)
