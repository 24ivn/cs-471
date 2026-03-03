from django.shortcuts import render

def index(request):
    return render(request, "bookmodule/index.html") [cite: 213, 214]

def list_books(request):
    return render(request, 'bookmodule/list_books.html') [cite: 215, 216]

def viewbook(request, bookId):
    return render(request, 'bookmodule/one_book.html') [cite: 217, 218]

def aboutus(request):
    return render(request, 'bookmodule/aboutus.html') [cite: 219, 220]