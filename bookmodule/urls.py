from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search', views.search, name='search'), # رابط البحث من لاب 6
    
    # --- روابط Lab 7 الجديدة ---
    path('simple/query', views.simple_query, name='simple_query'), # Task 3
    path('complex/query', views.lookup_query, name='complex_query'), # Task 4
    
    # الروابط القديمة لضمان عمل السيرفر
    path('html5/links', views.links_view),
    path('html5/text/formatting', views.formatting_view),
    path('html5/listing', views.listing_view),
    path('html5/tables', views.tables_view),
]