from django.urls import path
from . import views

urlpatterns = [
    # المهمة الأولى: عرض النسبة المئوية للتوفر
    path('lab9/task1', views.lab9_task1),
    
    # المهمة الثانية: عرض إجمالي مخزون الكتب لكل ناشر
    path('lab9/task2', views.lab9_task2),
    
    # المهمة الثالثة: عرض أقدم كتاب لكل ناشر
    path('lab9/task3', views.lab9_task3),
]