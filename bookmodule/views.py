from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, Publisher, Author
from django.db.models import Sum, F, ExpressionWrapper, FloatField, Min
from .forms import BookForm  

def lab9_task1(request):
    total_quantity = Book.objects.aggregate(total=Sum('quantity'))['total'] or 1
    books = Book.objects.annotate(
        availability_pct=ExpressionWrapper(
            (F('quantity') * 100.0) / total_quantity, 
            output_field=FloatField()
        )
    )
    return render(request, 'bookmodule/lab9_task1.html', {'books': books})

def lab9_task2(request):
    publishers = Publisher.objects.annotate(total_stock=Sum('book__quantity'))
    return render(request, 'bookmodule/lab9_task2.html', {'publishers': publishers})

def lab9_task3(request):
    publishers = Publisher.objects.annotate(oldest_book_date=Min('book__pubdate'))
    return render(request, 'bookmodule/lab9_task3.html', {'publishers': publishers})



def lab10_listbooks(request):
    books = Book.objects.all()
    return render(request, 'bookmodule/lab10_listbooks.html', {'books': books})

def lab10_addbook(request):
    if request.method == 'POST':
        t = request.POST.get('title')
        p = request.POST.get('price')
        q = request.POST.get('quantity')
        pd = request.POST.get('pubdate')
        pub_id = request.POST.get('publisher')
        
        publisher_obj = Publisher.objects.get(id=pub_id)
        Book.objects.create(title=t, price=p, quantity=q, pubdate=pd, publisher=publisher_obj)
        return redirect('/books/lab9_part1/listbooks')
    
    publishers = Publisher.objects.all()
    return render(request, 'bookmodule/lab10_addbook.html', {'publishers': publishers})

def lab10_editbook(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.price = request.POST.get('price')
        book.quantity = request.POST.get('quantity')
        book.pubdate = request.POST.get('pubdate')
        book.save()
        return redirect('/books/lab9_part1/listbooks')
    return render(request, 'bookmodule/lab10_editbook.html', {'book': book})

def lab10_deletebook(request, id):
    book = get_object_or_404(Book, id=id)
    book.delete()
    return redirect('/books/lab9_part1/listbooks')



def lab10_listbooks2(request):
    books = Book.objects.all()
    return render(request, 'bookmodule/lab10_listbooks2.html', {'books': books})

def lab10_addbook2(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/books/lab9_part2/listbooks')
    else:
        form = BookForm()
    return render(request, 'bookmodule/lab10_addbook2.html', {'obj': form})

def lab10_editbook2(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('/books/lab9_part2/listbooks')
    else:
        form = BookForm(instance=book)
    return render(request, 'bookmodule/lab10_editbook2.html', {'obj': form})

def lab10_deletebook2(request, id):
    book = get_object_or_404(Book, id=id)
    book.delete()
    return redirect('/books/lab9_part2/listbooks')