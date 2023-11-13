from django.shortcuts import render, redirect
from . import models
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import get_object_or_404
from Cart.forms import CartAddProductForm   #форма корзины
# Create your views here.


def home (request):
    return render(request, 'home.html', {'home':home})

def about (request):
    return render(request, 'about.html', {'about':about})

def contacts (request):
    return render(request, 'contacts.html', {'contacts':contacts})

def show_salads (request):
    viewed_salads = request.session.get('viewed_salads',[])
    salads = models.Dishes.objects.filter(category__name='Салаты')    #<QuerySet [<Dishes: Сельдь под шубой>, <Dishes: Овощной салат с семе>, <Dishes: Салат-микс с цыпленк>, <Dishes: Низуаз с тунцом>, <Dishes: Оливье>, <Dishes: Цезарь>]>
    paginator = Paginator(salads, 4)   #показ на стр. по 4 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    #rows_count = (page_obj.paginator.count - 1) // 4 + 1  # Вычисляем количество рядов
    cart_product_form = CartAddProductForm()   #добавляем форму корзины
     # Получаем ингредиенты для каждого салата
    for salad in page_obj:
        ingredients = models.Ingredients.objects.filter(dishe_id=salad.id)
        salad.ingredients = []
        for ingredient in ingredients:
            product = models.Products.objects.get(id=ingredient.product_id)
            salad.ingredients.append(product.name)
     
    return render(request, 'salads.html', {'salads': salads, 
                                           'products': page_obj, 
                                           'viewed_salads':viewed_salads,
                                           'cart_product_form': cart_product_form,
                                           }) 

def show_cold_dishes (request):
    cold_dishes = models.Dishes.objects.filter(category__name='Холодные блюда')    #<QuerySet [<Dishes: Сельдь под шубой>, <Dishes: Овощной салат с семе>, <Dishes: Салат-микс с цыпленк>, <Dishes: Низуаз с тунцом>, <Dishes: Оливье>, <Dishes: Цезарь>]>
    paginator = Paginator(cold_dishes, 4)   #показ на стр. по 4 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    #rows_count = (page_obj.paginator.count - 1) // 4 + 1  # Вычисляем количество рядов
    cart_product_form = CartAddProductForm()   #добавляем форму корзины
    for cold_dish in page_obj:
        ingredients = models.Ingredients.objects.filter(dishe_id=cold_dish.id)
        cold_dish.ingredients = []
        for ingredient in ingredients:
            product = models.Products.objects.get(id=ingredient.product_id)
            cold_dish.ingredients.append(product.name)
     
    return render(request, 'cold-dishes.html', {'cold_dishes': cold_dishes, 
                                           'products': page_obj, 
                                           'cart_product_form': cart_product_form,
                                           }) 

def show_hot_dishes (request):
    hot_dishes = models.Dishes.objects.filter(category__name='Горячие блюда')    #<QuerySet [<Dishes: Сельдь под шубой>, <Dishes: Овощной салат с семе>, <Dishes: Салат-микс с цыпленк>, <Dishes: Низуаз с тунцом>, <Dishes: Оливье>, <Dishes: Цезарь>]>
    paginator = Paginator(hot_dishes, 4)   #показ на стр. по 4 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    cart_product_form = CartAddProductForm()   #добавляем форму корзины
    for hot_dish in page_obj:
        ingredients = models.Ingredients.objects.filter(dishe_id=hot_dish.id)
        hot_dish.ingredients = []
        for ingredient in ingredients:
            product = models.Products.objects.get(id=ingredient.product_id)
            hot_dish.ingredients.append(product.name)
     
    return render(request, 'hot-dishes.html', {'hot_dishes': hot_dishes, 
                                           'products': page_obj, 
                                           'cart_product_form': cart_product_form,
                                           }) 
    
def show_side_dishes (request):
    side_dishes = models.Dishes.objects.filter(category__name='Гарниры')    #<QuerySet [<Dishes: Сельдь под шубой>, <Dishes: Овощной салат с семе>, <Dishes: Салат-микс с цыпленк>, <Dishes: Низуаз с тунцом>, <Dishes: Оливье>, <Dishes: Цезарь>]>
    paginator = Paginator(side_dishes, 4)   #показ на стр. по 4 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    cart_product_form = CartAddProductForm()   #добавляем форму корзины
    for side_dish in page_obj:
        ingredients = models.Ingredients.objects.filter(dishe_id=side_dish.id)
        side_dish.ingredients = []
        for ingredient in ingredients:
            product = models.Products.objects.get(id=ingredient.product_id)
            side_dish.ingredients.append(product.name)
     
    return render(request, 'side-dishes.html', {'side_dishes': side_dishes, 
                                           'products': page_obj, 
                                           'cart_product_form': cart_product_form,
                                           }) 
    
def show_desserts (request):
    desserts = models.Dishes.objects.filter(category__name='Десерты')    #<QuerySet [<Dishes: Сельдь под шубой>, <Dishes: Овощной салат с семе>, <Dishes: Салат-микс с цыпленк>, <Dishes: Низуаз с тунцом>, <Dishes: Оливье>, <Dishes: Цезарь>]>
    paginator = Paginator(desserts, 4)   #показ на стр. по 4 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    cart_product_form = CartAddProductForm()   #добавляем форму корзины
    for dessert in page_obj:
        ingredients = models.Ingredients.objects.filter(dishe_id=dessert.id)
        dessert.ingredients = []
        for ingredient in ingredients:
            product = models.Products.objects.get(id=ingredient.product_id)
            dessert.ingredients.append(product.name)
     
    return render(request, 'desserts.html', {'desserts': desserts, 
                                           'products': page_obj, 
                                           'cart_product_form': cart_product_form,
                                           }) 
    
def show_drinkables (request):
    drinkables = models.Dishes.objects.filter(category__name='Напитки')    #<QuerySet [<Dishes: Сельдь под шубой>, <Dishes: Овощной салат с семе>, <Dishes: Салат-микс с цыпленк>, <Dishes: Низуаз с тунцом>, <Dishes: Оливье>, <Dishes: Цезарь>]>
    paginator = Paginator(drinkables, 4)   #показ на стр. по 4 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    cart_product_form = CartAddProductForm()   #добавляем форму корзины
    for drinkable in page_obj:
        ingredients = models.Ingredients.objects.filter(dishe_id=drinkable.id)
        drinkable.ingredients = []
        for ingredient in ingredients:
            product = models.Products.objects.get(id=ingredient.product_id)
            drinkable.ingredients.append(product.name)
     
    return render(request, 'drinkables.html', {'drinkables': drinkables, 
                                           'products': page_obj, 
                                           'cart_product_form': cart_product_form,
                                           }) 