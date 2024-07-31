from django.shortcuts import render, get_object_or_404
from catalog.models import Product, Category


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'new message from {name}({email}): {message}')

    category_list = [{'name': 'подарки для вас'}, {'name': 'подарки для нас'}]
    context = {
        "category_list": category_list
    }

    return render(request, 'contacts.html', context)


def home(request):
    product_list = Product.objects.all()
    category_list = Category.objects.all()
    context = {
        "product_list": product_list,
        "category_list": category_list
    }
    return render(request, 'home.html', context)


def product(request, pk):
    product_ = get_object_or_404(Product, pk=pk)
    context = {
        "product_": product_
    }
    return render(request, 'product.html', context)
