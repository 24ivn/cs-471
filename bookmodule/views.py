from django.shortcuts import render

def links_view(request):
    return render(request, 'links.html')

def formatting_view(request):
    return render(request, 'formatting.html')

def listing_view(request):
    return render(request, 'listing.html')
def tables_view(request):
    return render(request, 'tables.html')