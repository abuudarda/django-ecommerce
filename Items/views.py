from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.
def detail(request, pk):
    item = get_object_or_404(Product, pk=pk)
    related_items = item.objects.filter(category=item.category).exclude(pk=pk)[0:3]
    return render(request, 'Item/index.html',{'item':item, 'related_items':related_items})