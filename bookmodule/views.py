from django.shortcuts import render
from .models import Book, Address, Student 
from django.db.models import Q, Count, Sum, Avg, Max, Min 

def search(request):
    if request.method == "POST":
        keyword = request.POST.get('keyword', '').strip()
        isTitle = request.POST.get('option1')
        isAuthor = request.POST.get('option2')
        
        if isTitle and isAuthor:
            books = Book.objects.filter(title__icontains=keyword) | Book.objects.filter(author__icontains=keyword)
        elif isTitle:
            books = Book.objects.filter(title__icontains=keyword)
        elif isAuthor:
            books = Book.objects.filter(author__icontains=keyword)
        else:
            books = Book.objects.all()
            
        return render(request, 'bookmodule/bookList.html', {'books': books})
    
    return render(request, 'bookmodule/search.html')


def simple_query(request):
    mybooks = Book.objects.filter(title__icontains='and')
    return render(request, 'bookmodule/bookList.html', {'books': mybooks})


def lookup_query(request):
    mybooks = Book.objects.filter(author__isnull=False).filter(title__icontains='and').filter(edition__gte=2).exclude(price__lte=100)
    
    if len(mybooks) >= 1:
        return render(request, 'bookmodule/bookList.html', {'books': mybooks})
    else:
        return render(request, 'bookmodule/search.html')


def index(request):
    return render(request, 'bookmodule/index.html')

def links_view(request):
    return render(request, 'bookmodule/links.html')

def formatting_view(request):
    return render(request, 'bookmodule/formatting.html')

def listing_view(request):
    return render(request, 'bookmodule/listing.html')

def tables_view(request):
    return render(request, 'bookmodule/tables.html')

def lab8_task1(request):
    books = Book.objects.filter(Q(price__lte=80)) 
    return render(request, 'bookmodule/bookList.html', {'books': books})

def lab8_task2(request):
    # استخدام & للربط بين الشروط و | للاختيار بين العنوان أو المؤلف 
    query = Q(edition__gt=3) & (Q(title__icontains='qu') | Q(author__icontains='qu')) 
    books = Book.objects.filter(query)
    return render(request, 'bookmodule/bookList.html', {'books': books})

def lab8_task3(request):
    # استخدام ~ للنفي (NOT) 
    query = Q(edition__lte=3) & ~(Q(title__icontains='qu') | Q(author__icontains='qu')) 
    books = Book.objects.filter(query)
    return render(request, 'bookmodule/bookList.html', {'books': books})

def lab8_task4(request):
    books = Book.objects.all().order_by('title') 
    return render(request, 'bookmodule/bookList.html', {'books': books})

def lab8_task5(request):
    stats = Book.objects.aggregate(
        total_books=Count('id'),
        total_price=Sum('price'),
        avg_price=Avg('price'),
        max_price=Max('price'),
        min_price=Min('price')
    ) 
    return render(request, 'bookmodule/lab8_stats.html', {'stats': stats})

# في نهاية ملف bookmodule/views.py
def lab8_task7(request):
    # استخدام annotate لحساب عدد الطلاب في كل مدينة
    cities = Address.objects.annotate(student_count=Count('student'))
    return render(request, 'bookmodule/city_stats.html', {'cities': cities})