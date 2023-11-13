from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from Restora.models import Dishes
from .cart import Cart
from .forms import CartAddProductForm

# Create your views here.

@require_POST   #разрешить только POST запросы, поскольку это представление изменит данные
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Dishes, id=product_id)
    print(f'prod = {product}')
    # извлекаем экземпляр продукта/блюда с заданным ID и проверяем CartAddProductForm.
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(dishe=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart:cart_detail')

def cart_remove(request, product_id):   #получает id продукта 
    print("Product ID:", product_id) 
    cart = Cart(request)
    product = get_object_or_404(Dishes, id=product_id)   #извлекаем экземпляр продукта с заданным id и удаляем продукт из корзины
    print("Product:", product) 
    cart.remove(product)
    return redirect('cart:cart_detail')

def cart_reduce(request, product_id):
    quantity = request.GET.get('quantity')
    cart = Cart(request)
    product = get_object_or_404(Dishes, id=product_id)
    cart.reduce(product, int(quantity))
    return redirect('cart:cart_detail')
    
def cart_plus(request, product_id):
    quantity = request.GET.get('quantity')
    cart = Cart(request)
    product = get_object_or_404(Dishes, id=product_id)
    cart.plus(product, int(quantity))
    return redirect('cart:cart_detail')    
    
def cart_detail(request):
    cart = Cart(request)
    print(f'cart = {cart}')
    return render(request, 'cart/detail.html', {'cart': cart})