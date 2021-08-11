from django.shortcuts import render
from .models import Author, Book


def author_detail(request, pk):

    author_obj = Author.objects.get(pk=pk)

    book_objs = Book.objects.filter(category=author_obj.id)

    context = {
        'author': author_obj,
        'books': book_objs
    }

    return render(request, 'books/author_detail.html', context)
