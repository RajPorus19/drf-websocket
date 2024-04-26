from books.models import Book, Library, Author, Borrower
from rest_framework import serializers


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"


class LibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Library
        fields = "__all__"


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"


class BorrowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borrower
        fields = "__all__"
