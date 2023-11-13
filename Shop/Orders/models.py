from django.db import models

# Create your models here.
from django.db import models
from Restora.models import Dishes
from django.core.validators import RegexValidator



class Order(models.Model):
    first_name = models.CharField('Имя', max_length=100)
    last_name = models.CharField('Фамилия', max_length=100)
    phoneNumberRegex = RegexValidator(regex = r"^(\+375|80)-(29|25|44|33)-(\d{3})(\d{2})(\d{2})$")
    phone = models.CharField('Телефон',
        validators=[phoneNumberRegex],
        max_length=15,
        unique=True,
        default=None
    )
    email = models.EmailField()
    address = models.CharField('Адрес', max_length=250)
    city = models.CharField('Город', max_length=100)
    created = models.DateTimeField('Время заказа', auto_now_add=True)
    updated = models.DateTimeField('Обновлено', auto_now=True)
    paid = models.BooleanField(default=False)    #поле для различения оплаченных и неоплаченных заказов

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):        #общую стоимость товаров, купленных в этом заказе
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items', verbose_name='Заказ')
    dish = models.ForeignKey(Dishes, on_delete=models.SET_DEFAULT, related_name='order_items', verbose_name='Блюдо', null=True, default=None)
    price = models.DecimalField('Стоимость', max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField('Количество', default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):    #для возврата стоимости товара
        return self.price * self.quantity