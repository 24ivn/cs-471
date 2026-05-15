from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, Publisher, Author, Student, Gallery 
from django.db.models import Sum, F, ExpressionWrapper, FloatField, Min
from .forms import BookForm, StudentForm, GalleryForm 
from django.contrib.auth.decorators import login_required 
from django.contrib import messages 


@login_required(login_url='/users/login')
def lab9_task1(request):
    total_quantity = Book.objects.aggregate(total=Sum('quantity'))['total'] or 1
    books = Book.objects.annotate(
        availability_pct=ExpressionWrapper(
            (F('quantity') * 100.0) / total_quantity, 
            output_field=FloatField()
        )
    )
    return render(request, 'bookmodule/lab9_task1.html', {'books': books})

@login_required(login_url='/users/login')
def lab9_task2(request):
    publishers = Publisher.objects.annotate(total_stock=Sum('book__quantity'))
    return render(request, 'bookmodule/lab9_task2.html', {'publishers': publishers})

@login_required(login_url='/users/login')
def lab9_task3(request):
    publishers = Publisher.objects.annotate(oldest_book_date=Min('book__pubdate'))
    return render(request, 'bookmodule/lab9_task3.html', {'publishers': publishers})



@login_required(login_url='/users/login')
def lab10_listbooks(request):
    books = Book.objects.all()
    return render(request, 'bookmodule/lab10_listbooks.html', {'books': books})

@login_required(login_url='/users/login')
def lab10_addbook(request):
    if request.method == 'POST':
        t = request.POST.get('title')
        p = request.POST.get('price')
        q = request.POST.get('quantity')
        pd = request.POST.get('pubdate')
        pub_id = request.POST.get('publisher')
        
        publisher_obj = Publisher.objects.get(id=pub_id)
        Book.objects.create(title=t, price=p, quantity=q, pubdate=pd, publisher=publisher_obj)
        messages.success(request, "Book added successfully (Part 1)!")
        return redirect('/books/lab10/listbooks')
    
    publishers = Publisher.objects.all()
    return render(request, 'bookmodule/lab10_addbook.html', {'publishers': publishers})

@login_required(login_url='/users/login')
def lab10_editbook(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.price = request.POST.get('price')
        book.quantity = request.POST.get('quantity')
        book.pubdate = request.POST.get('pubdate')
        book.save()
        messages.info(request, "Book updated successfully!")
        return redirect('/books/lab10/listbooks')
    return render(request, 'bookmodule/lab10_editbook.html', {'book': book})

@login_required(login_url='/users/login')
def lab10_deletebook(request, id):
    book = get_object_or_404(Book, id=id)
    book.delete()
    messages.warning(request, "Book deleted!")
    return redirect('/books/lab10/listbooks')



@login_required(login_url='/users/login')
def lab11_list_students(request):
    students = Student.objects.all()
    return render(request, 'bookmodule/lab11_list_students.html', {'students': students})

@login_required(login_url='/users/login')
def lab11_add_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Student added successfully with addresses!")
            return redirect('/books/lab11/students')
    else:
        form = StudentForm()
    return render(request, 'bookmodule/lab11_add_student.html', {'form': form})

@login_required(login_url='/users/login')
def lab11_gallery(request):
    if request.method == "POST":
        form = GalleryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Image uploaded successfully!")
            return redirect('/books/lab11/gallery')
    else:
        form = GalleryForm()
    images = Gallery.objects.all()
    return render(request, 'bookmodule/lab11_gallery.html', {'form': form, 'images': images})



@login_required(login_url='/users/login')
def lab10_listbooks2(request):
    books = Book.objects.all()
    return render(request, 'bookmodule/lab10_listbooks2.html', {'books': books})

@login_required(login_url='/users/login')
def lab10_addbook2(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Book added successfully using Django Forms!")
            return redirect('/books/lab10/listbooks2')
    else:
        form = BookForm()
    return render(request, 'bookmodule/lab10_addbook2.html', {'obj': form})

@login_required(login_url='/users/login')
def lab10_editbook2(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            messages.info(request, "Book updated successfully!")
            return redirect('/books/lab10/listbooks2')
    else:
        form = BookForm(instance=book)
    return render(request, 'bookmodule/lab10_editbook2.html', {'obj': form})

@login_required(login_url='/users/login')
def lab10_deletebook2(request, id):
    book = get_object_or_404(Book, id=id)
    book.delete()
    messages.warning(request, "Book deleted successfully!")
    return redirect('/books/lab10/listbooks2')