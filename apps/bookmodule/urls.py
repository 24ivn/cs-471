from django.urls import path
from . import views # استيراد ملف views من نفس المجلد [cite: 136]

urlpatterns = [
    path('', views.index), # المهمة 1 و 5 [cite: 138]
    path('index2/<int:val1>/', views.index2), # المهمة 3 [cite: 141]
    path('<int:bookId>', views.viewbook), # المهمة 7 [cite: 171]
]