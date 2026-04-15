from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search', views.search, name='search'), 
    
    path('simple/query', views.simple_query, name='simple_query'), 
    path('complex/query', views.lookup_query, name='complex_query'), 
    
    path('html5/links', views.links_view),
    path('html5/text/formatting', views.formatting_view),
    path('html5/listing', views.listing_view),
    path('html5/tables', views.tables_view),
    path('lab8/task1', views.lab8_task1),
path('lab8/task2', views.lab8_task2),
path('lab8/task3', views.lab8_task3),
path('lab8/task4', views.lab8_task4),
path('lab8/task5', views.lab8_task5),
path('lab8/task7', views.lab8_task7),
]