from rest_framework import serializers
from .models import Order, OrderItem

class OrderItemSerializer(serializers.ModelSerializer):
    model = OrderItem
    fields = ['product_item', 'quantity', 'price']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

class Meta:
    model = Order
    fields = ['id', 'created_at', 'total_price', 'items']