from rest_framework import serializers

# from models import Product
# from models import Review

from .models import Product, Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['__all__']
    # реализуйте все поля

class ProductListSerializer(serializers.Serializer):
    title = serializers.CharField()
    price = serializers.DecimalField(10, 2)
    # реализуйте поля title и price

class ProductDetailsSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    class Meta:
        model = Product
        fields = ['title', 'description', 'price', 'comments']
    # реализуйте поля title, description, price и reviews (список отзывов к товару)
