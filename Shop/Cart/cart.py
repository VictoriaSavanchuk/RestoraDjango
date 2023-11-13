from decimal import Decimal
from django.conf import settings
from Restora.models import Dishes


class Cart(object):

    def __init__(self, request):
        """
        Инициализируем корзину, чтобы сделать ее доступной для других методов класса Cart
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)       #получаем корзину с текущей сессии 
        if not cart:
            # save an empty cart in the session   если корзина в тек сессии отсут., создаем сессию с пустой корзиной
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart
        
    def add(self, dishe, quantity=1, update_quantity=False):
        """
        Добавить продукт в корзину или обновить его количество.
        """
        product_id = str(dishe.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0,
                                    'price': str(dishe.price)}
        if update_quantity:   
            #Это логическое значение, которое указывает, требуется ли обновление
            # количества с заданным количеством (True), или же новое количество должно быть добавлено к существующему количеству (False).
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()      #сохраним корзину в сессии.
        
    def save(self):
        # Обновление сессии cart
        self.session[settings.CART_SESSION_ID] = self.cart
        # Отметить сеанс как "измененный", чтобы убедиться, что он сохранен
        self.session.modified = True
        
    def remove(self, dish):
        """
        Удаление товара из корзины.
        """
        product_id = str(dish.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()
            
    def reduce(self, dish, quantity):
        """
        Уменьшение товара в корзине.
        """
        product_id = str(dish.id)
        if product_id in self.cart:
            quantity -= 1
            if quantity <= 0:
                del self.cart[product_id]
            else:
                self.cart[product_id]['quantity'] = quantity
            self.save()      
    
    def plus(self, dish, quantity):
        """
        Увеличение товара в корзине.
        """
        product_id = str(dish.id)
        print(f'quantity = {quantity}')
        if product_id in self.cart:
            quantity += 1
            self.cart[product_id]['quantity'] = quantity
            self.save()      
            
    def __iter__(self):
        """
        Перебор элементов в корзине и получение продуктов из базы данных.
        """
        product_ids = self.cart.keys()
        # получение объектов product и добавление их в корзину
        dishes = Dishes.objects.filter(id__in=product_ids)
        for dish in dishes:
            self.cart[str(dish.id)]['dish'] = dish      

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item        
            
    def __len__(self):
        """
        Подсчет всех товаров в корзине.
        Мы возвращаем сумму количества всех товаров.
        """
        return sum(item['quantity'] for item in self.cart.values())
    
    def get_total_price(self):
        """
        Подсчет стоимости товаров в корзине.
        """
        return sum(Decimal(item['price']) * item['quantity'] for item in
                self.cart.values())
        
    def clear(self):
        # удаление корзины из сессии
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True