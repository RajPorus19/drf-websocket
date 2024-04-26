# apis tests
from books.models import Author, Book
from rest_framework.test import APITestCase
from django.urls import reverse


class TestBookViewSet(APITestCase):
    def setUp(self) -> None:
        self.author1 = Author.objects.create(name="Author 1", birth_date="1990-01-01")
        self.book1 = Book.objects.create(title="Book 1", author=self.author1)
        return super().setUp()
    def test_books_list(self):
        response = self.client.get(reverse("books-list"))
        self.assertEqual(response.status_code, 200)