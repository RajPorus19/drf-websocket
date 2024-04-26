from django.db import models

# Create your models here.
# create a model book, library, and borrower


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey("Author", on_delete=models.CASCADE)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Library(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)


class Author(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField()

    def __str__(self):
        return self.name


class Borrower(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField("Book")

    def __str__(self):
        return self.name
