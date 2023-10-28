from rest_framework import serializers
from .models import Book
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

new_book = {"title": "Learning Python 2", "price": 3500}
