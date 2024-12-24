from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect

from products.models import ProductCategory, Product, Basket
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    context = {
        'title': 'Частный репетитор',
        'username': 'Mihail',
        'is_promotion': True,
    }
    return render(request, 'products/index.html', context)

def products(request, category_id=None, page_number=1):
    products = Product.objects.filter(category_id=category_id) if category_id else Product.objects.all()
    per_page = 3
    paginator=Paginator(products, per_page)
    products_paginator = paginator.page(page_number)

    context = {
        'title': 'Store - Каталог',
        #'products': Product.objects.all(),
        'products': products_paginator,
        'categories': ProductCategory.objects.all(),
    }
    return render(request, 'products/products.html', context)

#добавление товара в корзину:
@login_required()
def basket_add(request, product_id): #передаются доп данные - product_id
    product = Product.objects.get(id=product_id) #этот продукт кладем в корзину
    # берем все элементы корзины которые принадлежат пользователю, который выполняет
    # запрос и также всзять все корзины с даннным продуктом, то
    # есть возьмутся все корзины пользовтеля с определеннным продуктом:
    baskets = Basket.objects.filter(user=request.user, product=product)


    if not baskets.exists(): #если queryset у нас пустой
        Basket.objects.create(user=request.user, product=product, quantity=1)
    else:
        basket=baskets.first() #можно и last() - без разницы - потому что все равно один товар
        basket.quantity += 1
        basket.save()
    #возвращаем польовталея на то же место где он выполнил запрос
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

@login_required
def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])