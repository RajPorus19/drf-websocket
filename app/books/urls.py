from books.apis import BookViewSet, LibraryViewSet, AuthorViewSet, BorrowerViewSet
from django.urls import path

urlpatterns = [
    path(
        "books/",
        BookViewSet.as_view({"get": "list", "post": "create"}),
        name="books-list",
    ),
    path(
        "books/<int:pk>/",
        BookViewSet.as_view(
            {"get": "retrieve", "put": "update", "delete": "destroy"},
            name="books-detail",
        ),
    ),
    path(
        "libraries/",
        LibraryViewSet.as_view({"get": "list", "post": "create"}),
        name="libraries-list",
    ),
    path(
        "libraries/<int:pk>/",
        LibraryViewSet.as_view(
            {"get": "retrieve", "put": "update", "delete": "destroy"},
            name="libraries-detail",
        ),
    ),
    path(
        "authors/",
        AuthorViewSet.as_view({"get": "list", "post": "create"}),
        name="authors-list",
    ),
    path(
        "authors/<int:pk>/",
        AuthorViewSet.as_view(
            {"get": "retrieve", "put": "update", "delete": "destroy"},
            name="authors-detail",
        ),
    ),
    path(
        "borrowers/",
        BorrowerViewSet.as_view({"get": "list", "post": "create"}),
        name="borrowers-list",
    ),
    path(
        "borrowers/<int:pk>/",
        BorrowerViewSet.as_view(
            {"get": "retrieve", "put": "update", "delete": "destroy"},
            name="borrowers-detail",
        ),
    ),
]
