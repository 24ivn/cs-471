from django import forms
from .models import Book, Student, Gallery

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        widgets = {
            'addresses': forms.CheckboxSelectMultiple(), 
        }

class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = ['title', 'picture']