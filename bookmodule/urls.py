from django.urls import path
from . import views

urlpatterns = [
    path('lab9/task1', views.lab9_task1),
    
    path('lab9/task2', views.lab9_task2),
    
    path('lab9/task3', views.lab9_task3),
    path('lab9_part1/listbooks', views.lab10_listbooks),
    path('lab9_part1/addbook', views.lab10_addbook),
    path('lab9_part1/editbook/<int:id>', views.lab10_editbook),
    path('lab9_part1/deletebook/<int:id>', views.lab10_deletebook),
    path('lab9_part2/listbooks', views.lab10_listbooks2),
    path('lab9_part2/addbook', views.lab10_addbook2),
    path('lab9_part2/editbook/<int:id>', views.lab10_editbook2),
    path('lab9_part2/deletebook/<int:id>', views.lab10_deletebook2),
]
