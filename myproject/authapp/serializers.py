# from rest_framework import serializers
# from django.contrib.auth.models import User

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id', 'username', 'email']
from rest_framework import serializers
from .models import Contact, Address, Product, Cart, Order, Payment, OrderPlaced

# Contact Serializer
class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

# Address Serializer
class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'

# Product Serializer
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

# Cart Serializer
class CartSerializer(serializers.ModelSerializer):
    total_cost = serializers.ReadOnlyField()

    class Meta:
        model = Cart
        fields = '__all__'

# Order Serializer
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

# Payment Serializer
class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

# OrderPlaced Serializer
class OrderPlacedSerializer(serializers.ModelSerializer):
    total_cost = serializers.ReadOnlyField()

    class Meta:
        model = OrderPlaced
        fields = '__all__'
