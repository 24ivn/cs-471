from django.urls import path
from . import views  # هنا الاستيراد الصحيح

urlpatterns = [
    path('html5/links', views.links_view),
    path('html5/text/formatting', views.formatting_view),
    path('html5/listing', views.listing_view),
    path('html5/tables', views.tables_view),
]