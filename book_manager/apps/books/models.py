from django.db import models


class Author(models.Model):

    name = models.TextField()

    surname = models.TextField()

    country = models.TextField()

    def __str__(self):
        return f'{self.name} {self.surname}'


class Category(models.Model):

    name = models.TextField()

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name


class Book(models.Model):

    title = models.TextField()

    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    year = models.IntegerField()

    publisher = models.TextField()

    isbn = models.TextField()

    location = models.TextField()

    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    for_sale = models.BooleanField(default=False)

    def __str__(self):
        return self.title
