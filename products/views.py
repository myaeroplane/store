from django.shortcuts import render
from datetime import datetime
from products.models import Product, ProductCategory

current_date = datetime.now()

# Create your views here.
# контроллеры = вьювс (вьюхи) = функции

def index(request):
    context = {
        'tittle': 'Store',
        'current_date': current_date,
    }
    return render(request, 'products/index.html', context)


def products(request):
    context = {
        'tittle': 'Catalog',
        'categories': ProductCategory.objects.all(),
        'products': Product.objects.all(),
              }
    return render(request, 'products/products.html', context)

def test_context(request):
    context = {
        'tittle': 'тестовый контекст',
        'head': 'Приветствую!',
        'text': 'Привет, это моя тестовая страница',
        'products': [
            {
                'name': 'Худи черного цвета с монограммами adidas Originals',
                'price': 6053.00,
            },
            {
                'name': 'Синяя куртка The North Face',
                'price': 7045.00,
            },
            {
                'name': 'Коричневый спортивный oversized-топ ASOS DESIGN',
                'price': 4878.50,
            },
        ],
        'promotion': True,
        'products_of_promotion': [
            {
                'name': 'Черный рюкзак Nike Heritage',
                'price': 2036.00,
            },
        ],
    }
    return render(request, 'products/test_context.html', context)

