from django import forms
from .models import Book, Student, Gallery

# الفورم القديم للكتب (الذي يطلبه ملف views الحالي)
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

# فورم الطلاب للاب 11 (Task 1 & 2)
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        widgets = {
            'addresses': forms.CheckboxSelectMultiple(), # لاختيار عدة عناوين بسهولة
        }

# فورم معرض الصور للاب 11 (Task 3)
class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = ['title', 'picture']