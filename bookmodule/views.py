from django.shortcuts import render
from .models import Book # استيراد الموديل [cite: 42]

# --- 1. البحث (دمج Lab 6 و Lab 7) ---
def search(request):
    if request.method == "POST":
        keyword = request.POST.get('keyword', '').strip()
        isTitle = request.POST.get('option1')
        isAuthor = request.POST.get('option2')
        
        # استخدام ORM للبحث الحقيقي في قاعدة البيانات [cite: 46]
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


# --- 2. الاستعلام البسيط (Task 3) [cite: 40] ---
def simple_query(request):
    # استرجاع الكتب التي يحتوي عنوانها على 'and' [cite: 46]
    mybooks = Book.objects.filter(title__icontains='and')
    return render(request, 'bookmodule/bookList.html', {'books': mybooks})


# --- 3. الاستعلام المعقد (Task 4) [cite: 59] ---
def lookup_query(request):
    # شروط البحث: المؤلف موجود، العنوان فيه 'and'، الطبعة >= 2، السعر > 100 [cite: 63, 64]
    mybooks = Book.objects.filter(author__isnull=False).filter(title__icontains='and').filter(edition__gte=2).exclude(price__lte=100)[:10]
    
    if len(mybooks) >= 1:
        return render(request, 'bookmodule/bookList.html', {'books': mybooks})
    else:
        # قمنا بتعديلها لتوجيهك لصفحة البحث (search) بدلاً من index لتجنب الأخطاء
        return render(request, 'bookmodule/search.html')


# --- 4. الدوال المساعدة لضمان عمل كافة الروابط ---
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