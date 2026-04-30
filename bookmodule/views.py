from django.shortcuts import render
from .models import Book, Publisher, Author
from django.db.models import Sum, F, ExpressionWrapper, FloatField, Min

# Task 1: حساب النسبة المئوية لتوفر الكتب
def lab9_task1(request):
    total_quantity = Book.objects.aggregate(total=Sum('quantity'))['total'] or 1
    books = Book.objects.annotate(
        availability_pct=ExpressionWrapper(
            (F('quantity') * 100.0) / total_quantity, 
            output_field=FloatField()
        )
    )
    return render(request, 'bookmodule/lab9_task1.html', {'books': books})

# Task 2: عرض إجمالي مخزون الكتب لكل ناشر
def lab9_task2(request):
    # استخدام annotate مع Sum لحساب إجمالي الكمية لكل ناشر
    publishers = Publisher.objects.annotate(total_stock=Sum('book__quantity'))
    return render(request, 'bookmodule/lab9_task2.html', {'publishers': publishers})

# Task 3: عرض أقدم كتاب تم نشره لكل ناشر
def lab9_task3(request):
    # استخدام annotate مع Min لجلب تاريخ أول كتاب منشور
    publishers = Publisher.objects.annotate(oldest_book_date=Min('book__pubdate'))
    return render(request, 'bookmodule/lab9_task3.html', {'publishers': publishers})