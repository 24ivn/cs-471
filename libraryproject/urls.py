from django.contrib import admin
from django.urls import include, path # تأكدي من وجود كلمة include هنا 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', include("apps.bookmodule.urls")), # توجيه الروابط لتطبيق الكتب 
]