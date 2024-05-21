from django.shortcuts import render, redirect

from book_app.forms import BookForm
# Create your views here.


from book_app.models import *


def index(request):
    books = Book.objects.all()
    return render(request, "index.html", {"books": books})


def book_details(request, book_id):
    book = Book.objects.get(id=book_id)
    return render(request, "book_details.html", {"book": book})


def book_add(request):
    if request.method == "GET":
        form = BookForm()
    else:
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/")

    return render(request, 'book_add.html', {"form": form})
