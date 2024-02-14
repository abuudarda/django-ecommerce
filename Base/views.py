from django.shortcuts import render
from Items.models import Category, Product
# Create your views here.
def index(request):
    items = Product.objects.all()
    categories = Category.objects.all()
    return render(request, 'Base/index.html', {'items': items, 'categories': categories})

def contact(request):
    return render(request, 'Base/contact.html')
