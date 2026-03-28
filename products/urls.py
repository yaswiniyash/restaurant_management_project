from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', ProductViewSet)

urlpatterns = router.urls
