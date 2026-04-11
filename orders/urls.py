from django.urls import path
from .views import *

urlpatterns = [
    path("coupons.validate/", CouponValidationView.as_view(),name="validate-coupon"),
    path("history/", OrderHistoryView.as_view, name='order-history'),
    path('coupons/', CouponListView.as_view(), name='coupons'),
    path('orders/<int:id>/', OrderDetailAPIView.as_view(), name='order_detail'),
]